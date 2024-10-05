import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_default(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_eq2(self):
        node = TextNode("This is a text node", "bold", "yourmom.com")
        node2 = TextNode("This is a text node", "italic", "yourmom.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()