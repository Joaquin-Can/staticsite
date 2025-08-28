from textnode import *

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        string_list = []
        if self.props is not None:
            for key in self.props:
                string_list.append(f'{key}="{self.props[key]}"')
            return " ".join(string_list)
        return ""
        

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        result = self.props_to_html()
        if self.value is None:
            raise ValueError
        if self.tag is None or self.tag == "":
            return f"{self.value}"
        if self.props is None or result == "":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag} {result}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag found")
        if self.children is None:
            raise ValueError("No children node found")
        result = ""
        for element in self.children:
            result += element.to_html()
        return f"<{self.tag}>{result}</{self.tag}>"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    raise Exception("Not supported text type")
