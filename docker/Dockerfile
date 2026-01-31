# Use official openclaw image directly
FROM ghcr.io/openclaw/openclaw:latest

# Create entrypoint script with proper permissions handling
USER root
RUN printf '#!/bin/sh\nif [ ! -d "/home/node/.openclaw/cron" ]; then\n  mkdir -p /home/node/.openclaw/cron /home/node/clawd/canvas /home/node/clawd/agents /home/node/clawd/devices\n  chown -R node:node /home/node/.openclaw /home/node/clawd\n  chmod -R 755 /home/node/.openclaw /home/node/clawd\nfi\nif [ -z "$OPENCLAW_GATEWAY_TOKEN" ]; then\n  OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 16)\n  export OPENCLAW_GATEWAY_TOKEN\n  echo "Generated gateway token: $OPENCLAW_GATEWAY_TOKEN"\nfi\nexec /bin/sh -c "node dist/index.js gateway --bind lan --port 18789 --allow-unconfigured --token \\"$OPENCLAW_GATEWAY_TOKEN\\""\n' > /entrypoint-unraid.sh && chmod +x /entrypoint-unraid.sh

# Override entrypoint to use our custom script
ENTRYPOINT ["/entrypoint-unraid.sh"]
