#!/bin/sh
set -e

# Ensure required directories exist with proper permissions
mkdir -p /home/node/.openclaw/cron
mkdir -p /home/node/clawd/canvas
mkdir -p /home/node/clawd/agents
mkdir -p /home/node/clawd/devices

# Generate a random token if not provided
if [ -z "$OPENCLAW_GATEWAY_TOKEN" ]; then
    # Generate random hex token (32 chars)
    OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 16)
    export OPENCLAW_GATEWAY_TOKEN
    echo "Generated gateway token: $OPENCLAW_GATEWAY_TOKEN"
    echo "Set OPENCLAW_GATEWAY_TOKEN=$OPENCLAW_GATEWAY_TOKEN in your container environment to use the same token"
fi

# Start gateway with generated/provided token
exec node dist/index.js gateway --bind lan --port 18789 --allow-unconfigured --token "$OPENCLAW_GATEWAY_TOKEN"
