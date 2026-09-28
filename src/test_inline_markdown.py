import unittest
from textnode import TextNode, TextType, split_nodes_delimiter, extract_markdown_images, extract_markdown_links

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

    def test_extract_markdown_image(self):
        text =  "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(matches, [("image", "https://i.imgur.com/zjjcJKZ.png")])

    def test_extract_multiple_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual(matches, [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_markdown_link(self):
        text = "This is a text with a link [google](https://www.google.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [("google", "https://www.google.com")])

    def test_extract_multiple_markdown_links(self):
        text = "This is text with a link [google](https://www.google.com) and [to youtube](https://www.youtube.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [
            ("google", "https://www.google.com"),
            ("to youtube", "https://www.youtube.com")
        ])

    def test_extract_images_not_pick_up_as_links(self):
        text = "This is an image ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [])
    
if __name__ == "__main__":
    unittest.main()