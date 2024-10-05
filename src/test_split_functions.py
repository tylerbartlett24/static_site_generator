import unittest
from split_functions import *

class TestSplitNodes(unittest.TestCase):
    
    def test_italic_next(self):
        node = TextNode("Here is some **te****xt**", "text")
        test = split_nodes_delimiter([node], "**", "bold")
        target = [
            TextNode("Here is some ", "text"),
            TextNode("te", "bold"),
            TextNode("xt", "bold")
        ]
        self.assertEqual(test, target)
        
    def test_code(self):
        node = TextNode("Here is some `code`", "text")
        test = split_nodes_delimiter([node], "`", "code")
        target = [
            TextNode("Here is some ", "text"),
            TextNode("code", "code")
        ]
        self.assertEqual(test, target)
        
    def test_two_things(self):
        node = TextNode("*Here* is some `code`", "text")
        node2 = TextNode("Some **bold** text", "text")
        list = [node, node2]
        test = split_nodes_delimiter(list, "**", "bold")
        test = split_nodes_delimiter(test, "`", "code")
        test = split_nodes_delimiter(test, "*", "italic")
        target = [
            TextNode("Here", "italic"),
            TextNode(" is some ", "text"),
            TextNode("code", "code"),
            TextNode("Some ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text")
        ]
        self.assertEqual(test, target)
        
    def test_2_images(self):
        s = ("This is text with a "
             "![rick roll](https://i.imgur.com/aKaOqIh.gif)"
             " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        node = TextNode(s, "text")
        result = split_nodes_image([node])
        target = [
            TextNode("This is text with a ", "text"),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", "text"),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(result, target)
        
    def test_text_to_text_nodes(self):
        self.maxDiff = None
        s = ("This is **text** with an *italic* word and a `code block` and "
             "an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a"
             " [link](https://boot.dev)")
        target = [
            TextNode("This is ", "text"),
            TextNode("text", "bold"),
            TextNode(" with an ", "text"),
            TextNode("italic", "italic"),
            TextNode(" word and a ", "text"),
            TextNode("code block", "code"),
            TextNode(" and an ", "text"),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text"),
            TextNode("link", "link", "https://boot.dev"),
        ]
        test = text_to_text_nodes(s)
        self.assertEqual(test, target)
        
    def test_link(self):
        node = TextNode(
    ("This is text with a link [to boot dev](https://www.boot.dev)"
     " and [to youtube](https://www.youtube.com/@bootdotdev)"),
    "text",
    )
        nodes = [node]
        target = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", 
                     "https://www.youtube.com/@bootdotdev"), ]
        test = split_nodes_link(nodes)
        self.assertEqual(test, target)