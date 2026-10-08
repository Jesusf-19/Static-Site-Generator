import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

class Test_Block_Markdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items"""
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(blocks, [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items"
        ])

    def test_block_to_heading_blocktype(self):
        block = "### Hello World"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_heading_no_space(self):
        block = "######Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_more_than_6_hashtags_headings(self):
        block = "####### Hello world"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_code_blocktype(self):
        block = "```\nprint('Hello, world')```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_quote_blocktype(self):
        block = ">first line\n>second line\n>third line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_unordered_list_blocktype(self):
        block = "- first line\n- second line\n- third line"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_block_to_ordered_list_blocktype(self):
        block = "1. first line\n2. second line\n3. third line"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_not_ordered_list(self):
        block = "1. first line\n3. second line\n4. third line"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Testcases for block to HTML
    def test_pragraphs(self):
        markdown = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")

    def test_heading(self):
        markdown = "# Hello World"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><h1>Hello World</h1></div>")

    def test_heading_with_bolding(self):
        markdown = "### This is **important**"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><h3>This is <b>important</b></h3></div>")

    def test_quote(self):
        markdown = """> This is a quote
> This is another line"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><blockquote>This is a quote This is another line</blockquote></div>")

    def test_unordered_lists(self):
        markdown = """- Apple
- Banana
- Orange"""

        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>Apple</li><li>Banana</li><li>Orange</li></ul></div>")

    def test_ordered_lists(self):
        markdown = """1. First item
2. Second item
3. Third item"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>")

    def test_list_with_formatting(self):
        markdown = """- This is **bold**
- This is _italic_
- This is `code`"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>This is <b>bold</b></li><li>This is <i>italic</i></li><li>This is <code>code</code></li></ul></div>")

    def test_paragraph_with_image(self):
        markdown = "Here is an ![image](https://example.com/image.png)"
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, '<div><p>Here is an <img src="https://example.com/image.png" alt="image"></img></p></div>')

    def test_pargraph_with_link(self):
        markdown = "Visit [Boot.dev](https://boot.dev) to learn Python."
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, '<div><p>Visit <a href="https://boot.dev">Boot.dev</a> to learn Python.</p></div>')

    def test_codeblock(self):
        markdown = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(markdown)
        html = node.to_html()
        self.assertEqual(html, "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>")


if __name__ == "__main__":
    unittest.main()