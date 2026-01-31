#!/bin/bash
# Helper script to manage OpenClaw container

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
COMMAND=${1:-help}
CONTAINER_NAME=${CONTAINER_NAME:-openclaw}

# Helper functions
print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Commands
start() {
    print_info "Starting OpenClaw container..."
    docker-compose up -d
    print_success "Container started"
}

stop() {
    print_info "Stopping OpenClaw container..."
    docker-compose down
    print_success "Container stopped"
}

restart() {
    print_info "Restarting OpenClaw container..."
    docker-compose restart
    print_success "Container restarted"
}

logs() {
    print_info "Following container logs (Ctrl+C to exit)..."
    docker-compose logs -f openclaw
}

logs_last() {
    LINES=${2:-50}
    docker-compose logs openclaw | tail -n $LINES
}

status() {
    print_info "Container status:"
    docker-compose ps
}

build() {
    print_info "Building Docker image..."
    docker-compose build
    print_success "Build completed"
}

rebuild() {
    build
    start
}

shell() {
    print_info "Opening shell in container..."
    docker exec -it $CONTAINER_NAME sh
}

config() {
    print_info "OpenClaw configuration directory:"
    echo "./appdata/config"
    
    if [ -d "./appdata/config" ]; then
        print_info "Configuration files:"
        ls -la "./appdata/config" || true
    else
        print_error "Config directory not found. Start container first."
    fi
}

validate() {
    print_info "Validating template and configuration..."
    
    if command -v python3 &> /dev/null; then
        python3 scripts/validate-template.py
    else
        print_error "Python3 not found"
        exit 1
    fi
}

clean() {
    print_info "Cleaning up..."
    docker-compose down -v
    rm -rf appdata/
    print_success "Cleanup completed"
}

help() {
    cat << 'EOF'
OpenClaw Container Management

Usage: ./manage.sh [COMMAND]

Commands:
  start                Start container in background
  stop                 Stop container
  restart              Restart container
  status               Show container status
  logs                 Follow container logs
  logs [N]             Show last N lines of logs
  build                Build Docker image
  rebuild              Build and start container
  shell                Open shell in container
  config               Show config directory
  validate             Validate template and configuration
  clean                Stop and remove all data
  help                 Show this help message

Examples:
  ./manage.sh start
  ./manage.sh logs
  ./manage.sh logs 100
  ./manage.sh shell
  ./manage.sh validate

Environment Variables:
  CONTAINER_NAME       Container name (default: openclaw)

EOF
}

# Main
case $COMMAND in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    logs)
        logs_last $2
        ;;
    logs-follow)
        logs
        ;;
    status)
        status
        ;;
    build)
        build
        ;;
    rebuild)
        rebuild
        ;;
    shell)
        shell
        ;;
    config)
        config
        ;;
    validate)
        validate
        ;;
    clean)
        clean
        ;;
    help)
        help
        ;;
    *)
        print_error "Unknown command: $COMMAND"
        help
        exit 1
        ;;
esac
