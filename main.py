import requests
import json


# TODO: Parse vuln.json from the inital Snyk scan
def vuln_data_parser():
    with open("vuln.json") as json_file:
        data = json.load(json_file)
        for p in data["vulnerabilities"]:
            print("")
            print("Title: " + p["title"])
            print("Package: " + p["packageName"])
            print("Severity: " + p["severity"])
            print("Version: " + p["version"])
            print("ID: " + p["id"])
            print("")


# TODO: If Critical security issues are detected as a result of the Snyk test create a GitHub Issue that contains a list of the security issues detected. The issue id, title, package and version should be included for each entry
# TODO: If no Critical security issues are detected, the GitHub Issue should still be created, but display "No Security Issues Found"
# TODO: Generate github issues for each of the security issues detected
# TODO: Check for errors and handle them gracefully
# TODO: Add logging to slack - nice to have


def main():
    vuln_data_parser()


if __name__ == "__main__":
    main()
