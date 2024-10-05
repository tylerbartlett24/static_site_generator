import re
from markdown_to_html_node import *
import os

def extract_title(markdown):
    title = re.search(r"# (.*?)\n\n", markdown).group(0).lstrip("# ").strip()
    return title
    
def generate_page(filepath, template_path, dest_path):
    print(f"Generating page from {filepath} to {dest_path} " +
          f"using {template_path}")
    with open(filepath) as f:
        markdown = f.read()
    with open(template_path) as t:
        template = t.read()
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown).to_html()
    page = re.sub(r"{{ Title }}", title, template)
    page = re.sub(r"{{ Content }}", html, page)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    with open(dest_path, "w") as f:
        f.write(page)
        
def generate_recursively(from_dir, template_path, dest_dir):
    for file_path in os.listdir(from_dir):
        check = os.path.join(from_dir, file_path)
        if os.path.isfile(check) or os.path.islink(check):
            dest_path = os.path.join(dest_dir, file_path.rstrip("md")+"html")
            generate_page(check, template_path, dest_path)
        elif os.path.isdir(check):
            dest_path = os.path.join(dest_dir, file_path)
            generate_recursively(check, template_path, dest_path)
        else:
            raise Exception("Oh shit")
            
    
    
    