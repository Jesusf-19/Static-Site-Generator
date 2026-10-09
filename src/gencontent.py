import os
from blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 heading found!")

def generate_page(from_path, template_path, dest_path, basepath):
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

    # Adjust root-relative URLs for GitHub Pages
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    destination = os.path.dirname(dest_path)

    if destination:
        os.makedirs(destination, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, item)
        destintation_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(source_path):
            if source_path.endswith(".md"):
                destintation_path = os.path.splitext(destintation_path)[0] + ".html"

                generate_page(source_path, template_path, destintation_path, basepath)
        else:
            os.makedirs(destintation_path, exist_ok=True)
            generate_pages_recursive(source_path, template_path, destintation_path, basepath)

    