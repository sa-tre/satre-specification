import os
import sys
from datetime import datetime, timedelta
from github import Github

def main():
    token = os.environ["GITHUB_TOKEN"]
    repo_name = os.environ["GITHUB_REPOSITORY"]

    g = Github(token)
    repo = g.get_repo(repo_name)

    issues = repo.get_issues(state="open")

    for issue in issues:
        if issue.pull_request is not None:
            # Ignore pull requests
            continue

        issue_age = (datetime.utcnow() - issue.created_at).days

        if issue_age > 7:
            comment = f"⏰ Reminder: This issue is more than 7 days old. Please review and take the necessary actions."
            issue.create_comment(comment)

if __name__ == "__main__":
    main()
