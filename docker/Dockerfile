# Use official openclaw image directly
FROM ghcr.io/openclaw/openclaw:latest

# Copy custom entrypoint for UNRAID-specific setup
COPY docker/entrypoint.sh /entrypoint-unraid.sh

# Override entrypoint to use our custom script
ENTRYPOINT ["/entrypoint-unraid.sh"]
