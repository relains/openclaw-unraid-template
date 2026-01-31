# OpenClaw UNRAID Template - Quick Reference

## Directory Structure

```
openclaw-unraid-template/
├── template/
│   └── openclaw.xml                # UNRAID template (install this)
├── docker/
│   └── Dockerfile                  # Docker image definition
├── docs/
│   ├── INSTALL.md                 # Installation guide
│   ├── CONFIGURATION.md           # Configuration reference
│   └── CHANNELS.md                # Channel setup guides
├── scripts/
│   └── validate-template.py       # Validation script
├── .github/workflows/
│   ├── build-and-push.yml         # CI/CD (build & push)
│   └── validate.yml               # CI/CD (validation)
├── docker-compose.yml             # Local development
├── manage.sh                       # Helper script
├── README.md                       # Main README
├── CONTRIBUTING.md                # Contribution guide
├── SECURITY.md                    # Security policy
├── LICENSE                        # MIT License
└── package.json                   # Project metadata

appdata/                           # Generated on first run
├── config/                        # Configuration files
└── workspace/                     # Workspace data
```

## Key Files to Know

| File | Purpose |
|------|---------|
| `template/openclaw.xml` | **This is what you import into UNRAID** |
| `docker/Dockerfile` | Builds the Docker image (from OpenClaw repo) |
| `docs/INSTALL.md` | Complete installation + setup guide |
| `docker-compose.yml` | For local development/testing |
| `manage.sh` | Helper commands (Linux/macOS) |

## Getting Started

### 1. Import Template into UNRAID

Copy the URL to your template:
```
https://raw.githubusercontent.com/relains/openclaw-unraid-template/main/template/openclaw.xml
```

Or use template file directly from GitHub.

### 2. Install on UNRAID

1. Apps → Community Applications
2. Search "OpenClaw" or paste template URL
3. Click Install
4. Configure ports & paths
5. Start container

### 3. Access WebUI

```
http://your-unraid-ip:18789/
```

### 4. Configure Channels

See `docs/CHANNELS.md` for setup guides:
- Telegram
- Discord
- Slack
- WhatsApp
- And more...

## Local Development

```bash
# Start
docker-compose up -d

# Check logs
docker-compose logs -f openclaw

# Access
http://localhost:18789/

# Stop
docker-compose down

# Or use helper script
./manage.sh start
./manage.sh logs
./manage.sh stop
```

## Validation

```bash
# Validate template
python3 scripts/validate-template.py

# Or with npm
npm run validate
```

## Docker Hub

Docker images are built and pushed to:
```
docker pull openclaw/openclaw:latest
```

(Configuration depends on Docker Hub setup)

## Configuration Files

### Basic Config
```json
// ~/.openclaw/openclaw.json
{
  "gateway": {
    "bind": "0.0.0.0",
    "port": 18789
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  }
}
```

See `docs/CONFIGURATION.md` for full reference.

## Messaging Channels

Supported platforms:
- ✅ WebChat (built-in)
- ✅ Telegram
- ✅ Discord  
- ✅ Slack
- ✅ WhatsApp
- ✅ Google Chat
- ✅ Signal
- ✅ iMessage (macOS)
- ✅ Teams
- ✅ Matrix
- ✅ Zalo

See `docs/CHANNELS.md` for detailed setup per channel.

## Ports

| Port | Purpose | UNRAID Default |
|------|---------|-----------------|
| 18789 | Gateway (required) | 18789 |
| 18790 | Bridge (optional) | 18790 |

Change in UNRAID Docker settings if conflicts.

## Volumes

| Container Path | Host Path | Purpose |
|----------------|-----------|---------|
| `/home/node/.openclaw` | `/mnt/user/appdata/openclaw/config` | Config |
| `/home/node/openclaw-workspace` | `/mnt/user/appdata/openclaw/workspace` | Workspace |

Persist data across container restarts.

## Environment Variables

Set in UNRAID container settings (Advanced):

| Variable | Purpose |
|----------|---------|
| `CLAWDBOT_GATEWAY_TOKEN` | Auth token (optional) |
| `CLAUDE_AI_SESSION_KEY` | Claude API key (optional) |
| `CLAUDE_WEB_SESSION_KEY` | Claude Web session (optional) |
| `CLAUDE_WEB_COOKIE` | Claude Web cookie (optional) |

More in `docs/CONFIGURATION.md`.

## Troubleshooting

### Container won't start
- Check logs: `docker logs openclaw`
- Verify ports not in use
- Check disk space

### WebUI not accessible
- Check firewall
- Verify port mapping
- Check container health

### No AI responses
- Verify Claude credentials
- Check logs for errors
- Test internet connectivity

See `docs/INSTALL.md` for full troubleshooting.

## CI/CD Pipeline

GitHub Actions automate:
- ✅ Building Docker image
- ✅ Pushing to registry
- ✅ Validating template XML
- ✅ Checking docker-compose
- ✅ Security scanning (Trivy)
- ✅ Creating releases

## Support & Documentation

- **OpenClaw**: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- **UNRAID**: [unraid.net](https://unraid.net)
- **Issues**: [GitHub Issues](https://github.com/openclaw/openclaw-unraid-template/issues)
- **Contributing**: See `CONTRIBUTING.md`
- **Security**: See `SECURITY.md`

## License

MIT License - See `LICENSE` file

---

**Questions?** Check the documentation or open an issue on GitHub!
