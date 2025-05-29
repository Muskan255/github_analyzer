import requests
from collections import Counter

def fetch_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    return response.json()

def analyze_github_profile(username):
    user_data = fetch_user_data(username)
    if not user_data:
        print("User not found.")
        return

    repos = fetch_repos(username)
    languages = [repo['language'] for repo in repos if repo['language']]
    language_counts = Counter(languages)

    print(f"\nGitHub Profile Analysis for @{username}")
    print("-" * 40)
    print(f"Name        : {user_data.get('name')}")
    print(f"Public Repos: {user_data['public_repos']}")
    print(f"Followers   : {user_data['followers']}")
    print(f"Following   : {user_data['following']}")
    print(f"Bio         : {user_data.get('bio')}")
    print("\nTop Languages Used:")
    for lang, count in language_counts.most_common(3):
        print(f"  {lang} - {count} repo(s)")
    print("-" * 40)

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    analyze_github_profile(username)
