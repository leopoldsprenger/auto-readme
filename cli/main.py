import argparse
import sys
from pathlib import Path
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

core_path = Path(__file__).resolve().parent.parent / "core"
sys.path.append(str(core_path))

from generator import (
    get_repository_files,
    summarize_files,
    generate_readme_content,
    save_readme,
)
from chatbot import prompts


def parse_arguments() -> argparse.Namespace:
    """
    Parses command-line arguments for the repository name and optional custom prompt.

    Returns:
        argparse.Namespace: Parsed arguments with 'repo' and 'prompt' fields.
    """
    parser = argparse.ArgumentParser(
        description="Generate a README for a GitHub repository using OpenAI."
    )
    parser.add_argument(
        "repo",
        type=str,
        help="GitHub repository in the format 'username/repository_name'"
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default=prompts["generate readme"],
        help="Custom prompt to guide the structure and tone of the generated README"
    )
    return parser.parse_args()


def main() -> None:
    """
    Handles program execution and user interaction via the command line.
    """
    arguments = parse_arguments()
    repo_full_name = arguments.repo
    custom_prompt = arguments.prompt

    try:
        print(f"{Fore.CYAN}Starting README generation for: {repo_full_name}{Style.RESET_ALL}")

        print(f"{Fore.YELLOW}Fetching repository files...{Style.RESET_ALL}")
        try:
            files_dict, binary_files = get_repository_files(repo_full_name)
        except Exception as e:
            print(f"{Fore.RED}Error fetching repository files: {e}{Style.RESET_ALL}")
            sys.exit(1)

        if not files_dict:
            raise ValueError("No files found in the repository.")

        print(f"{Fore.YELLOW}Summarizing text files...{Style.RESET_ALL}")
        summarized_files = summarize_files(files_dict)

        print(f"{Fore.YELLOW}Generating README content...{Style.RESET_ALL}")
        readme_content = generate_readme_content(
            summarized_files,
            binary_files,
            repo_full_name,
            user_prompt=custom_prompt
        )

        print(f"{Fore.GREEN}Saving README to 'README_output.md'...{Style.RESET_ALL}")
        save_readme(readme_content)

        print(f"{Fore.GREEN}README generation complete.{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program interrupted by user.{Style.RESET_ALL}")
        sys.exit(0)


if __name__ == "__main__":
    main()
