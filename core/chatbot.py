import openai
from typing import Literal, Dict

# Prompt templates for the chatbot
prompts: Dict[str, str] = {
    "one file summary": (
        "Please summarize this file briefly in markdown and don't add any text other than the summary to your answer. "
        "Include a 2 sentence summary of the code function and any explanation for sections that could be important to mention "
        "in a readme file for any repository that file may be in:"
    ),
    "generate readme": (
        "Take all of these readme files and generate a single readme file for the entire repository. "
        "Don't write the markdown declaration symbols before and after the contents of the readme file, just return its contents. "
        "Also don't add anything like 'here is the contents of the readme file', just return the readme file without any further explanation. "
        "Make it interactive with distinct sections like installation, usage, and license. Include installation instructions, usage examples, and license information. "
        "Also make a project overview section that includes a brief description of the project and its purpose with links to clickable headers. "
        "Please also use the names of the provided binary files and include them as embeds in the readme file when you think applicable (use the file names and endings as context clues). "
        "If you find an already existing readme in the files I list, please restructure it or completely rewrite it depending on how in-depth it is, since the user wants a new one."
    )
}


def get_response(
    content: str,
    model: Literal["gpt-3.5-turbo", "gpt-4", "gpt-4o"] = "gpt-4o"
) -> str:
    """
    Sends a prompt to the OpenAI Chat API and returns the model's response.

    Args:
        content: The user input or system instruction to be sent to the model.
        model: The model name to use for generation. Default is 'gpt-4o'.

    Returns:
        The response content as a string.
    """
    response = openai.Completion.create(
        model=model,
        messages=[{"role": "user", "content": content}]
    )
    return response.choices[0].message
