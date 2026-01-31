# Security Policy

## Reporting Security Issues

If you discover a security vulnerability in this project, please submit na issue.

**Please include:**
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

## Security Considerations

### General

- **Never commit credentials** (tokens, API keys, passwords)
- Use environment variables for sensitive data
- Rotate credentials regularly
- Keep Docker images updated

### For UNRAID Users

1. **Access Control**
   - Set `gateway.token` for authentication
   - Use firewall rules to restrict access
   - Consider running behind reverse proxy with TLS

2. **Data Security**
   - Backup `/mnt/user/appdata/openclaw/config/` regularly
   - Backup contains sensitive credentials
   - Store backups securely
   - Encrypt backups for off-site storage

3. **Network**
   - Don't expose ports to untrusted networks
   - Use VPN for remote access
   - Enable HTTPS via reverse proxy (nginx, traefik)
   - Monitor logs for suspicious activity

4. **Updates**
   - Keep Docker image updated
   - Watch for security announcements
   - Test updates on non-production first

### For Channel Operators

1. **WhatsApp**: Phone must be online initially to establish connection
2. **Telegram**: Bot token is sensitive — never share publicly
3. **Discord**: Bot token grants full bot permissions — treat as password
4. **Slack**: Signing secret + bot token = sensitive
5. **All channels**: Rotate credentials if suspected compromise

## Dependency Security

This project depends on:
- **OpenClaw**: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
  - Check their security policy
  - Monitor their advisories

Dependencies are scanned during CI/CD with Trivy. Reports available in GitHub Security tab.

## Disclosure Policy

- We follow responsible disclosure practices
- We aim to patch issues within 30 days
- We'll credit reporters (unless they prefer anonymity)
- We maintain a public advisory list

## Scope

This policy covers:
- Docker image vulnerabilities
- UNRAID template security
- Documentation security guidance

Out of scope:
- OpenClaw core vulnerabilities (report to OpenClaw project)
- Docker/Kubernetes security (report to respective projects)

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-01-29 | Initial security policy |

---

Thank you for helping keep OpenClaw secure! 🔒
