# Messaging Channels Setup Guide

Instructions for connecting OpenClaw to various messaging platforms.

## Overview

OpenClaw supports these messaging channels:

| Channel | Type | Difficulty | Setup Time |
|---------|------|------------|-----------|
| **WebChat** | Web-based | ⭐ Easy | 1 min |
| **Telegram** | Bot | ⭐ Easy | 5 min |
| **Discord** | Bot | ⭐ Easy | 5 min |
| **Slack** | App | ⭐⭐ Medium | 10 min |
| **WhatsApp** | QR Pairing | ⭐⭐ Medium | 5 min |
| **Google Chat** | Bot | ⭐⭐ Medium | 10 min |
| **Signal** | Registration | ⭐⭐ Medium | 5 min |
| **iMessage** | macOS App | ⭐⭐⭐ Hard | 15 min |
| **Teams** | Bot | ⭐⭐ Medium | 10 min |
| **Matrix** | Homeserver | ⭐⭐⭐ Hard | 15 min |
| **Zalo** | Phone Pairing | ⭐⭐ Medium | 5 min |

## WebChat (Built-in)

The easiest way to interact with OpenClaw.

### Setup

1. Open `http://your-unraid-ip:18789/`
2. WebChat interface loads automatically
3. You can start chatting immediately

### Configuration

```json
{
  "channels": {
    "webchat": {
      "enabled": true,
      "path": "/webchat"
    }
  }
}
```

### Features
- No setup required
- Works in any browser
- Text chat interface
- Real-time WebSocket connection

---

## Telegram

Connect OpenClaw as a Telegram bot.

### Step 1: Create Bot

1. Open Telegram and search for **@BotFather**
2. Click **Start**
3. Send `/newbot`
4. Choose a name (e.g., "My OpenClaw")
5. Choose a username (must be unique, must end with "bot")
6. Copy the **API Token** provided

**Token format**: `1234567890:ABCDEFGHIJKLMNOPQRSTuvwxyz`

### Step 2: Configure OpenClaw

Edit `/mnt/user/appdata/openclaw/config/openclaw.json`:

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "YOUR_API_TOKEN_HERE"
    }
  }
}
```

Replace `YOUR_API_TOKEN_HERE` with your bot token.

### Step 3: Restart Container

In UNRAID WebUI, restart openclaw container.

### Step 4: Test

Find your bot in Telegram by username and send a message.

### Advanced Options

```json
{
  "telegram": {
    "enabled": true,
    "token": "...",
    "polling": false,
    "webhook_url": "https://your-domain.com/telegram"
  }
}
```

---

## Discord

Connect OpenClaw as a Discord bot.

### Step 1: Create Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **New Application**
3. Name it (e.g., "OpenClaw")
4. Go to **Bot** → **Add Bot**
5. Under **TOKEN**, click **Copy**

**Token format**: `MTk4NjIyNDgzNzQ0MTI4OTYx.A.ZfqX...`

### Step 2: Set Permissions

In Developer Portal:
1. Go to **OAuth2** → **URL Generator**
2. Select **Scopes**: `bot`
3. Select **Permissions**:
   - ✅ Send Messages
   - ✅ Read Messages/View Channels
   - ✅ Read Message History
4. Copy the generated URL

### Step 3: Invite Bot to Server

1. Paste the URL in browser
2. Select your Discord server
3. Click **Authorize**

### Step 4: Configure OpenClaw

Edit `/mnt/user/appdata/openclaw/config/openclaw.json`:

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN_HERE"
    }
  }
}
```

### Step 5: Restart & Test

1. Restart openclaw container
2. Send a message to your bot in Discord
3. It should respond using AI

### Advanced Options

```json
{
  "discord": {
    "enabled": true,
    "token": "...",
    "prefix": "!",
    "dm_only": false
  }
}
```

---

## Slack

Connect OpenClaw to a Slack workspace.

### Step 1: Create Slack App

