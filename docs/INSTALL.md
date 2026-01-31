# Installation Guide

Comprehensive guide for installing and setting up OpenClaw on UNRAID.

## Prerequisites

- UNRAID server version 6.8 or higher
- Docker support enabled (default on UNRAID)
- ~2GB RAM recommended
- ~10GB disk space for appdata and workspace
- Active internet connection for AI/channel connectivity

## Step-by-Step Installation

### Step 1: Add the Template to UNRAID

**Option A: Via Template Repo (Recommended)**

1. In UNRAID Web UI, go to **Apps**
2. Click **Community Applications** (if not visible, enable it in settings)
3. Search for **OpenClaw**
4. Click the OpenClaw template
5. Click **Install**

**Option B: Via Template URL**

1. Go to **Apps** → **Community Applications**
2. Click **Check for Updates** or search bar
3. Paste template URL: `https://raw.githubusercontent.com/relains/openclaw-unraid-template/main/template/openclaw.xml`
4. Click the result
5. Click **Install**

### Step 2: Configure Container Settings

When the installation dialog appears, configure:

#### **Required Settings**

| Setting | Value | Notes |
|---------|-------|-------|
| **Container Name** | `openclaw` | Default; change if running multiple instances |
| **Gateway Port** | `18789` | UNRAID → Container port mapping |
| **Bridge Port** | `18790` | Optional, for device pairing |
| **Config Path** | `/mnt/user/appdata/openclaw/config` | Where configs are stored |
| **Workspace Path** | `/mnt/user/appdata/openclaw/workspace` | Where data is stored |

#### **Advanced Settings (Optional)**

Scroll to "Advanced View" for these environment variables:

- **CLAWDBOT_GATEWAY_TOKEN**: Authentication token for gateway (set if you need access control)
- **CLAUDE_AI_SESSION_KEY**: Session key for Claude API (if using Claude backend)
- **CLAUDE_WEB_SESSION_KEY**: Claude Web session (optional)
- **CLAUDE_WEB_COOKIE**: Claude Web auth cookie (optional)

Don't set these initially if you're unsure — you can add them later by editing the container.

### Step 3: Start the Container

1. After configuration, click **Apply**
2. UNRAID will download the image and start the container
3. Watch the logs in the Docker section to ensure it starts successfully

Check Docker section for logs:
```
HEALTHY status indicates the container is ready
```

### Step 4: Access the WebUI

1. Open your browser and navigate to: `http://your-unraid-ip:18789/`
   - Replace `your-unraid-ip` with your UNRAID server's IP address
   - Example: `http://192.168.1.100:18789/`

2. You should see the **OpenClaw WebChat** interface

3. Initial setup wizard will appear — follow the prompts

## Post-Installation Configuration

### Create Initial Config File

The config directory is now available at:
```
/mnt/user/appdata/openclaw/config/
```

Create a basic configuration file:

**File**: `/mnt/user/appdata/openclaw/config/openclaw.json`

```json
{
  "gateway": {
    "bind": "0.0.0.0",
    "port": 18789,
    "token": "your-secure-token-here"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  },
  "channels": {
    "webchat": {
      "enabled": true
    }
  },
  "security": {
    "allowlist": [],
    "blocklist": []
  }
}
```

### Add AI Backend Credentials

To enable AI responses, you need Claude API credentials:

#### For Claude API:

