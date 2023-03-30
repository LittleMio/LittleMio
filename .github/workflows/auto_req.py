name: auto Requests

on:
  schedule:
    # Run every 10 minutes
    - cron: '*/10 * * * *'

jobs:
  run-python:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Run python script
        run: |
          cd .github
          python auto_req.py
