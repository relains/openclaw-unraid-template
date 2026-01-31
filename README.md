# OpenClaw UNRAID Template

A complete UNRAID application template for OpenClaw — your personal AI assistant platform that connects multiple messaging channels to a single control plane.

## Overview

OpenClaw is a Node.js-based AI assistant gateway that allows you to:

- **Connect Multiple Messaging Platforms**: WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Teams, Matrix, Zalo, WebChat
- **Unified Control Plane**: Single WebSocket gateway managing all channels
- **AI-Powered Responses**: Powered by Claude API or local AI models
- **Voice Support**: Wake-word detection and voice responses
- **Companion Apps**: macOS menu bar app, iOS and Android nodes
- **Self-Hosted**: Run entirely on your own infrastructure
- **Secure**: Token-based authentication and sandboxing

## Quick Start

### 1. Install via UNRAID

1. Navigate to **Apps** in UNRAID
2. Search for **"OpenClaw"** or add this repository URL
3. Click **Install** and configure:
   - **Gateway Port**: Default `18789` (required)
   - **Bridge Port**: Default `18790` (optional, for device pairing)
   - **Config Path**: Maps to `~/.openclaw`
   - **Workspace Path**: Maps to `~/clawd`

### 2. First Access

After installation:
- Navigate to `http://your-unraid-ip:18789/` in your browser
- You'll see the OpenClaw WebChat interface
- Initial setup wizard will guide you through configuration

### 3. Configure AI Backend

Set environment variables in container settings:
- **CLAUDE_AI_SESSION_KEY**: Your Claude AI session key
- **CLAUDE_WEB_SESSION_KEY**: Claude Web session (optional)
- **CLAUDE_WEB_COOKIE**: Claude Web authentication (optional)

See [INSTALL.md](docs/INSTALL.md) for detailed configuration.

## Key Ports

| Port | Purpose | Required |
|------|---------|----------|
| **18789** | WebSocket Gateway (main control plane) | ✅ Yes |
| **18790** | Bridge port (device pairing) | ⭕ Optional |

## Data Volumes

| Container Path | Host Path | Purpose |
|----------------|-----------|---------|
| `/home/node/.openclaw` | `/mnt/user/appdata/openclaw/config` | Configuration files & credentials |
| `/home/node/clawd` | `/mnt/user/appdata/openclaw/workspace` | Workspace data & channel configs |

## Repository Structure

```
openclaw-unraid-template/
├── template/
│   └── openclaw.xml          # UNRAID template definition
├── docker/
│   └── Dockerfile            # Docker image build
├── docs/
│   ├── INSTALL.md           # Detailed installation guide
│   ├── CONFIGURATION.md     # Configuration reference
│   └── CHANNELS.md          # Messaging channel setup
├── .github/workflows/
│   └── build-and-push.yml   # CI/CD pipeline
├── docker-compose.yml       # Local development
└── README.md                # This file
```

## Local Development

### Build Locally

```bash
# Clone and build
docker-compose up --build

# Access the container
docker exec -it openclaw sh

# View logs
docker-compose logs -f openclaw
```

### Rebuild Docker Image

```bash
# Build image
docker build -f docker/Dockerfile -t openclaw:latest .

# Push to registry (if configured)
docker push openclaw:latest
```

## Configuration

### Minimal Setup

After installation, create a basic configuration file in the config directory:

```json
# ~/.openclaw/openclaw.json
{
  "gateway": {
    "port": 18789,
    "token": "your-secure-token"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  }
}
```

### Full Configuration Reference

See [CONFIGURATION.md](docs/CONFIGURATION.md) for complete options and channel setup.

## Connecting Messaging Channels

OpenClaw supports these channels:

- **WhatsApp**: Via qrcode pairing
- **Telegram**: Using bot token
- **Slack**: Workspace app integration
- **Discord**: Bot token setup
- **Google Chat**: Service account configuration
- **Signal**: Phone number registration
- **iMessage**: macOS companion app
- **Teams**: Bot app registration
- **Matrix**: Homeserver configuration
- **Zalo**: Phone account pairing
- **WebChat**: Built-in web interface

See [CHANNELS.md](docs/CHANNELS.md) for detailed setup instructions per channel.

## Security Considerations

- Runs as non-root user (`node:node`, uid 1000)
- Config directory contains sensitive credentials — back it up securely
- Use strong authentication tokens
- Consider firewall rules to restrict access to trusted networks
- For remote access, use VPN or reverse proxy with authentication
- Default: Gateway binds to all interfaces (0.0.0.0) — adjust as needed for security

## Troubleshooting

### Container won't start
- Check logs: `docker logs openclaw`
- Verify ports 18789/18790 are not in use
- Ensure config directory has proper permissions

### WebUI not accessible
- Check firewall rules
- Verify port mapping: `docker port openclaw`
- Ensure gateway is running: `curl http://localhost:18789/`

### AI responses not working
- Verify Claude session keys are set correctly
- Check logs for authentication errors
- Ensure internet connectivity for API calls

For more help, see [INSTALL.md](docs/INSTALL.md) or open an issue on [GitHub](https://github.com/openclaw/openclaw/issues).

## Support

- **GitHub Issues**: [openclaw/openclaw](https://github.com/openclaw/openclaw/issues)
- **Documentation**: [openclaw docs](https://github.com/openclaw/openclaw#readme)
- **Community**: UNRAID forums

## License

This template inherits the license from the [OpenClaw project](https://github.com/openclaw/openclaw).

## Related Projects

- **OpenClaw**: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- **UNRAID**: [unraid.net](https://unraid.net)
