from block_to_block_type import *
from markdown_to_blocks import *
from htmlnode import *
from textnode import TextNode
from split_functions import *
from text_node_to_html_node import text_node_to_html_node
import re

def strip_identifiers_not_list(block, block_type):
    if block_type == block_type_code:
        return block.strip("```").strip()
    elif block_type == block_type_heading:
        return block.lstrip("#").strip()
    elif block_type == block_type_quote:
        block = re.sub(r">", "", block)
        block = block.strip()
        return block
    elif block_type == block_type_olist:
        return block
    elif block_type == block_type_paragraph:
        return block
    elif block_type == block_type_ulist:
        return block
    else:
        raise Exception("Invalid block type")
    
def block_to_html_not_list(block_text, block_type, number=0):
    children = []
    nodes = text_to_text_nodes(block_text)
    for node in nodes:
        leaf_node = text_node_to_html_node(node)
        children.append(leaf_node)
    if block_type == block_type_code:
        return ParentNode("pre", [ParentNode("code", children)])
    elif block_type == block_type_heading:
        return ParentNode(f"h{number}", children)
    elif block_type == block_type_quote:
        return ParentNode("blockquote", children)
    elif block_type == block_type_paragraph:
        return ParentNode("p", children)
    
def block_to_html_list(block_text, block_type):
    if block_type == block_type_ulist:
        block_text = block_text.lstrip("* ")
        block_text = block_text.lstrip("- ")
        lines = re.split(r"- |\* ", block_text)
        child_nodes = []
        for line in lines:
            line = line.rstrip("\n")
            line = line.strip()
            text_nodes = text_to_text_nodes(line)
            leaves = []
            for text_node in text_nodes:
                html = text_node_to_html_node(text_node)
                leaves.append(html)
            list_item = ParentNode("li", leaves)
            child_nodes.append(list_item)
        return ParentNode("ul", child_nodes)
    elif block_type == block_type_olist:
        block_text = re.sub("^\d\. ", "", block_text)
        lines = re.split(r"\d\. ", block_text)    
        child_nodes = []
        for line in lines:
            line = line.rstrip("\n")
            line = line.rstrip()
            text_nodes = text_to_text_nodes(line)
            leaves = []
            for text_node in text_nodes:
                html = text_node_to_html_node(text_node)
                leaves.append(html)
            list_item = ParentNode("li", leaves)
            child_nodes.append(list_item)
        return ParentNode("ol", child_nodes)
            
            

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    head_num = 0
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type != block_type_olist and block_type != block_type_ulist:
            if block_type == "heading":
                head_num = len(block) - len(block.lstrip("#"))
            text = strip_identifiers_not_list(block, block_type)
            html = block_to_html_not_list(text, block_type, head_num)
            child_nodes.append(html)
        else:
            html = block_to_html_list(block, block_type)
            child_nodes.append(html)
    return ParentNode("div", child_nodes)