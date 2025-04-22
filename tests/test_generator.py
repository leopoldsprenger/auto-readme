import unittest
from unittest.mock import patch
from pathlib import Path
import sys

# Add the 'core' directory to the sys.path to allow imports from core/
sys.path.append(str(Path(__file__).resolve().parent.parent / 'core'))

from generator import generate_readme_content


class TestGenerator(unittest.TestCase):

    @patch('generator.get_response')
    def test_generate_readme_content(self, mock_get_response):
        # Mock the OpenAI API response
        mock_get_response.return_value = 'Generated README content here.'

        # Test input
        summarized_files = {'file1.txt': 'Summarized content of file1.'}
        binary_files = ['binaryfile.exe']
        repo_full_name = 'user/repo'
        user_prompt = 'Custom prompt here.'

        # Call the function
        result = generate_readme_content(summarized_files, binary_files,
                                         repo_full_name, user_prompt)

        # Validate output
        self.assertEqual(result, 'Generated README content here.')
        mock_get_response.assert_called_once()


if __name__ == '__main__':
    unittest.main()
