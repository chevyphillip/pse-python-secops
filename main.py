from helper import *
from issues import get_list_of_current_github_issues
from vuln_data_parser import vuln_data_parser

# TODO: If Critical security issues are detected as a result of the Snyk test create a GitHub Issue that contains a list of the security issues detected. The issue id, title, package and version should be included for each entry
# TODO: If no Critical security issues are detected, the GitHub Issue should still be created, but display "No Security Issues Found"
# TODO: Generate github issues for each of the security issues detected
# TODO: Check for errors and handle them gracefully
# TODO: Add logging to slack - nice to have


def main():
    vuln_data_parser()
    get_list_of_current_github_issues()


if __name__ == "__main__":
    main()
