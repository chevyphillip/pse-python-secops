import re
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

    for vuln_data_payload in vuln_data["vulnerabilities"]:
        if vuln_data_payload["severity"] == "critical":
            title = f"Critical Vulnerability Found in {vuln_data_payload['title']}"
            body = f"[X] - A critical vulnerability was found in {vuln_data_payload['packageName']}\nVersion: {vuln_data_payload['version']}\nSnyk ID: {vuln_data_payload['id']}."
        elif vuln_data_payload["severity"] != "critical":
            title = "No Security Issues Found"
            body = "No Security Issues Found"
        else:
            return None

        payload = {"title": title, "body": body, "labels": [vuln_data_payload["id"]]}

        r = requests.post(url, headers=headers, json=payload)
        if r.status_code == 201:
            print("Issue Created!")
        else:
            print(f"Failed to create issue. Status code: {r.status_code}")


def delete_duplicate_issues_based_on_snyk_id():
    github_repo = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    url = f"https://api.github.com/repos/{github_repo['owner']}/{github_repo['repo']}/issues"
    headers = get_github_auth()

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        issues = r.json()
        snyk_ids = []
        for issue in issues:
            if issue["title"].startswith("Critical Vulnerability Found in"):
                snyk_id = re.search(r"Snyk ID: ([a-z0-9]+)", issue["body"])
                if snyk_id:
                    snyk_ids.append(snyk_id.group(1))
                else:
                    print("No Snyk ID found in issue body.")
        snyk_ids = list(set(snyk_ids))
        for snyk_id in snyk_ids:
            r = requests.get(
                f"https://api.github.com/repos/{github_repo['owner']}/{github_repo['repo']}/issues?labels={snyk_id}",
                headers=headers,
            )
            if r.status_code == 200:
                issues = r.json()
                for issue in issues:
                    r = requests.delete
