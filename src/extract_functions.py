import re

def extract_markdown_images(markdown):
    matches = re.findall(r"!\[(.*?)\)", markdown)
    output = []
    for match in matches:
        temp = tuple(match.split("]("))
        output.append(temp)
    return output

def extract_markdown_links(markdown):
    matches = re.findall(r"\[(.*?)\)", markdown)
    output = []
    for match in matches:
        temp = tuple(match.split("]("))
        output.append(temp)
    return output