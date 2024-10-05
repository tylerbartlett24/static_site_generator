import unittest
from extract_functions import *


class TestExtractFunctions(unittest.TestCase):
    
    def test_image_extract(self):
        text = ("This is text with a ![rick roll]"
                "(https://i.imgur.com/aKaOqIh.gif)"
                " and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        target =  [("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                   ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        test = extract_markdown_images(text)
        self.assertEqual(test, target)
        
    def test_link_extract(self):
        text = ("This is text with a link [to boot dev]"
                "(https://www.boot.dev) and [to youtube]"
                "(https://www.youtube.com/@bootdotdev)")
        target = [("to boot dev", "https://www.boot.dev"),
                  ("to youtube", "https://www.youtube.com/@bootdotdev")]
        test = extract_markdown_links(text)
        self.assertEqual(test, target)
        