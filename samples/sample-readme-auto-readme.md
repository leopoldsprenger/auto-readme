# Auto README Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

The Auto README Generator is a tool designed to automatically generate README files for your GitHub projects. By leveraging OpenAI's GPT models, it saves you time and effort in documenting your projects, improving their presentation and making them more accessible to collaborators and users. This is especially useful for rapid prototyping and projects where documentation might otherwise be neglected.

*   [Installation](#installation)
*   [Usage](#usage)
*   [Why It's Useful](#why-its-useful)
*   [License](#license)

## Demo

*(Include a GIF or screenshot here showcasing the tool in action)*

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/leopoldsprenger/auto-readme.git
    cd auto-readme
    ```

2.  **Create a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    *   Create a `.env` file in the root directory of the project.
    *   Add your OpenAI API key and GitHub token (optional, but recommended for accessing private repositories) to the `.env` file:

        ```
        OPENAI_API_KEY=YOUR_OPENAI_API_KEY
        GITHUB_TOKEN=YOUR_GITHUB_TOKEN # Optional: Only needed for private repos or higher rate limits
        ```

    *   Remember to replace `YOUR_OPENAI_API_KEY` and `YOUR_GITHUB_TOKEN` with your actual API key and token. You can get an OpenAI API key from [OpenAI's website](https://platform.openai.com/). You can create a GitHub token with `repo` scope from [GitHub's personal access tokens settings](https://github.com/settings/tokens).

## Usage

The tool is run from the command line using the `cli/main.py` script.

1.  **Navigate to the project directory:**

    ```bash
    cd auto-readme
    ```

2.  **Run the script with the repository name as an argument:**

    ```bash
    python cli/main.py your_github_username/your_repository_name
    ```

    Replace `your_github_username/your_repository_name` with the actual username and repository name. For example: `python cli/main.py leopoldsprenger/auto-readme`

3.  **Optional: Use a custom prompt:**

    You can provide a custom prompt to tailor the generated README to your specific needs.

    ```bash
    python cli/main.py your_github_username/your_repository_name --prompt "Write a README for a project that implements a machine learning model for image classification."
    ```

4.  **Output:**

    The generated README file will be saved as `README_output.md` in the same directory where you run the script.

## Why It's Useful

*   **Saves Time:** Automatically generates a well-structured README file, eliminating the need to write one from scratch.
*   **Improves Project Presentation:** Creates a professional-looking README, making your project more appealing to potential users and contributors.
*   **Facilitates Collaboration:** Provides clear documentation, making it easier for others to understand and contribute to your project.
*   **Ideal for Rapid Prototyping:** Quickly generates basic documentation for new projects, allowing you to focus on development.
*   **Automatic summarization of Code:** Using the `core/chatbot.py` module the tool automatically summarises all code and generate documentation from it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
