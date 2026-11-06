name: Mise à jour du cache

on:
  schedule:
    - cron: "0 */6 * * *"
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install requests
      - run: python scripts/update_cache.py
      - name: Enregistrer le fichier
        run: |
          git config user.name "cache-bot"
          git config user.email "cache-bot@users.noreply.github.com"
          git add cache.db
          git commit -m "Mise à jour du cache" || echo "Rien à enregistrer"
          git push
