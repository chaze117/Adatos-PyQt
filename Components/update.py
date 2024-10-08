import git.repo
import requests
import zipfile
import os
import shutil
import git
# GitHub repository details
repo_owner = 'chaze117'  # Replace with the repository owner name
repo_name = 'Adatos-PyQt'    # Replace with the repository name
file_path = 'version.txt'  # Path to the version file in the repo

# Raw file URL to fetch the version file
url = f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{file_path}'
def checkForUpdate():
    response = requests.get(url)
    response.raise_for_status()  # Raise an error if the request fails
    latest_version = response.text.strip()  # Get the content and remove whitespace
    local_version = None
    with open(file_path, 'r') as file:
        local_version = file.readline().strip()

    if latest_version != local_version:
        try:
            repo =  git.Repo(os.getcwd())
            origin = repo.remotes.origin
            origin.pull()
            print(f"Successfully pulled from {origin.name} into.")
        
        except git.exc.GitCommandError as e:
            print(f"Failed to pull repository: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
checkForUpdate()
