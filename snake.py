import requests


# Fetch the GitHub contribution graph SVG
response = requests.get(f"https://github.com/iamasik.svg")
with open("snake.svg", "wb") as f:
    f.write(response.content)
