# Development Environment Setup

Instructions for developers working on the OpenClaw UNRAID template.

## Prerequisites

- **Git**: Version control
- **Docker**: Container runtime
- **Docker Compose**: Multi-container orchestration
- **Python 3.8+**: For validation scripts
- **Node.js** (optional): For npm scripts

### Installation

**macOS/Linux:**
```bash
# Install Docker & Docker Compose
curl https://get.docker.com | sh

# Or use package manager
brew install docker docker-compose  # macOS
sudo apt install docker.io docker-compose  # Linux
```

**Windows:**
- Download [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Includes Docker & Docker Compose

## Clone Repository

```bash
git clone https://github.com/openclaw/openclaw-unraid-template.git
cd openclaw-unraid-template
```

## Local Development Setup

### Start Container

```bash
# Start OpenClaw locally
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f openclaw
```

Container will be available at: `http://localhost:18789/`

### Stop Container

```bash
docker-compose down
```

### Rebuild Image

```bash
docker-compose up -d --build
```

## Project Structure

```
.
├── template/              # UNRAID template files
│   └── openclaw.xml      # ⭐ The actual template
├── docker/                # Docker configuration
│   └── Dockerfile        # Container image definition
├── docs/                  # Documentation
│   ├── INSTALL.md
│   ├── CONFIGURATION.md
│   └── CHANNELS.md
├── scripts/               # Utility scripts
│   └── validate-template.py
├── .github/workflows/     # CI/CD configuration
│   ├── build-and-push.yml
│   └── validate.yml
├── docker-compose.yml    # Local dev setup
├── manage.sh             # Helper script
└── README.md
```

## Validation

### Validate Template

```bash
# Using Python script
python3 scripts/validate-template.py

# Using npm
npm run validate

# Manual XML validation
python3 -c "import xml.etree.ElementTree as ET; ET.parse('template/openclaw.xml'); print('✓ Valid')"
```

### Validate Docker Compose

```bash
docker-compose config > /dev/null && echo "✓ Valid"
```

### Validate Dockerfile

```bash
docker build -f docker/Dockerfile -t openclaw:test .
```

## Making Changes

### Edit Template (openclaw.xml)

```bash
# Open in editor
code template/openclaw.xml  # VS Code
vim template/openclaw.xml   # Vim
```

**After changes:**
1. Validate XML: `python3 scripts/validate-template.py`
2. Test in UNRAID (or docker-compose locally)
3. Commit: `git add template/openclaw.xml && git commit -m "Update: description"`

### Edit Dockerfile

```bash
# Make changes
vim docker/Dockerfile

# Rebuild and test
docker-compose up -d --build

# Check logs
docker-compose logs -f openclaw
```

### Edit Documentation

Documentation is in `docs/` directory:
- `INSTALL.md` - Installation guide
- `CONFIGURATION.md` - Config reference
- `CHANNELS.md` - Channel setup guides

```bash
# Edit documentation
vim docs/INSTALL.md

# Preview markdown (optional)
# Use VS Code preview or https://marked.js.org/demo
```

**Before committing:**
- Verify all links are correct
- Test any code examples
- Check formatting (markdown)

## Testing Locally

### Full Local Setup

```bash
# Start fresh
docker-compose down -v
docker-compose up -d --build

# Wait for container to start (~30 seconds)
sleep 30

# Check health
docker-compose ps

# Access WebUI
open http://localhost:18789/  # macOS
xdg-open http://localhost:18789/  # Linux
start http://localhost:18789/  # Windows
```

### Shell Access

```bash
docker exec -it openclaw sh

# Inside container
ps aux
ls -la /app
cat /home/node/.openclaw/openclaw.json  # View config
```

### View Logs

```bash
# Last 50 lines
docker-compose logs openclaw | tail -50

# Follow in real-time
docker-compose logs -f openclaw

# With timestamps
docker-compose logs -f --timestamps openclaw
```

## Git Workflow

### Create Feature Branch

```bash
git checkout -b feature/my-feature
# or
git checkout -b fix/bug-name
```

### Make Changes

```bash
# Edit files
vim template/openclaw.xml

# Test changes
python3 scripts/validate-template.py

# Stage changes
git add template/openclaw.xml docs/

# Commit with clear message
git commit -m "Add: new environment variable for X"
# or
git commit -m "Fix: incorrect port mapping"
```

### Push and Create PR

```bash
git push origin feature/my-feature

# Then create PR on GitHub
```

### Commit Message Format

```
type(scope): description

Examples:
- Add: new configuration option
- Fix: template XML validation error
- Docs: improve INSTALL.md instructions
- Test: add validation tests
- Refactor: improve Dockerfile structure
```

## Common Tasks

### Add New Configuration Option

1. Edit `template/openclaw.xml` - Add `<Config>` element
2. Update `docs/CONFIGURATION.md` - Document the option
3. Update `docker/Dockerfile` - If it needs special setup
4. Test locally with `docker-compose`
5. Validate: `python3 scripts/validate-template.py`

### Add New Channel Setup Guide

1. Edit `docs/CHANNELS.md` - Add section for channel
2. Include step-by-step setup instructions
3. Provide configuration examples
4. Test instructions work (if possible)

### Fix Container Startup Issue

1. Check logs: `docker-compose logs -f openclaw`
2. Edit `docker/Dockerfile`
3. Rebuild: `docker-compose up -d --build`
4. Test: `docker-compose logs openclaw`
5. Commit fix

## Troubleshooting

### Build Fails

```bash
# Full rebuild with no cache
docker-compose build --no-cache

# Check Dockerfile syntax
docker build --dry-run -f docker/Dockerfile .

# Check logs for errors
docker-compose logs openclaw
```

### Port Already in Use

```bash
# Change port in docker-compose.yml
# Or kill process:
# macOS/Linux:
lsof -i :18789
kill -9 <PID>

# Windows:
netstat -ano | findstr :18789
taskkill /PID <PID> /F
```

### Git Conflicts

```bash
# Update from main
git fetch origin
git rebase origin/main

# Or merge if you prefer
git merge origin/main

# Resolve conflicts and continue
```

## Code Review Checklist

Before creating a PR, verify:

- ✅ XML template validates: `python3 scripts/validate-template.py`
- ✅ docker-compose.yml valid: `docker-compose config`
- ✅ Dockerfile builds: `docker-compose build`
- ✅ Container starts: `docker-compose up -d`
- ✅ WebUI accessible: `http://localhost:18789/`
- ✅ Documentation updated
- ✅ No credentials in code
- ✅ Commit messages are clear

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [UNRAID Documentation](https://docs.unraid.net/)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)
- [Git Documentation](https://git-scm.com/doc)

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/openclaw/openclaw-unraid-template/issues)
- **Discussions**: [GitHub Discussions](https://github.com/openclaw/openclaw-unraid-template/discussions)
- **Contributing**: See `CONTRIBUTING.md`

---

Happy coding! 🚀
