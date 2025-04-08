from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes, delim, type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            count =  node.text.count(delim)
            #if count % 2 != 0:
                #raise Exception("Illegal Markdown: No terminating delimiter")
            chunks = node.text.split(delim)
            for i in range(0, len(chunks)):
                if i % 2 == 0:
                    if chunks[i] != "":
                        new_node = TextNode(chunks[i], "text")
                        new_nodes.append(new_node)
                else:
                    new_node = TextNode(chunks[i], type)
                    new_nodes.append(new_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            text = node.text
            chunks = re.split(r"!\[(.*?)\]\((.*?)\)", text)
            i = 0
            while i < len(chunks):
                if i % 3 == 0:
                    if chunks[i] != "":
                        new_node = TextNode(chunks[i], "text")
                        new_nodes.append(new_node)
                    i+=1
                else:
                    new_node = TextNode(chunks[i], "image", chunks[i+1])
                    new_nodes.append(new_node)
                    i+=2
    return new_nodes
    
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            text = node.text
            chunks = re.split(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
            i = 0
            while i < len(chunks):
                if i % 3 == 0:
                    if chunks[i] != "":
                        new_node = TextNode(chunks[i], "text")
                        new_nodes.append(new_node)
                    i+=1
                else:
                    new_node = TextNode(chunks[i], "link", chunks[i+1])
                    new_nodes.append(new_node)
                    i+=2
    return new_nodes

def text_to_text_nodes(text):
    nodes = [TextNode(text, "text")]
    nodes = split_nodes_delimiter(nodes, "**", "bold")
    nodes = split_nodes_delimiter(nodes, "_", "italic")
    nodes = split_nodes_delimiter(nodes, "`", "code")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes
    
