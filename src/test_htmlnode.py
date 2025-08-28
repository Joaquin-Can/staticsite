import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    def test_inq(self):
        node = HTMLNode(tag="h1", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="a", props={"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    def test_eq2(self):
        node = HTMLNode(tag="h1", props={"href": "https://www.google.com"})
        node2 = HTMLNode(tag="h1", props={"href": "https://www.google.com"})
        self.assertEqual(node, node2)

    def method(self):
        node2 = HTMLNode(tag="h1", props={"href": "https://www.google.com"})
        return node2.props_to_html()

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_p(self):
        node = LeafNode("a", "Hello, world!")
        self.assertEqual(node.to_html(), "<a>Hello, world!</a>")

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_no_children(self):
        parent_node = ParentNode("span", [])
        self.assertEqual(parent_node.to_html(), "<span></span>" )

    def test_to_html_multiple_children(self):
        child_1 = LeafNode("a", "child1")
        child_2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_1, child_2])
        self.assertEqual(parent_node.to_html(), "<div><a>child1</a><b>child2</b></div>")
    

def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

def test_text_2(self):
    node = TextNode("This is a text node", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is a text node")

def test_text_3(self):
    node = TextNode("This is a text node", TextType.LINK, url="www.coocoo.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "This is a text node")
    self.assertEqual(html_node.props, {"href": "www.coocoo.com"})