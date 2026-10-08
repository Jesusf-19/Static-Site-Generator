import os
import shutil
from gencontent import generate_page

def copy_recursive(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied: {source_path} -> {destination_path}")
        else:
            os.mkdir(destination_path)
            copy_recursive(source_path, destination_path)


def copy_static(source, destination):
    # Check whether the destination already exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    # Create an empty destination directory
    os.mkdir(destination)

    # Start copying files
    copy_recursive(source, destination)


def main():
    copy_static("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()