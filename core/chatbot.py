import openai
from typing import Literal, Dict

# Prompt templates for the chatbot
prompts: Dict[str, str] = {
    "one file summary": (
        "Summarize the following source code file in markdown. Do not include any text outside of the summary itself. "
        "Begin with a 1–2 sentence high-level overview of the file’s purpose. "
        "Then include specific code snippets with concise explanations for important parts that should be highlighted in a README (e.g., core classes, scraping functions, model definitions, etc.)."
    ),
    "generate readme": (
        "Create a complete README file in markdown for this GitHub repository based on the summaries provided. "
        "Do not add any extra commentary or markdown code block markers — just return the raw README content. "
        "Structure the README with clear sections: Project Overview, Installation, Usage, License. "
        "Include a brief project description with purpose, and make section headers clickable (i.e., anchor links). "
        "If existing README content is present, restructure or rewrite it to meet these standards. "
        "If binary files (e.g., images, GIFs) are provided, embed them using their filenames when relevant (e.g., demo visuals)."
    )
}


def get_response(
        content: str,
        model: Literal["gpt-3.5-turbo", "gpt-4", "gpt-4o"] = "gpt-4o") -> str:
    """
    Sends a prompt to the OpenAI Chat API and returns the model's response.

    Args:
        content: The user input or system instruction to be sent to the model.
        model: The model name to use for generation. Default is 'gpt-4o'.

    Returns:
        The response content as a string.
    """
    response = openai.chat.completions.create(model=model,
                                              messages=[{
                                                  "role": "user",
                                                  "content": content
                                              }])
    return response.choices[0].message.content
