# Agile Assignment No. 1 — Git and GitHub

**Student Name:** Rohan Shelar  
**Subject:** Agile  
**Academic Year:** 2026–27  
**Repository:** https://github.com/rohanshelar991/dev

## Aim
To implement source-code management using Git and GitHub, including repository creation, commits, branching, merging, and collaboration.

## Tools Used
- macOS Terminal
- Git
- GitHub

## Practical Implementation
1. Initialized a local Git repository.
2. Created README.md and committed the initial version.
3. Connected the local repository to GitHub.
4. Pushed the main branch to GitHub.
5. Created the feature-login branch.
6. Added login.txt and committed the login feature.
7. Pushed the feature branch to GitHub.
8. Merged feature-login into main.
9. Pushed the merged changes to GitHub.

## Git Commands Used
```bash
git init -b main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/rohanshelar991/dev.git
git push -u origin main
git switch -c feature-login
git add .
git commit -m "Add login feature"
git push -u origin feature-login
git switch main
git merge feature-login
git push origin main
git branch
git log --oneline
cd ~/Desktop/agile-assignment

git switch main

cat > README.md <<'EOF'
# Agile Assignment 1 — Git and GitHub

**Student Name:** Rohan Shelar  
**Subject:** Agile  
**Repository:** https://github.com/rohanshelar991/dev

## Aim
To demonstrate source-code management using Git and GitHub.

## Objectives
- Create a local Git repository.
- Track and commit changes.
- Create and push a feature branch.
- Merge the feature branch into main.
- Maintain project files on GitHub.

## Practical Steps
1. Initialized the Git repository.
2. Created and committed README.md.
3. Connected the repository to GitHub.
4. Pushed the main branch.
5. Created the feature-login branch.
6. Added and committed login.txt.
7. Pushed the feature branch.
8. Merged feature-login into main.
9. Pushed the merged changes to GitHub.

## Files
- README.md — Assignment documentation.
- login.txt — Sample login feature.
- docs/GIT_WORKFLOW.md — Git workflow explanation.

## Result
Successfully demonstrated Git initialization, version control, commits, branching, pushing, and merging.
