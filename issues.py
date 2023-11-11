from hmac import new
import requests
import json
from helper import get_github_auth


# Save the vulnerabilities from Snyk to a json file one for Node and one for Docker. Rutun errors if there are any.
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


# Create a Github issue if there are any critical vulnerabilities.
def create_github_issue():

    github_repo = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    url = f"https://api.github.com/repos/{github_repo['owner']}/{github_repo['repo']}/issues"

    # Get the Github auth token from the helper function
    headers = get_github_auth()


    # store the vulnerabilities in a variable called vuln_data
    vuln_data = parse_vuln_data()

    # Remove duplicates from vuln_data by converting it to a dictionary and back to a list. Dictionary keys are unique.
    vuln_data["vulnerabilities"] = list({vuln['id']:vuln for vuln in vuln_data["vulnerabilities"]}.values())

    # After duplicates are removed, check if there are any critical vulnerabilities and create an issue if there are. If not, create an issue saying no security issues were found.
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
