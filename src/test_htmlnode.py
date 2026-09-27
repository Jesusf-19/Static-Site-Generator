import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"href": "https://www.google.com",
                               "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), 
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html_with_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_empty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "paragraph"})
        self.assertEqual(repr(node), "HTMLNode(p, Hello, None, {'class': 'paragraph'})")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_raw_txt(self):
        node = LeafNode(None, "This is raw text")
        self.assertEqual(node.to_html(), "This is raw text")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchildren = LeafNode("b", "grandchild")
        children = ParentNode("span", [grandchildren])
        parent = ParentNode("div", [children])
        self.assertEqual(parent.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_childrens(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, "Normal text")
        child3 = LeafNode("i", "Italic")
        parent = ParentNode("div", [child1, child2, child3])
        self.assertEqual(parent.to_html(), 
                         "<div><b>Bold text</b>Normal text<i>Italic</i></div>")

    def test_to_html_with_props(self):
        child = LeafNode(None, "Click me")
        parent = ParentNode("a", [child], {"href": "https://www.google.com"})
        self.assertEqual(parent.to_html(), 
                         '<a href="https://www.google.com">Click me</a>')

    def test_to_html_with_no_tag(self):
        child = LeafNode(None, "Regular Text")
        parent = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_with_no_children(self):
        parent = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent.to_html()



if __name__ == "__main__":
    unittest.main()