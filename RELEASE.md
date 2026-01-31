# Release Process

Quick guide for releasing new versions of the OpenClaw UNRAID template.

## Before Release

1. **Test locally:**
   ```bash
   python3 scripts/validate-template.py
   docker-compose up --build
   docker logs openclaw --tail 20
   ```

2. **Commit all changes:**
   ```bash
   git add .
   git commit -m "Fix: description of changes"
   git push origin main
   ```

## Creating a Release

### 1. Create and push tag

```bash
git tag -a v1.0.1 -m "Release v1.0.1 - Brief description

- Fix: specific fix
- Add: new feature
- Update: improvement"

git push origin v1.0.1
```

**Note:** Pushing the tag automatically triggers GitHub Actions to:
- Validate the template
- Build Docker image
- Push to Docker Hub (`relains/openclaw:v1.0.1` and `relains/openclaw:latest`)

### 2. Monitor GitHub Actions

Check build status: https://github.com/relains/openclaw-unraid-template/actions

Wait for:
- ✅ Validate workflow
- ✅ Build and Push workflow

### 3. Create GitHub Release

After successful build:

1. Go to https://github.com/relains/openclaw-unraid-template/releases
2. Click on tag `v1.0.1`
3. Click **"Create release from tag"**
4. Fill in:
   - **Title:** `v1.0.1`
   - **Description:**
     ```
     Release v1.0.1 - Brief description

     ## What's Changed
     - Fix: specific fix details
     - Add: new feature details
     - Update: improvement details

     ## Installation
     See [INSTALL.md](docs/INSTALL.md) for setup instructions.
     ```
5. Click **"Publish release"**

## Version Numbering

Use [Semantic Versioning](https://semver.org/):

- **v1.0.0** - Major release (breaking changes)
- **v1.1.0** - Minor release (new features, backwards compatible)
- **v1.0.1** - Patch release (bug fixes)

## Checklist

Before releasing:

- [ ] All tests pass locally
- [ ] Template validates: `python3 scripts/validate-template.py`
- [ ] Docker image builds: `docker-compose build`
- [ ] Container starts: `docker-compose up`
- [ ] Documentation updated
- [ ] CHANGELOG.md updated (if exists)
- [ ] Commit message follows convention

After releasing:

- [ ] GitHub Actions completed successfully
- [ ] Docker image available on Docker Hub
- [ ] GitHub Release created with proper description
- [ ] Test installation in UNRAID (if possible)

## Quick Commands Reference

```bash
# Validate
python3 scripts/validate-template.py

# Build locally
docker-compose up --build

# Tag and release
git tag -a v1.0.1 -m "Release message"
git push origin v1.0.1

# Delete tag
git tag -d v1.0.1
git push origin --delete v1.0.1
```
