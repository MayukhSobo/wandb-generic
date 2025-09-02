# How to Create Releases and Publish to PyPI

## Automatic Publishing Workflow
When you create a GitHub release, it automatically publishes to PyPI! 

## Creating a Release

### GitHub Web Interface (Recommended)
1. Go to your GitHub repo
2. Click "Releases" → "Create a new release"  
3. Tag version: `v1.0.0` (must match version in pyproject.toml)
4. Release title: `Release v1.0.0`
5. Description: Copy from CHANGELOG.md or write release notes
6. Click "Publish release"

## What Happens Automatically
1. GitHub Actions detects the new release
2. Runs tests on Python 3.8-3.12
3. Builds the package (wheel + source distribution)
4. Publishes to PyPI automatically  
5. People can install with: `pip install wandb-generic`

## For Future Versions
1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Update version in `src/wandb_generic/__init__.py` 
4. Commit and push changes
5. Create new release with new version tag
6. Automatic publishing happens! 