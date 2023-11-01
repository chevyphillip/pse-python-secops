import requests
import json
from helper import get_github_auth


def parse_vuln_data():
    try:
        with open("vuln.json", "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(e)


def create_github_issue():
    github_repo = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    url = f"https://api.github.com/repos/{github_repo['owner']}/{github_repo['repo']}/issues"
    headers = get_github_auth()

    vuln_data = parse_vuln_data()

    if vuln_data["severity"] == "critical":
        title = f"Critical Vulnerability: {vuln_data['title']}"
        body = f"ID: {vuln_data['id']}\nTitle: {vuln_data['title']}\nPackage Name: {vuln_data['packageName']}\nVersion: {vuln_data['version']}\n"
    else:
        title = "No Security Issues Found"
        body = "No Security Issues Found"

    payload = {"title": title, "body": body}

    r = requests.post(url, headers=headers, json=payload)
    print(r.status_code)
    print(r.json())
    print("Issues Created!")
