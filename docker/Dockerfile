FROM node:22-bookworm

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    python3 \
    && rm -rf /var/lib/apt/lists/*

# Install pnpm
RUN npm install -g pnpm@latest

# Clone openclaw repository (formerly moltbot and/or clawdbot)
RUN git clone --depth 1 --branch main https://github.com/openclaw/openclaw.git . && \
    rm -rf .git

# Install dependencies
RUN pnpm install --frozen-lockfile

# Build UI assets
RUN pnpm ui:build

# Build the application
RUN pnpm build

# Create non-root user 'node' with uid 1000 (already exists in base image)
# Ensure proper permissions and create all required directories
RUN mkdir -p /home/node/.openclaw/cron \
             /home/node/clawd/canvas \
             /home/node/clawd/agents \
             /home/node/clawd/devices && \
    chown -R node:node /home/node

# Copy entrypoint script
COPY docker/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Switch to node user
USER node

# Expose ports
EXPOSE 18789 18790

# Set environment defaults
ENV HOME=/home/node \
    TERM=xterm-256color \
    NODE_ENV=production

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD node -e "require('http').get('http://localhost:18789', (r) => {if (r.statusCode !== 200) throw new Error(r.statusCode)})"

# Start via entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]
