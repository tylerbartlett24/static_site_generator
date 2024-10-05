from htmlnode import LeafNode
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode
import unittest

class TestTextHTML(unittest.TestCase):
    
    def test_italic(self):
        text = TextNode("Italic text", "italic")
        target = LeafNode("i", "Italic text")
        self.assertEqual(text_node_to_html_node(text), target)
        
    def test_bold(self):
        text = TextNode("Bold text", "bold")
        target = LeafNode("b", "Bold text")
        self.assertEqual(text_node_to_html_node(text), target)
    
    def test_error(self):
        with self.assertRaises(Exception):
            text = TextNode("text", "jimmy")
            html = text_node_to_html_node(text)
