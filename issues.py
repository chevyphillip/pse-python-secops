import requests
import json
from helper import get_github_auth


def parse_vuln_data():
    try:
        with open("node_vulns.json", "r") as f1, open("docker_vulns.json", "r") as f2:
            node_data = json.load(f1)
            docker_data = json.load(f2)
            node_data["vulnerabilities"].extend(docker_data["vulnerabilities"])
            return node_data
    except Exception as e:
        print(f"Error: {e}")
        return None


def create_github_issue():
    github_repo = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    url = f"https://api.github.com/repos/{github_repo['owner']}/{github_repo['repo']}/issues"
    headers = get_github_auth()

    vuln_data = parse_vuln_data()

    # Handle dubplicated entires within the combined vuln_data. If thier is a duplicate, remove it. then create the issue.
    for unfilterd_vulns1 in vuln_data["vulnerabilities"]:
        for unfilterd_vulns2 in vuln_data["vulnerabilities"]:
            if unfilterd_vulns1["id"] == unfilterd_vulns2["id"]:
                vuln_data["vulnerabilities"].remove(unfilterd_vulns2)


    for vuln_data_payload in vuln_data["vulnerabilities"]:
        if vuln_data_payload["severity"] == "critical":
            title = f"Critical Vulnerability Found in {vuln_data_payload['title']}"
            body = f"❌ - A critical vulnerability was found in {vuln_data_payload['packageName']}\nVersion: {vuln_data_payload['version']}\nSnyk ID: {vuln_data_payload['id']}."
        else:
            title = "No Security Issues Found"
            body = "No Security Issues Found"

        payload = {"title": title, "body": body}

        r = requests.post(url, headers=headers, json=payload)
        if r.status_code == 201:
            print("Issue Created!")
        else:
            print(f"Failed to create issue. Status code: {r.status_code}")
