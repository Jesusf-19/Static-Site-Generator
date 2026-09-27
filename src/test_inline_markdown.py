import unittest
from textnode import TextNode, TextType, split_nodes_delimiter

class TestInlineMarkdown(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
                         TextNode("This is text with a ", TextType.TEXT),
                         TextNode("code block", TextType.CODE),
                         TextNode(" word", TextType.TEXT)])

    def test_split_bold(self):
        node = TextNode("This is a text with **bold phrase** inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
                         TextNode("This is a text with ", TextType.TEXT),
                         TextNode("bold phrase", TextType.BOLD),
                         TextNode(" inside", TextType.TEXT)])

    def test_split_italic(self):
        node = TextNode("This is a text with _italic phrase_ inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
                         TextNode("This is a text with ", TextType.TEXT),
                         TextNode("italic phrase", TextType.ITALIC),
                         TextNode(" inside", TextType.TEXT)])

    def test_with_no_delimiter(self):
        node = TextNode("This is a text phrase", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.TEXT)
        self.assertEqual(new_nodes, [
            TextNode("This is a text phrase", TextType.TEXT)
        ])

    def test_no_matching_closing_delimiter(self):
        node = TextNode("This is a text with a _italic phrase inside", TextType.TEXT)
        with self.assertRaises(Exception):
            new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)


if __name__ == "__main__":
    unittest.main()