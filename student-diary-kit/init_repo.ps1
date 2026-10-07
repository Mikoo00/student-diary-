# Creates local repo student-diary with two commits (stands in for practical work 3)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "student-diary")
if (-not (git config user.name) -or -not (git config user.email)) {
  Write-Host "Configure git first:"
  Write-Host '  git config --global user.name "Your Name"'
  Write-Host '  git config --global user.email "you@example.com"'
  exit 1
}
git init -b main
git add README.md .gitignore
git commit -m "Initial commit: add README and .gitignore"
git add diary.py
git commit -m "Add diary and schedule module"
git log --oneline
