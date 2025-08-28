from markdown_blocks import markdown_to_html_node
from htmlnode import *
import os

def extract_title(markdown):
    lines = markdown.splitlines()
    if not lines:
        raise Exception("No header found")

    first_line = lines[0]

    if not first_line.startswith("# "):
        raise Exception("No header found")
    
    header_title = first_line[1:]
    header_title = header_title.strip()
    return header_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    entries_list = os.listdir(dir_path_content)
    for element in entries_list:
        full_path = os.path.join(dir_path_content, element)
        if os.path.isfile(full_path):
            if element[-3:] == ".md":
                generate_page(full_path, template_path, os.path.join(dest_dir_path, element[:-3] + ".html"), basepath)
        elif os.path.isdir(full_path):
            generate_pages_recursive(full_path, template_path, os.path.join(dest_dir_path, element), basepath)
        else:
            raise Exception("Not a file or directory")