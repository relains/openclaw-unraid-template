# Use official openclaw image directly
FROM ghcr.io/openclaw/openclaw:latest

# Create entrypoint script with proper permissions handling
USER root
RUN printf '#!/bin/sh\nchown -R node:node /home/node/.openclaw 2>/dev/null || true\nchown -R node:node /home/node/clawd 2>/dev/null || true\nchmod -R 755 /home/node/.openclaw 2>/dev/null || true\nchmod -R 755 /home/node/clawd 2>/dev/null || true\nmkdir -p /home/node/.openclaw/cron /home/node/clawd/canvas /home/node/clawd/agents /home/node/clawd/devices 2>/dev/null || true\nchown -R node:node /home/node/.openclaw /home/node/clawd 2>/dev/null || true\nchmod -R 755 /home/node/.openclaw /home/node/clawd 2>/dev/null || true\nif [ -z "$OPENCLAW_GATEWAY_TOKEN" ]; then\n  OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 16)\n  export OPENCLAW_GATEWAY_TOKEN\n  echo "Generated gateway token: $OPENCLAW_GATEWAY_TOKEN"\nfi\nexec /bin/sh -c "node dist/index.js gateway --bind lan --port 18789 --allow-unconfigured --token \"$OPENCLAW_GATEWAY_TOKEN\""\n' > /entrypoint-unraid.sh && chmod +x /entrypoint-unraid.sh

# Override entrypoint to use our custom script
ENTRYPOINT ["/entrypoint-unraid.sh"]
