from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node
from public_stuff import copy_from_static_to_public
from generating_functions import *
import os

def main():
    copy_from_static_to_public("static", "public")
    generate_recursively("content",
                  "template.html", 
                  "public")
    


if __name__ == "__main__":
    main()