import unittest
from markdown_to_html_node import *

class TestMarkdownToHTMLNode(unittest.TestCase):
    
    def test_block_to_html_list(self):
        self.maxDiff = None
        block_type = block_type_ulist
        text = "* Normal* **Bold*** *Italic*"
        target = ParentNode("ul", [ParentNode("li",[LeafNode(None,"Normal")]),
                                   ParentNode("li", [LeafNode("b", "Bold")]),
                                   ParentNode("li", 
                                              [LeafNode("i", "Italic")])
                                   ])
        trial = block_to_html_list(text, block_type)
        self.assertEqual(trial, target)
        
    def test_block_to_html_code(self):
        block_type = block_type_code
        text = "code"
        target=ParentNode("pre",[ParentNode("code",[LeafNode(None,"code")])])
        trial = block_to_html_not_list(text, block_type)
        self.assertEqual(trial, target)
        
    def test_block_to_html_heading(self):
        block_type = block_type_heading
        text = "Heading*italic*"
        head_num = 3
        target=ParentNode("h3",
                          [LeafNode(None, "Heading"),
                           ParentNode("i",[LeafNode(None, "italic")])])
        trial = block_to_html_not_list(text, block_type, head_num)
        self.assertEqual(trial.to_html(), target.to_html())
        
    def test_markdown_to_html_node(self):
        text = ">quote>quote\n\n## Heading\n\n1. list\n2. list\n\ntext"
        target = ("<div><blockquote>quotequote</blockquote><h2>Heading</h2>"
                  "<ol><li>list</li><li>list</li></ol><p>text</p></div>")
        trial = markdown_to_html_node(text)
        self.assertEqual(trial.to_html(), target)
        