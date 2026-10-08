import unittest
from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello World"
        title = extract_title(markdown)
        self.assertEqual(title, "Hello World")

    def test_extract_title_with_spaces(self):
        markdown = "#       The Hunger Games      "
        title = extract_title(markdown)
        self.assertEqual(title, "The Hunger Games")

    def test_extract_title_no_h1(self):
        markdown = "### Hello World"
        with self.assertRaises(Exception):
            extract_title(markdown)
    


if __name__ == "__main__":
    unittest.main()