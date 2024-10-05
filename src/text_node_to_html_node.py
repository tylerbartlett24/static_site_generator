from htmlnode import LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href" : f"{text_node.url}"})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src" : f"{text_node.url}",
                                    "alt" : f"{text_node.text}"})
    else:
        raise Exception("Invalid Text Type")