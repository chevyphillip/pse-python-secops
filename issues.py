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
        return None


def create_github_issue():
    github_repo = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    url = f"https://api.github.com/repos/{github_repo['owner']}/{github_repo['repo']}/issues"
    headers = get_github_auth()

    vuln_data = parse_vuln_data()

    for vuln_data_payload in vuln_data:
        if vuln_data_payload["severity"] == "critical":
            title = f"Critical Vulnerability Found in {vuln_data_payload['title']}"
            body = f"""
            [X] - A critical vulnerability was found in {vuln_data_payload['packageName']}\nVersion: {vuln_data_payload['version']}\nSnyk ID: {vuln_data_payload['id']}.
            """
        else:
            title = "No Security Issues Found."
            body = "No Security Issues Found."

        payload = {"title": title, "body": body}

        r = requests.post(url, headers=headers, json=payload)
        print(r.status_code)
        print(r.json())
        print("Issues Created!")
