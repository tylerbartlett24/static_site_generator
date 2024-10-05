import unittest
from generating_functions import *

class TestGenFunc(unittest.TestCase):
    def test_title_extract(self):
        text = "#   Heading  \n\ntext"
        target = "Heading"
        trial = extract_title(text)
        self.assertEqual(target, trial)