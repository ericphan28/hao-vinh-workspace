# Git Repository Setup Guide

## 1. Initialize Git Repository

```bash
# Khởi tạo Git repository
git init

# Thêm remote repository (nếu có)
git remote add origin https://github.com/your-username/haovinh.git
```

## 2. Create .gitignore

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/settings.json
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Temporary files
tmp/
temp/
```

## 3. Initial Commit

```bash
# Add all files
git add .

# Initial commit
git commit -m "initial: setup programming course workspace

- Add project structure for 2 students
- Add Python project templates
- Add documentation and coding standards
- Add evaluation rubrics
- Add shared resources and utilities"

# Push to remote (if exists)
git push -u origin main
```

## 4. Create Student Branches

```bash
# Create and switch to thienhao branch
git checkout -b thienhao-main
git push -u origin thienhao-main

# Switch back to main
git checkout main

# Create and switch to thienvinh branch  
git checkout -b thienvinh-main
git push -u origin thienvinh-main

# Switch back to main
git checkout main
```

## 5. Branch Protection (GitHub/GitLab)

### GitHub Branch Protection Rules:
- Go to Settings > Branches
- Add rule for `main` branch:
  - Require pull request reviews before merging
  - Require status checks to pass
  - Include administrators
  - Allow force pushes: NO
  - Allow deletions: NO

### Recommended Settings:
- Require at least 1 reviewer
- Dismiss stale reviews when new commits are pushed
- Require review from code owners
- Restrict pushes that create files larger than 100MB
