import json


def vuln_data_parser():
    with open("vuln.json") as json_file:
        data = json.load(json_file)
        for p in data["vulnerabilities"]:
            if data["vulnerabilities"][0]["severity"] == "critical":
                print("")
                print("Critical security issues detected!")
                print("ID: " + p["id"])
                print("Title: " + p["title"])
                print("Package: " + p["packageName"])
                print("Version: " + p["version"])
                print("")
            else:
                print("No Security Issues Found")
