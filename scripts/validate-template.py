#!/usr/bin/env python3
"""
Validate UNRAID OpenClaw template and configuration.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def validate_xml_template(template_path: str) -> bool:
    """Validate UNRAID XML template."""
    print("=" * 60)
    print("UNRAID Template Validation")
    print("=" * 60)
    
    try:
        tree = ET.parse(template_path)
        root = tree.getroot()
        
        # Validate root element
        if root.tag != 'Container':
            print(f"✗ Root element must be 'Container', got '{root.tag}'")
            return False
        
        version = root.get('version')
        if version != '2':
            print(f"✗ Template version must be '2', got '{version}'")
            return False
        
        print(f"✓ Root element valid (Container v{version})")
        
        # Check required fields
        required_fields = {
            'Name': str,
            'Repository': str,
            'Network': str,
            'Shell': str,
            'Privileged': str,
        }
        
        missing = []
        for field, field_type in required_fields.items():
            elem = root.find(field)
            if elem is None:
                missing.append(field)
            elif not elem.text or elem.text.strip() == '':
                missing.append(f"{field} (empty)")
        
        if missing:
            print(f"✗ Missing required fields: {', '.join(missing)}")
            return False
        
        print(f"✓ All required fields present")
        
        # Validate Configs
        configs = root.findall('Config')
        valid_configs = 0
        
        for i, config in enumerate(configs):
            config_name = config.get('Name')
            config_type = config.get('Type')
            config_target = config.get('Target')
            
            if not config_name:
                print(f"✗ Config[{i}] missing Name")
                continue
            
            if not config_type:
                print(f"✗ Config '{config_name}' missing Type")
                continue
            
            if not config_target:
                print(f"✗ Config '{config_name}' missing Target")
                continue
            
            valid_type = config_type in ['Port', 'Path', 'Variable']
            if not valid_type:
                print(f"✗ Config '{config_name}' has invalid Type '{config_type}'")
                continue
            
            valid_configs += 1
        
        print(f"✓ {valid_configs}/{len(configs)} Configs are valid")
        
        if valid_configs != len(configs):
            return False
        
        # Check recommended fields
        recommended = ['Icon', 'Overview', 'Category', 'WebUI', 'Support', 'Project']
        missing_recommended = []
        
        for field in recommended:
            elem = root.find(field)
            if elem is None or not elem.text or elem.text.strip() == '':
                missing_recommended.append(field)
        
        if missing_recommended:
            print(f"⚠ Missing recommended fields: {', '.join(missing_recommended)}")
        else:
            print(f"✓ All recommended fields present")
        
        print("\n✓ Template validation passed!")
        return True
        
    except ET.ParseError as e:
        print(f"✗ XML Parse Error: {e}")
        return False
    except Exception as e:
        print(f"✗ Validation Error: {e}")
        return False


def validate_dockerfile(dockerfile_path: str) -> bool:
    """Validate Dockerfile."""
    print("\n" + "=" * 60)
    print("Dockerfile Validation")
    print("=" * 60)
    
    try:
        if not Path(dockerfile_path).exists():
            print(f"⚠ Dockerfile not found at {dockerfile_path}")
            return True
        
        with open(dockerfile_path, 'r') as f:
            content = f.read()
        
        if 'FROM' not in content:
            print("✗ Dockerfile missing FROM instruction")
            return False
        
        print("✓ Dockerfile has FROM instruction")
        
        if 'EXPOSE' in content:
            print("✓ Dockerfile has EXPOSE instruction")
        
        if 'HEALTHCHECK' in content:
            print("✓ Dockerfile has HEALTHCHECK")
        
        if 'USER' in content and 'root' not in content:
            print("✓ Dockerfile uses non-root user")
        
        print("\n✓ Dockerfile validation passed!")
        return True
        
    except Exception as e:
        print(f"✗ Dockerfile validation error: {e}")
        return False


def validate_docker_compose(compose_path: str) -> bool:
    """Validate docker-compose.yml."""
    print("\n" + "=" * 60)
    print("Docker Compose Validation")
    print("=" * 60)
    
    try:
        import yaml
        
        if not Path(compose_path).exists():
            print(f"⚠ docker-compose.yml not found at {compose_path}")
            return True
        
        with open(compose_path, 'r') as f:
            compose = yaml.safe_load(f)
        
        if not compose or 'services' not in compose:
            print("✗ docker-compose.yml missing 'services' section")
            return False
        
        print("✓ Services section present")
        
        services = compose['services']
        if 'openclaw' not in services:
            print("⚠ 'openclaw' service not found")
        else:
            service = services['openclaw']
            
            if 'image' in service:
                print(f"✓ Image defined: {service['image']}")
            
            if 'ports' in service:
                print(f"✓ Ports defined: {service['ports']}")
            
            if 'volumes' in service:
                print(f"✓ Volumes defined: {len(service['volumes'])} mount(s)")
            
            if 'environment' in service:
                print(f"✓ Environment variables defined")
        
        print("\n✓ Docker Compose validation passed!")
        return True
        
    except ImportError:
        print("⚠ PyYAML not installed, skipping YAML validation")
        return True
    except Exception as e:
        print(f"✗ Docker Compose validation error: {e}")
        return False


def main():
    """Run all validations."""
    results = []
    
    # Validate template
    template_path = 'template/openclaw.xml'
    results.append(('Template', validate_xml_template(template_path)))
    
    # Validate Dockerfile
    results.append(('Dockerfile', validate_dockerfile('docker/Dockerfile')))
    
    # Validate docker-compose
    results.append(('Docker Compose', validate_docker_compose('docker-compose.yml')))
    
    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    
    all_passed = all(result[1] for result in results)
    
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status:8} {name}")
    
    if all_passed:
        print("\n✓ All validations passed!")
        return 0
    else:
        print("\n✗ Some validations failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