1. Go to [Slack API](https://api.slack.com/apps)
2. Click **Create New App** → **From scratch**
3. App Name: "OpenClaw"
4. Choose your workspace
5. Click **Create App**

### Step 2: Configure Bot Token

1. Go to **OAuth & Permissions**
2. Under **Scopes** → **Bot Token Scopes**, add:
   - `app_mentions:read`
   - `chat:write`
   - `channels:history`
   - `groups:history`
   - `im:history`
   - `mpim:history`
3. Scroll up → **Install to Workspace** (if not already installed)
4. Copy **Bot User OAuth Token** (`xoxb-...`)

### Step 3: Get Signing Secret

1. Go to **Basic Information**
2. Copy **Signing Secret**

### Step 4: Configure OpenClaw

Edit `/mnt/user/appdata/openclaw/config/openclaw.json`:

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "bot_token": "xoxb-YOUR_TOKEN_HERE",
      "signing_secret": "YOUR_SIGNING_SECRET_HERE"
    }
  }
}
```

### Step 5: Setup Event Subscriptions

For the bot to receive messages, configure webhooks:

1. In Slack App settings, go to **Event Subscriptions**
2. Turn on **Enable Events**
3. For **Request URL**, use:
   ```
   https://your-unraid-ip:18789/slack/events
   ```
   (Replace `your-unraid-ip` with actual IP)
4. Slack will verify the endpoint
5. Under **Subscribe to bot events**, add:
   - `app_mention`
   - `message.im`

### Step 6: Restart & Test

1. Restart openclaw container
2. In Slack, mention your bot: `@OpenClaw hello`
3. Bot should respond

---

## WhatsApp

Connect via QR code pairing.

### Step 1: Access WhatsApp Setup

1. Open `http://your-unraid-ip:18789/`
2. Navigate to **Channels** → **WhatsApp**
3. A QR code will appear

### Step 2: Scan QR Code

1. Open WhatsApp on your phone
2. Go to **Settings** → **Linked Devices**
3. Tap **Link a Device**
4. Scan the QR code from OpenClaw WebUI

### Step 3: Confirm

1. WhatsApp will ask for confirmation
2. Confirm linking
3. OpenClaw is now connected to WhatsApp

### Important Notes

- Your phone must stay online initially to establish connection
- After pairing, the "linked device" can work independently
- Messages will appear as coming from a "linked device"
- Supports individual and group chats

### Configuration

```json
{
  "channels": {
    "whatsapp": {
      "enabled": true
    }
  }
}
```

---

## Other Channels

### Google Chat

1. Create a service account in [Google Cloud Console](https://console.cloud.google.com)
2. Download JSON credentials
3. Configure in OpenClaw:

```json
{
  "google_chat": {
    "enabled": true,
    "webhook_url": "https://chat.googleapis.com/v1/spaces/...",
    "credentials_file": "path/to/credentials.json"
  }
}
```

### Signal

1. Register phone number in Signal app
2. Configure in OpenClaw:

```json
{
  "signal": {
    "enabled": true,
    "phone_number": "+1234567890"
  }
}
```

### iMessage (macOS only)

1. Set up macOS companion app
2. Configure in OpenClaw:

```json
{
  "imessage": {
    "enabled": true,
    "macos_app": "openclaw-macos"
  }
}
```

### Teams

1. Create bot in Azure & Microsoft Teams
2. Get bot ID and password
3. Configure:

```json
{
  "teams": {
    "enabled": true,
    "bot_id": "...",
    "bot_password": "..."
  }
}
```

### Matrix

1. Specify homeserver URL
2. Create user/get access token
3. Configure:

```json
{
  "matrix": {
    "enabled": true,
    "homeserver_url": "https://matrix.org",
    "user_id": "@bot:matrix.org",
    "access_token": "..."
  }
}
```

### Zalo (Vietnam)

1. Register Zalo Official Account
2. Get access token
3. Configure:

```json
{
  "zalo": {
    "enabled": true,
    "access_token": "..."
  }
}
```

---

## Testing Channels

### Via WebChat

1. Test locally via `http://your-unraid-ip:18789/`
2. Send a message
3. Verify response

### Via Logs

Monitor channel activity in logs:

```bash
docker logs -f openclaw | grep -i channel
```

### Common Issues

**"Channel disabled"**
- Ensure `enabled: true` in config
- Restart container

**"Auth failed"**
- Verify token/credentials are correct
- Check for special characters or copy-paste errors
- Generate new credentials if needed

**"No response"**
- Verify AI is configured with working session key
- Check firewall/network connectivity
- Review logs for errors

---

## Best Practices

1. **Start with one channel**: Get WebChat working first, then add others
2. **Test each channel**: Send messages via each platform to verify
3. **Back up credentials**: Save your tokens somewhere safe (outside OpenClaw)
4. **Rotate tokens**: Change tokens periodically if compromised
5. **Limit access**: Use allowlist/blocklist for security
6. **Monitor logs**: Watch for authentication errors

---

## Support

- Channel documentation: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- Troubleshoot: See logs in Docker section of UNRAID
- Issues: [github.com/openclaw/openclaw/issues](https://github.com/openclaw/openclaw/issues)
