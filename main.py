import requests
import json
import os


# TODO: Parse vuln.json from the inital Snyk scan


def get_list_of_current_github_issues():
    github_token = os.environ.get("GITHUB_TOKEN")
    github_issue_params = {"owner": "chevyphillip", "repo": "nodejs-goof"}
    headers = {
        "Accept": "Accept: application/vnd.github+json",
        "Authorzation": "Bearer " + github_token,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    url = f"https://api.github.com/repos/{github_issue_params['owner']}/{github_issue_params['repo']}/issues"
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(r.json())


def vuln_data_parser():
    with open("vuln.json") as json_file:
        data = json.load(json_file)
        for p in data["vulnerabilities"]:
            print("")
            print("ID: " + p["id"])
            print("Title: " + p["title"])
            print("Package: " + p["packageName"])
            print("Version: " + p["version"])
            print("")


# TODO: If Critical security issues are detected as a result of the Snyk test create a GitHub Issue that contains a list of the security issues detected. The issue id, title, package and version should be included for each entry
# TODO: If no Critical security issues are detected, the GitHub Issue should still be created, but display "No Security Issues Found"
# TODO: Generate github issues for each of the security issues detected
# TODO: Check for errors and handle them gracefully
# TODO: Add logging to slack - nice to have


def main():
    # vuln_data_parser()
    get_list_of_current_github_issues()


if __name__ == "__main__":
    main()
