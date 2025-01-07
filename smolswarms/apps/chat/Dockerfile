# Base image slimmer than my wallet after GPU costs
FROM node:18-slim as builder

# Install deps faster than my Discord loading time
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set up our quantum workspace
WORKDIR /app

# Copy our blessed configuration
COPY config.yaml ./config.yaml

# Clone LibreChat at a specific version (no random commits fr fr)
RUN git clone --depth 1 --branch v0.6.9 https://github.com/danny-avila/LibreChat.git .

# Install deps with that optimization sauce
RUN npm ci --only=production

# Copy our simplified UI and configs
COPY simplified-ui/ ./client/src/
COPY swarm-plugin/ ./api/plugins/swarm/

# Build that frontend cleaner than my git history
RUN npm run build

# Final image slimmer than my attention span
FROM node:18-slim

WORKDIR /app

# Copy only what we need (no bloat fr fr)
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/api ./api
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/config.yaml ./config.yaml

# Environment that hits different
ENV NODE_ENV=production
ENV PORT=3000
ENV HOST=0.0.0.0

# Health check more reliable than my sleep schedule
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/api/health || exit 1

# Let it cook
EXPOSE 3000
CMD ["node", "api/server.js"] 