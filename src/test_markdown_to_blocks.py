import unittest
from markdown_to_blocks import *

class TestMarkdownToBlocks(unittest.TestCase):
    
    def test_example_from_site(self):
        s = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        target = [
            "# This is a heading",
            ("This is a paragraph of text. It has some **bold** and *italic*"
             " words inside of it."),
            ("* This is the first list item in a list block\n"
             "* This is a list item\n"
             "* This is another list item")
        ]
        test = markdown_to_blocks(s)
        self.assertEqual(test, target)
        
    def test_extra_newlines(self):
        s = "Here is some text\n\n\n     More text"
        target = ["Here is some text",
                  "More text"]
        test = markdown_to_blocks(s)
        self.assertEqual(test, target)
