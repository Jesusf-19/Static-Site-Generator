import os
from blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 heading found!")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()

    with open(template_path, "r") as file:
        template = file.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html)

    destination = os.path.dirname(dest_path)

    if destination:
        os.makedirs(destination, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(full_html)