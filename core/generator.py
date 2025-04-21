import os
from typing import Dict, List, Tuple
from github import Github
from dotenv import load_dotenv
from chatbot import get_response, prompts
import github_scraper

# Load environment variables from the .env file
load_dotenv()

# Fetch API tokens from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_PAT = os.getenv("GITHUB_TOKEN")

# Ensure the tokens are available
if not OPENAI_API_KEY or not GITHUB_PAT:
    raise ValueError("API tokens are missing. Please check your .env file.")


def get_repository_files(repo_full_name: str) -> Tuple[Dict[str, str], List[str]]:
    """
    Retrieves all files from the specified GitHub repository and filters out binary files.

    Args:
        repo_full_name: The full name of the repository in the format 'username/reponame'.

    Returns:
        A tuple containing:
            - A dictionary where keys are file paths and values are the file contents.
            - A list of binary files in the repository.
    """
    github = Github(GITHUB_PAT)
    repository = github.get_repo(repo_full_name)
    return github_scraper.extract_text_files(repository)


def summarize_files(files_dict: Dict[str, str]) -> Dict[str, str]:
    """
    Summarizes the content of each text file in the repository using the OpenAI API.

    Args:
        files_dict: A dictionary containing the file paths and contents.

    Returns:
        A dictionary where keys are file paths and values are file summaries.
    """
    summarized_files = {}
    for file_name, file_content in files_dict.items():
        summary = get_response(prompts["one file summary"] + "\nFiles: " + str(file_content))
        summarized_files[file_name] = summary
    return summarized_files


def generate_readme_content(
    summarized_files: Dict[str, str],
    binary_files: List[str],
    repo_full_name: str,
    user_prompt: str = ""
) -> str:
    """
    Generates the content of a README file for the repository by combining file summaries and other details.

    Args:
        summarized_files: A dictionary where keys are file paths and values are file summaries.
        binary_files: A list of binary files in the repository.
        repo_full_name: The full name of the repository in the format 'username/reponame'.

    Returns:
        The generated README content as a string.
    """
    readme_prompt = (
        prompts["generate readme"]
        + f"\nThe repository is named {repo_full_name}"
        + "\nFile summaries: " + str(summarized_files)
        + "\nBinary Files: " + str(binary_files)
        + f"\nThe user requested a specific structure or personal adjustment: {user_prompt}"
    )
    return get_response(readme_prompt)


def save_readme(readme_content: str, output_path: str = "README_output.md") -> None:
    """
    Saves the generated README content to a file.

    Args:
        readme_content: The content to write into the README file.
        output_path: The path where the README file will be saved. Defaults to 'README_output.md'.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(readme_content)


def run_readme_generation(repo_full_name: str) -> str:
    """
    Runs the full pipeline: extract files, summarize them, and generate README content.

    Args:
        repo_full_name: The full name of the GitHub repository in the format 'username/repository_name'.

    Returns:
        str: The complete generated README content.
    """
    files_dict, binary_files = get_repository_files(repo_full_name)
    summarized_files = summarize_files(files_dict)
    readme_content = generate_readme_content(summarized_files, binary_files, repo_full_name)
    return readme_content
