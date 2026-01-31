# Use official openclaw image directly
FROM ghcr.io/openclaw/openclaw:latest

# Copy custom entrypoint for UNRAID-specific setup
USER root
COPY docker/entrypoint.sh /entrypoint-unraid.sh
RUN chmod +x /entrypoint-unraid.sh
USER node

# Override entrypoint to use our custom script
ENTRYPOINT ["/entrypoint-unraid.sh"]
