
def get_file_text_and_url(file):
    """
    Extracts the second line of text and the GitHub URL of a file.
    """
    text = None
    url = file.html_url

    with file.raw_data() as data:
        lines = data.readlines()
        if len(lines) >= 2:
            text = lines[1].decode().strip()

    return text, url

def get_readme_links(repo):
    """
    Recursively checks a GitHub repo's files and returns a README file
    in the format [Text](url).
    """
    readme_links = []

    for file in repo.get_contents(""):
        if file.type == "file":
            if file.name.lower() == "readme.md":
                text, url = get_file_text_and_url(file)
                if text is not None:
                    readme_links.append(f"[{text}]({url})")
            elif file.name.lower().endswith(".md"):
                readme_links += get_readme_links(file)

    return readme_links
