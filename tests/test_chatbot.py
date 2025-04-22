import unittest
from unittest.mock import patch, MagicMock
import os
from pathlib import Path
import sys

# Set a dummy API key for testing to prevent OpenAIError
os.environ['OPENAI_API_KEY'] = 'dummy-key'

# Add core/ to sys.path to import chatbot.py
sys.path.append(str(Path(__file__).resolve().parent.parent / 'core'))

from chatbot import get_response

class TestChatBot(unittest.TestCase):

    @patch('chatbot.openai.chat.completions.create')
    def test_get_response(self, mock_create):
        # Create a mocked response object
        mock_create.return_value.choices = [
            MagicMock(message=MagicMock(content="Mocked response"))
        ]

        prompt = "Summarize this code"
        result = get_response(prompt)

        self.assertEqual(result, "Mocked response")
        mock_create.assert_called_once_with(model="gpt-4o",
                                            messages=[{
                                                "role": "user",
                                                "content": prompt
                                            }])


if __name__ == '__main__':
    unittest.main()