1. Get your session key from [console.anthropic.com](https://console.anthropic.com)
2. Edit the container in UNRAID Docker tab
3. Add environment variable:
   ```
   CLAUDE_AI_SESSION_KEY = sk-ant-...
   ```
4. Restart the container

#### For Claude Web (Browser-Based):

1. Obtain your Claude Web session credentials
2. Add to container environment:
   ```
   CLAUDE_WEB_SESSION_KEY = your-session-key
   CLAUDE_WEB_COOKIE = your-cookie
   ```

## Connecting Messaging Channels

Once OpenClaw is running, you can connect multiple messaging platforms.

### WhatsApp

1. In WebUI, navigate to **Channels** → **WhatsApp**
2. Scan the QR code with WhatsApp on your phone
3. Confirm pairing
4. Messages will now route through OpenClaw

### Telegram

1. Create a bot via [@BotFather](https://t.me/botfather) on Telegram
2. Copy the bot token
3. In WebUI, go to **Channels** → **Telegram**
4. Paste the bot token
5. Your Telegram bot is now connected

### Discord

1. Create a Discord application at [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a bot and get the token
3. Go to **Channels** → **Discord** in WebUI
4. Paste the bot token
5. Invite the bot to your servers

### Slack

1. Create an app at [Slack API](https://api.slack.com/apps)
2. Get your bot token and signing secret
3. In WebUI, **Channels** → **Slack**
4. Enter credentials
5. Install the app in your workspace

### Other Channels

Similar setup for: Google Chat, Signal, iMessage (macOS), Teams, Matrix, Zalo

See [CHANNELS.md](CHANNELS.md) for detailed instructions per channel.

## Backup and Restoration

### Backup Your Config

The config directory contains all your settings and channel credentials:

```bash
# On UNRAID terminal
tar -czf /mnt/user/backups/openclaw-backup-$(date +%Y%m%d).tar.gz \
  /mnt/user/appdata/openclaw/config/
```

Or use UNRAID's built-in backup via WebUI.

### Restore from Backup

```bash
# Stop the container first in UNRAID WebUI

# Extract backup
tar -xzf /mnt/user/backups/openclaw-backup-20250129.tar.gz -C /

# Restart container
```

## Updating

### Update to Latest Version

1. In UNRAID WebUI, go to **Docker** tab
2. Find **openclaw** container
3. Click **Force Update** to pull latest image
4. Container will be recreated with new image

### View Logs

```bash
# Via UNRAID WebUI Docker tab — click "Logs" on the openclaw container

# Via terminal
docker logs openclaw

# Follow logs in real-time
docker logs -f openclaw
```

## Troubleshooting

### Container Won't Start

**Check logs:**
```bash
docker logs openclaw
```

**Common issues:**

1. **Port Already in Use**
   - Check if ports 18789 or 18790 are bound to another container
   - In UNRAID, change Gateway Port to a different number

2. **Insufficient Disk Space**
   - Check available space: `df -h /mnt/user/appdata/`
   - Free up space or increase cache drive

3. **Permissions Error**
   - Ensure `/mnt/user/appdata/openclaw/config/` directories exist and are writable
   - Run: `chmod -R 755 /mnt/user/appdata/openclaw/config/`

### WebUI Not Accessible

1. **Can't reach `http://localhost:18789/`**
   - Verify container is running in UNRAID Docker tab
   - Check port mapping: `docker port openclaw`
   - Check firewall rules on UNRAID

2. **Connection Refused**
   - Container may still be starting (wait 10-15 seconds)
   - Check logs for startup errors
   - Try: `curl http://localhost:18789/` from UNRAID terminal

### AI Responses Not Working

1. **"No AI backend configured"**
   - Set CLAUDE_AI_SESSION_KEY or Claude Web credentials
   - Restart container

2. **"Authentication failed"**
   - Verify your Claude session key is correct
   - Check for special characters or copy-paste errors
   - Generate a new key from Claude

3. **"Connection timeout"**
   - Verify internet connectivity from UNRAID
   - Check firewall rules allow HTTPS outbound
   - Verify Claude service is online: [status.anthropic.com](https://status.anthropic.com)

### Messaging Channel Not Receiving Messages

1. Verify channel credentials are correct
2. Check logs for errors: `docker logs openclaw | grep channel-name`
3. Ensure firewall/networking allows inbound webhooks (for Slack, Discord, etc.)
4. Verify bot permissions in the respective platform

## Getting Help

- **UNRAID Forum**: [unraid.net/community](https://unraid.net/community)
- **OpenClaw Issues**: [github.com/openclaw/openclaw/issues](https://github.com/openclaw/openclaw/issues)
- **Documentation**: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

## Advanced Configuration

### Custom Bind Address

By default, gateway listens on `0.0.0.0` (all interfaces). For security, restrict to loopback:

Edit `/mnt/user/appdata/openclaw/config/openclaw.json`:
```json
{
  "gateway": {
    "bind": "127.0.0.1",
    "port": 18789
  }
}
```

Then restart container.

### Multiple Instances

You can run multiple OpenClaw instances (e.g., for different workspaces):

1. Install OpenClaw template again with different container name
2. Use different ports: 18791, 18792, etc.
3. Use different config paths: `/mnt/user/appdata/openclaw-2/`, etc.

### Resource Limits

In UNRAID Docker settings, you can limit:
- **CPU Cores**: CPUs available
- **Memory**: RAM allocation (default: unlimited)

Recommended: 2 CPU cores, 2-4GB RAM

## Next Steps

- [CONFIGURATION.md](CONFIGURATION.md) — Complete configuration reference
- [CHANNELS.md](CHANNELS.md) — Connect messaging platforms
- [GitHub Wiki](https://github.com/openclaw/openclaw/wiki) — Advanced topics
