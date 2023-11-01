import json


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
