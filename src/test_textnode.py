import unittest

from textnode import TextNode, TextType
from inline_markdown import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_inq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_eq2(self):
        node = TextNode("blabla", TextType.TEXT)
        node2 = TextNode("blabla", TextType.TEXT)
        self.assertEqual(node, node2)


node_1 = TextNode("no markers here", TextType.TEXT)
node_2 = TextNode("a b c", TextType.TEXT)
node_3 = TextNode("a b c", TextType.TEXT)
new_list = [node_1, node_2, node_3]
split_nodes_delimiter(new_list,  "`", TextType.CODE)

out = split_nodes_delimiter(
    [TextNode("no markers here", TextType.TEXT),
     TextNode("a `b` c", TextType.TEXT),
     TextNode("x", TextType.TEXT)],
    "`",
    TextType.CODE,
)
for n in out:
    print(n.text, n.text_type)

def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

text_1 = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text_2 = "This is"
text_3 = "This is **text**"
text_4 = "This is ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
text_5 = ""
text_6 = "`code block`"
def first_test(self):
    first_result = text_to_textnodes(text_1)
    self.assertListEqual([
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
], first_result)
def second_test(self):
    second_result = text_to_textnodes(text_2)
    self.assertListEqual([TextNode("This is", TextType.TEXT)], second_result)
def third_test(self):
    third_result = text_to_textnodes(text_3)
    self.assertListEqual([TextNode("This is", TextType.TEXT), TextNode("text", TextType.BOLD)], third_result)
def fourth_test(self):
    fourth_result = text_to_textnodes(text_5)
    self.assertListEqual([TextNode("", TextType.TEXT)], fourth_result)





if __name__ == "__main__":
    unittest.main()
