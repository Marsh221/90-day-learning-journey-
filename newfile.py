import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)import requests

response = requests.get("https://api.github.com")

data = response.json()

print("Current GitHub API info:")
print(data)