import requests

# GitHub repository details
repo_owner = 'OWNER_NAME'  # Replace with the repository owner name
repo_name = 'REPO_NAME'    # Replace with the repository name
file_path = 'version.txt'  # Path to the version file in the repo

# Raw file URL to fetch the version file
url = f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{file_path}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    latest_version = response.text.strip()  # Get the content and remove whitespace

    print(f'Latest version from GitHub: {latest_version}')
except requests.RequestException as e:
    print(f"Error fetching the version file: {e}")
