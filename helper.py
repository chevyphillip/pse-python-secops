import os


# Get the Github auth token from the environment variables that is exposed to the Github Action. Expires when a job is completed. Or within 24 hours.
def get_github_auth():
    github_token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    return headers
