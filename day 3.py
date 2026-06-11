import requests

while True:
    username = input("\nEnter GitHub username (or type 'exit'): ")

    if username.lower() == "exit":
        print("Program stopped.")
        break

    url = f"https://api.github.com/users/{username}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    data = response.json()

    print("\n" + "="*40)

    if response.status_code == 200:
        print("        GITHUB USER DASHBOARD")
        print("="*40)
        print(f"Name        : {data.get('name')}")
        print(f"Username    : {data.get('login')}")
        print(f"Public Repos: {data.get('public_repos')}")
        print(f"Followers   : {data.get('followers')}")
        print(f"Following   : {data.get('following')}")
        print(f"Location    : {data.get('location')}")
        print(f"Profile URL : {data.get('html_url')}")
        print("="*40)
    else:
        print("ERROR: User not found or request failed")

    print("="*40)