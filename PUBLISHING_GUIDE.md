# Publishing Guide

## 1. Create PyPI Accounts
- Main PyPI: https://pypi.org/account/register/
- Test PyPI: https://test.pypi.org/account/register/ (for testing)

## 2. Install required tools
pip install twine

## 3. Upload to Test PyPI first (recommended)
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

## 4. Test install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ wandb-generic

## 5. Upload to production PyPI
twine upload dist/*

## 6. Test final install
pip install wandb-generic

