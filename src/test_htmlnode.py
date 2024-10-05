import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode("text", "more text", "whatever")
        node2 = HTMLNode("text", "more text", "whatever")
        self.assertEqual(node, node2)
        
    def test_def_1(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        
    def test_def_2(self):
        node = HTMLNode()
        self.assertIsNone(node.value)
        
    def test_def_3(self):
        node = HTMLNode()
        self.assertIsNone(node.children)
        
    def test_def_4(self):
        node = HTMLNode()
        self.assertIsNone(node.props)
        
    def test_props_to_html(self):
        node = HTMLNode("text", "more text", "whatever", 
                        {
                            "href" : "yourmom.com"
                        })
        target = ' href="yourmom.com"'
        self.assertEqual(node.props_to_html(), target)
        
    def test_leaf_to_html1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        target = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), target)
        
    def test_leaf_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        target = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(node.to_html(), target)
        
    def test_leaf_to_html3(self):
        node = LeafNode(None, "some text")
        target = "some text"
        self.assertEqual(node.to_html(), target)
        
    def test_parent_to_html_multi_child(self):
        node = ParentNode(
            "p", 
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        t = '<p><b>Bold Text</b>Normal Text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), t)
        
    def test_parent_to_html_nest_parent(self):
        node = ParentNode(
            "body",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "italic text"),
                        LeafNode(None, "some text")
                    ]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "some text"),
                        LeafNode("b", "bold text")
                    ]
                ),
                LeafNode("p", "some text")   
            ]
        )
        target =  ('<body><p><i>italic text</i>some text</p><p>some text<b>'
                      'bold text</b></p><p>some text</p></body>')
        self.assertEqual(node.to_html(), target)
        
    def test_parent_to_html_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None)
            html = node.to_html()
        
if __name__ == "__main__":
    unittest.main()
        