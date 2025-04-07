from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from public_stuff import copy_from_static_to_public
from generating_functions import *
import os
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_from_static_to_public("static", "docs")
    generate_recursively("content",
                  "template.html", 
                  "docs",
                  basepath)
    


if __name__ == "__main__":
    main()