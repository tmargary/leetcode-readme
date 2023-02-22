from github import Github

if __name__ == "__main__":
    # Replace with your GitHub access token
    ACCESS_TOKEN = "your_access_token_here"

    # Replace with your GitHub username and repository name
    USERNAME = "your_username_here"
    REPO_NAME = "your_repository_name_here"

    g = Github(ACCESS_TOKEN)
    repo = g.get_user(USERNAME).get_repo(REPO_NAME)
    readme_links = get_readme_links(repo)
    print("\n".join(readme_links))