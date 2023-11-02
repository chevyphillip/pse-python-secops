from helper import *
from issues import create_github_issue, delete_duplicate_issues_based_on_snyk_id


def main():
    delete_duplicate_issues_based_on_snyk_id()
    create_github_issue()


if __name__ == "__main__":
    main()
