# Use official openclaw image directly
FROM ghcr.io/openclaw/openclaw:latest

# Create entrypoint script with proper shebang
USER root
RUN printf '#!/bin/sh\nmkdir -p /home/node/.openclaw/cron\nmkdir -p /home/node/clawd/canvas\nmkdir -p /home/node/clawd/agents\nmkdir -p /home/node/clawd/devices\nif [ -z "$OPENCLAW_GATEWAY_TOKEN" ]; then\n  OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 16)\n  export OPENCLAW_GATEWAY_TOKEN\n  echo "Generated gateway token: $OPENCLAW_GATEWAY_TOKEN"\nfi\nexec node dist/index.js gateway --bind lan --port 18789 --allow-unconfigured --token "$OPENCLAW_GATEWAY_TOKEN"\n' > /entrypoint-unraid.sh && chmod +x /entrypoint-unraid.sh
USER node

# Override entrypoint to use our custom script
ENTRYPOINT ["/entrypoint-unraid.sh"]
