import requests
from helper import *


def get_list_of_current_github_issues():
    github_issue_params = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    headers = get_github_auth()
    url = f"https://api.github.com/repos/{github_issue_params['owner']}/{github_issue_params['repo']}/issues"
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.json())
    print("It Works!")
