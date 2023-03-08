import sys

from github import Github, Milestone, Issue
import argparse
import os

FILENAME = "record.md"
ANCHOR_NUMBER = 5


def login(token):
    return Github(token)


def get_repo(user: Github, repo: str):
    return user.get_repo(repo)


def get_milestone_number(milestone: Milestone):
    if milestone is None:
        return sys.maxsize
    return milestone.number


def get_issue_number(issue: Issue):
    return issue.number


def save(repo, m2i: dict):
    with open(FILENAME, "w") as f:
        f.writelines('# ' + repo.name + '\n\n')
        milestone_list = list(m2i.keys())
        milestone_list.sort(key=get_milestone_number)
        for milestone in milestone_list:
            if milestone is None:
                title = "未分类"
            else:
                title = milestone.title
            f.writelines('## ' + title + '\n')
            m2i.get(milestone).sort(key=get_issue_number)
            for issue in m2i.get(milestone):
                labels = issue.get_labels()
                labels_str = ' '.join(list(map(lambda x: x.name, labels)))
                f.writelines('[' + issue.title + '](' + issue.body + ')    ' + labels_str + '\n\n')


def main(token, repo_name):
    user = login(token)
    repo = user.get_repo(repo_name)
    issues = repo.get_issues(creator=user.get_user().login)
    m2i = {}
    for issue in issues:
        milestone = issue.milestone
        if milestone in m2i:
            m2i.get(milestone).append(issue)
        else:
            m2i[milestone] = [issue]
    save(repo, m2i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    options = parser.parse_args()
    main(options.github_token, options.repo_name)
