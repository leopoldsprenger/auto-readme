import unittest
from unittest.mock import patch, MagicMock
from pathlib import Path
import sys

# Add the 'core' directory to the sys.path to allow imports from core/
sys.path.append(str(Path(__file__).resolve().parent.parent / 'core'))

from github_scraper import extract_text_files, is_binary_file


class TestGitHubScraper(unittest.TestCase):

    @patch('github_scraper.Github')
    def test_extract_text_files(self, MockGithub):
        # Mock file 1 (text file)
        file1 = MagicMock()
        file1.path = "file1.txt"
        file1.type = "file"
        file1.decoded_content = b"Sample content"

        # Mock file 2 (binary file)
        binary_file = MagicMock()
        binary_file.path = "binaryfile.exe"
        binary_file.type = "file"
        binary_file.decoded_content = b"\x00\x01\x02"  # Non-text bytes

        # Side effect to simulate UnicodeDecodeError on binary file
        def is_binary_side_effect(file):
            if file.path == "binaryfile.exe":
                raise UnicodeDecodeError("utf-8", b"", 0, 1,
                                         "invalid start byte")
            return False

        # Patch is_binary_file function instead of relying on real logic
        with patch('github_scraper.is_binary_file',
                   side_effect=lambda f: f.path == "binaryfile.exe"):
            mock_repo = MagicMock()
            mock_repo.get_contents.return_value = [file1, binary_file]
            MockGithub.return_value.get_repo.return_value = mock_repo

            files_dict, binary_files = extract_text_files(mock_repo)

            self.assertIn("file1.txt", files_dict)
            self.assertIn("binaryfile.exe", binary_files)
            self.assertEqual(len(files_dict), 1)
            self.assertEqual(len(binary_files), 1)

    def test_is_binary_file(self):
        # Test for non-binary file
        mock_file_text = MagicMock()
        mock_file_text.decoded_content = b"This is a text file."
        self.assertFalse(is_binary_file(mock_file_text))

        # Test for binary file
        mock_file_binary = MagicMock()
        mock_file_binary.decoded_content = MagicMock()
        mock_file_binary.decoded_content.decode.side_effect = UnicodeDecodeError(
            "utf-8", b"", 0, 1, "invalid start byte")
        self.assertTrue(is_binary_file(mock_file_binary))

if __name__ == '__main__':
    unittest.main()
