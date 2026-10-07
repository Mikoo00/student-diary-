#!/usr/bin/env bash
# Создаёт локальный репозиторий student-diary с двумя коммитами (имитация ПР №3)
set -e
cd "$(dirname "$0")/student-diary"
if [ -z "$(git config user.name)" ] || [ -z "$(git config user.email)" ]; then
  echo "Сначала настройте git:"
  echo '  git config --global user.name "Ваше Имя"'
  echo '  git config --global user.email "you@example.com"'
  exit 1
fi
git init -b main
git add README.md .gitignore
git commit -m "Initial commit: add README and .gitignore"
git add diary.py
git commit -m "Add diary and schedule module"
git log --oneline
