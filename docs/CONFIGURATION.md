# Configuration Reference

Complete configuration options for OpenClaw.

## Configuration File

OpenClaw reads configuration from:
```
~/.openclaw/openclaw.json
~/.openclaw/config.json  (alternative, full config)
```

## Basic Structure

```json
{
  "gateway": {
    "bind": "0.0.0.0",
    "port": 18789,
    "token": "optional-auth-token"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  },
  "channels": {
    "webchat": { "enabled": true },
    "telegram": { "enabled": false },
    "discord": { "enabled": false }
  },
  "security": {
    "allowlist": [],
    "blocklist": []
  }
}
```

## Gateway Settings

### `gateway.bind`
**Type**: String (IP address)  
**Default**: `0.0.0.0` (all interfaces)  
**Examples**:
- `0.0.0.0` — Listen on all interfaces (public)
- `127.0.0.1` — Localhost only (secure)
- `192.168.1.100` — Specific IP address

**Note**: For UNRAID, `0.0.0.0` is typical. Use `127.0.0.1` if behind a reverse proxy.

### `gateway.port`
**Type**: Integer  
**Default**: `18789`  
**Range**: `1024-65535`  

Change only if port is in use. Update UNRAID container mapping accordingly.

### `gateway.token`
**Type**: String  
**Default**: None (optional)  

If set, all WebSocket connections must include token in authentication.  
Generate random: `openssl rand -hex 16`

## AI Settings

### `ai.provider`
**Type**: String  
**Options**:
- `claude` (Claude API) — **Recommended**
- `claude-web` (Browser-based)
- `local` (Local models, if available)

### `ai.model`
**Type**: String  
**Common models**:
- `claude-3-5-sonnet` (Default, fastest)
- `claude-3-opus` (Most capable)
- `claude-3-haiku` (Fastest)

### `ai.temperature`
**Type**: Float  
**Range**: `0.0 - 1.0`  
**Default**: `0.7`  

Lower = more deterministic, Higher = more creative

### `ai.max_tokens`
**Type**: Integer  
**Default**: `2048`  

Maximum tokens in response.

## Channel Settings

### Webchat (Built-in)
```json
"webchat": {
  "enabled": true,
  "path": "/webchat"
}
```

### Telegram
```json
"telegram": {
  "enabled": true,
  "token": "YOUR_BOT_TOKEN"
}
```

### Discord
```json
"discord": {
  "enabled": true,
  "token": "YOUR_BOT_TOKEN"
}
```

### Slack
```json
"slack": {
  "enabled": true,
  "bot_token": "xoxb-...",
  "signing_secret": "..."
}
```

### WhatsApp
```json
"whatsapp": {
  "enabled": true,
  "qr_code_url": "/whatsapp/qr"
}
```

See [CHANNELS.md](CHANNELS.md) for all channel options.

## Security Settings

### `security.allowlist`
**Type**: Array of strings  
**Default**: Empty (allow all)  

User IDs/numbers to allow. Leave empty to allow all.

```json
"allowlist": [
  "1234567890",
  "user@example.com"
]
```

### `security.blocklist`
**Type**: Array of strings  
**Default**: Empty  

User IDs to block explicitly.

```json
"blocklist": [
  "spam_bot_id"
]
```

## Logging

### `logging.level`
**Type**: String  
**Options**: `debug`, `info`, `warn`, `error`  
**Default**: `info`  

### `logging.format`
**Type**: String  
**Options**: `json`, `text`  
**Default**: `text`  

Logs are written to stdout (visible in Docker logs).

## Environment Variables

These override config file settings:

| Variable | Maps To | Example |
|----------|---------|---------|
| `CLAWDBOT_GATEWAY_TOKEN` | `gateway.token` | `abc123...` |
| `CLAUDE_AI_SESSION_KEY` | Claude API auth | `sk-ant-...` |
| `CLAUDE_WEB_SESSION_KEY` | Claude Web auth | Session UUID |
| `CLAUDE_WEB_COOKIE` | Claude Web cookie | Cookie string |

## Example Configurations

### Minimal (Webchat Only)
```json
{
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  },
  "channels": {
    "webchat": { "enabled": true }
  }
}
```

### Multi-Channel
```json
{
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  },
  "channels": {
    "webchat": { "enabled": true },
    "telegram": {
      "enabled": true,
      "token": "YOUR_TELEGRAM_TOKEN"
    },
    "discord": {
      "enabled": true,
      "token": "YOUR_DISCORD_TOKEN"
    },
    "slack": {
      "enabled": true,
      "bot_token": "xoxb-YOUR_TOKEN",
      "signing_secret": "YOUR_SIGNING_SECRET"
    }
  }
}
```

### Secure (with Authentication)
```json
{
  "gateway": {
    "bind": "127.0.0.1",
    "port": 18789,
    "token": "super-secret-token-here"
  },
  "ai": {
    "provider": "claude",
    "model": "claude-3-5-sonnet"
  },
  "channels": {
    "webchat": { "enabled": true }
  },
  "security": {
    "allowlist": ["admin_user_id"]
  }
}
```

## Reloading Configuration

Changes take effect on container restart:

```bash
docker restart openclaw
```

Or in UNRAID WebUI: Click container → Restart.

## Troubleshooting

### Configuration Not Applied
- Check file is at: `/mnt/user/appdata/openclaw/config/openclaw.json`
- Verify JSON syntax (use [jsonlint.com](https://jsonlint.com) to validate)
- Restart container after changes

### Invalid JSON
Error logs will show: `Invalid configuration file`  
Check for:
- Missing commas between properties
- Trailing commas (not allowed in JSON)
- Unquoted strings
- Unescaped quotes

Use JSON validator tool to check syntax.

## More Information

- Full OpenClaw docs: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- Channel setup: [CHANNELS.md](CHANNELS.md)
- UNRAID: [INSTALL.md](INSTALL.md)
