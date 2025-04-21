from github import Github, Repository
from github.ContentFile import ContentFile
from typing import Dict, Tuple, List


def authenticate_github(token: str) -> Github:
    """
    Authenticates with the GitHub API using a personal access token.

    Args:
        token: Personal Access Token (PAT) for GitHub authentication.

    Returns:
        Authenticated Github object.
    """
    return Github(token)


def fetch_repository(github: Github, username: str, repo_name: str) -> Repository.Repository:
    """
    Fetches a specific repository from a GitHub account.

    Args:
        github: Authenticated Github object.
        username: GitHub username.
        repo_name: Repository name.

    Returns:
        Repository object.
    """
    return github.get_repo(f"{username}/{repo_name}")


def is_binary_file(content_file: ContentFile) -> bool:
    """
    Determines whether a file is binary based on its decoding behavior.

    Args:
        content_file: A GitHub content file object.

    Returns:
        True if the file is binary, False otherwise.
    """
    try:
        _ = content_file.decoded_content.decode("utf-8")
        return False
    except UnicodeDecodeError:
        return True


def extract_text_files(repo: Repository.Repository) -> Tuple[Dict[str, str], List[str]]:
    """
    Extracts all readable text files from a repository.

    Args:
        repo: The GitHub repository object.

    Returns:
        A tuple containing:
            - A dictionary of file paths to UTF-8 decoded file contents.
            - A list of binary file paths.
    """
    file_contents: Dict[str, str] = {}
    binary_files: List[str] = []
    contents: List[ContentFile] = repo.get_contents("")

    while contents:
        item = contents.pop(0)
        if item.type == "dir":
            contents.extend(repo.get_contents(item.path))
        else:
            if is_binary_file(item):
                binary_files.append(item.path)
            else:
                file_contents[item.path] = item.decoded_content.decode("utf-8")

    return file_contents, binary_files


def get_files_from_repo(username: str, repo_name: str, token: str) -> Tuple[Dict[str, str], List[str]]:
    """
    Retrieves all UTF-8 decodable files and binary file paths from a GitHub repository.

    Args:
        username: GitHub username.
        repo_name: Name of the repository.
        token: GitHub personal access token.

    Returns:
        Tuple of:
            - Dictionary of text file paths to contents.
            - List of binary file paths.
    """
    github = authenticate_github(token)
    repo = fetch_repository(github, username, repo_name)
    return extract_text_files(repo)
