# Contributing to OpenClaw UNRAID Template

We welcome contributions! Here's how you can help:

## Types of Contributions

- 🐛 **Bug Reports**: Found an issue? [Open an issue](https://github.com/openclaw/openclaw-unraid-template/issues)
- 🎨 **Improvements**: Better documentation, icon, template layout
- 🔧 **Features**: New channel integrations, configuration options
- 📝 **Documentation**: Clarifications, examples, translations
- 🧪 **Testing**: Report issues you find in UNRAID

## Getting Started

### Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/openclaw-unraid-template.git
cd openclaw-unraid-template
```

### Test Locally

```bash
# Build and run locally
docker-compose up --build

# Check logs
docker-compose logs -f openclaw

# Access WebUI
open http://localhost:18789/
```

### Validate Changes

```bash
# Validate XML template
python3 << 'EOF'
import xml.etree.ElementTree as ET
ET.parse('template/openclaw.xml')
print("✓ Template is valid")
EOF

# Validate docker-compose
docker-compose config
```

## Development Workflow

1. **Create a feature branch**: `git checkout -b feature/your-feature`
2. **Make changes**: Edit files as needed
3. **Test locally**: Ensure everything works with `docker-compose`
4. **Validate**: Run validation scripts
5. **Commit**: `git commit -m "Add: description of changes"`
6. **Push**: `git push origin feature/your-feature`
7. **Open PR**: Create a pull request on GitHub

## File Structure

- **template/openclaw.xml** — UNRAID template definition (critical)
- **docker/Dockerfile** — Docker image build definition
- **docs/** — User documentation
- **docker-compose.yml** — Local development setup
- **.github/workflows/** — CI/CD automation

## Making Changes

### Update Template XML

Edit `template/openclaw.xml` to modify:
- Container metadata (Name, Icon, Description)
- Ports (change if needed)
- Volumes/paths
- Environment variables
- Configuration options

**Validate after changes**:
```bash
python3 -c "import xml.etree.ElementTree as ET; ET.parse('template/openclaw.xml'); print('Valid')"
```

### Update Dockerfile

Edit `docker/Dockerfile` to:
- Add system dependencies
- Change base image
- Modify build steps
- Add health checks

**Test with**:
```bash
docker-compose up --build
```

### Update Documentation

Edit files in `docs/`:
- `INSTALL.md` — Installation guide
- `CONFIGURATION.md` — Config reference
- `CHANNELS.md` — Channel setup guides

Use clear examples and test instructions work.

## Pull Request Guidelines

1. **Clear title**: "Add: X feature" or "Fix: X bug"
2. **Description**: Explain what changed and why
3. **Screenshots**: If UI changes, include screenshots
4. **Testing**: Describe how you tested
5. **Breaking changes**: Note any breaking changes clearly

### PR Title Format

```
type(scope): description

- Add: New feature description
- Fix: Bug fix description
- Docs: Documentation improvements
- Refactor: Code restructuring
- Test: Test additions
```

## Code Standards

- **XML**: Proper indentation (2 spaces), valid syntax
- **Bash**: POSIX compliant, quoted variables
- **Python**: PEP 8 style
- **Markdown**: Proper formatting, working links

## Testing Checklist

Before submitting a PR:

- [ ] Template XML validates
- [ ] docker-compose.yml valid
- [ ] Dockerfile builds successfully
- [ ] Container starts and is healthy
- [ ] WebUI accessible at configured port
- [ ] Documentation reflects changes
- [ ] No secrets or credentials in code
- [ ] Links in docs are valid

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/openclaw/openclaw-unraid-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/openclaw/openclaw-unraid-template/discussions)
- **OpenClaw Docs**: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🙏
