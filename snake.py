# snake.py

import requests

# Define your GitHub username
username = iamasik

# Fetch the GitHub contribution graph SVG
response = requests.get(f"https://github.com/{username}.svg")
with open("snake.svg", "wb") as f:
    f.write(response.content)
