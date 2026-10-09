# Static-Site-Generator

A static site generator built from scratch using Python. This project converts Markdown content into structured HTML and prepares static assets for a multi-page website that can be published with GitHub Pages.

This project focuses on Python fundamentals, object-oriented programming, recursion, file handling, Markdown parsing, and automated testing.

## Project Overview

The project was developed incrementally, with each component tested before integration. The completed generator supports recursive Markdown-to-HTML conversion, automatic page generation, static asset management, and deployment through GitHub Pages.

## Live Website

**[View the
website](https://Jesusf-19.github.io/Static-Site-Generator/)**

## Website Preview

![Static Site Generator Homepage](screenshots/homepage.png)


## Project Structure

``` text
static-site-gen/
├── content/
│   ├── index.md
│   ├── blog/
│   │   ├── glorfindel/index.md
│   │   ├── tom/index.md
│   │   └── majesty/index.md
│   └── contact/index.md
├── static/
│   ├── index.css
│   └── images/
├── docs/                  # Generated website, committed for GitHub Pages
├── src/
│   ├── main.py
│   ├── gencontent.py
│   ├── blocks.py
│   ├── inline_markdown.py
│   ├── htmlnode.py
│   ├── textnode.py
│   └── test_*.py
├── template.html
├── main.sh
├── build.sh
├── test.sh
└── README.md
```

## Features Implemented

### 1. TextNode System

Implemented a `TextNode` class to represent different types of inline Markdown content.

Supported text types:

- Plain text
- Bold text
- Italic text
- Inline code
- Hyperlinks
- Images

Each TextNode stores its text, type, and an optional URL for links or images.

### 2. HTMLNode System

Implemented an object-oriented HTML representation using three classes:

- `HTMLNode` — Base class for HTML elements.
- `LeafNode` — Represents HTML elements without child nodes.
- `ParentNode` — Represents HTML elements containing other HTML nodes.

The system supports HTML attributes, nested elements, and recursive HTML generation through the `to_html()` method.

### 3. Inline Markdown Parsing

Created functions that identify and convert inline Markdown formatting into TextNodes.

Implemented functionality includes:

- Splitting text using Markdown delimiters.
- Extracting Markdown images and links using regular expressions.
- Converting Markdown images into image TextNodes.
- Converting Markdown links into link TextNodes.
- Processing multiple formatting types in a single string.

The `text_to_textnodes()` function combines these operations into a single conversion pipeline.

### 4. Markdown Block Parsing

Implemented `markdown_to_blocks()` to separate Markdown documents into individual blocks.

Created a `BlockType` enumeration and a `block_to_block_type()` function to classify blocks.

Supported block types:

| Markdown Type | HTML Element |
|---|---|
| Paragraph | `<p>` |
| Heading | `<h1>` through `<h6>` |
| Code block | `<pre><code>` |
| Quote | `<blockquote>` |
| Unordered list | `<ul><li>` |
| Ordered list | `<ol><li>` |

### 5. Markdown to HTML Conversion

Implemented `markdown_to_html_node()` to convert Markdown documents into nested HTML nodes.

The conversion process:

1. Splits Markdown into individual blocks.
2. Determines the type of each block.
3. Creates the corresponding HTML parent nodes.
4. Converts inline Markdown into child HTML nodes.
5. Combines all blocks under a single `<div>` parent node.

Code blocks are handled separately to preserve their original content without applying inline Markdown formatting.

### 6. Static File Management
Implemented recursive static file copying to prepare website assets for deployment.

The generator:

- Copy files from `static/` to `docs/`.
- Recursively process nested directories.
- Preserve the original directory structure.
- Remove previously generated content before copying.
- Log copied files for debugging.

The docs/ directory contains the generated website and is committed to GitHub for deployment through GitHub Pages.

## Project Structure Explanation

The project is organized around separate modules for parsing, HTML generation, and testing.

| File or Directory | Purpose |
|---|---|
| `src/main.py` | Main application entry point |
| `src/textnode.py` | TextNode class and HTML conversion |
| `src/htmlnode.py` | HTMLNode, LeafNode, and ParentNode classes |
| `src/inline_markdown.py` | Inline Markdown parsing |
| `src/blocks.py` | Markdown block splitting and classification |
| `src/test_*.py` | Unit tests for project components |
| `static/` | Original website assets |
| `docs/` | Generated website files published through GitHub Pages |
| `main.sh` | Runs the application |
| `test.sh` | Runs the unit tests |
| `.gitignore` | Excludes generated and temporary files |

## Technologies Used

- **Python 3** — Primary programming language
- **HTML** — Generated webpage structure
- **CSS** — Website styling
- **Python unittest** — Automated testing
- **Regular Expressions** — Markdown link and image extraction
- **Git and GitHub** — Version control
- **Linux / WSL** — Development environment

No third-party Markdown parser is required.

## Getting Started

### Prerequisites

- Python 3 installed
- Git installed
- A terminal or development environment such as WSL

## How It Works

1.  `main.py` cleans and rebuilds the output directory (`docs/`).
2.  The static asset copier copies the contents of `static/` into
    `docs/`.
3.  `generate_pages_recursive()` walks through every subdirectory of
    `content/`.
4.  For each `.md` file, `generate_page()`:
    -   Reads the Markdown and HTML template.
    -   Converts Markdown into HTML using `markdown_to_html_node()`.
    -   Extracts the page's H1 heading using `extract_title()`.
    -   Replaces the template's title and content placeholders.
    -   Adjusts root-relative image and link URLs for the selected base
        path.
    -   Writes the generated `.html` file into the matching location
        under `docs/`.

For example:

``` text
content/blog/tom/index.md
            ↓
docs/blog/tom/index.html
```

## Run Locally

**Requirements:** Python 3, Git, and a terminal with Bash.

Clone the repository and navigate into it:

``` bash
git clone https://github.com/Jesusf-19/Static-Site-Generator.git
cd Static-Site-Generator
```

Start the local website:

``` bash
./main.sh
```

Open **http://localhost:8888/** in your browser.

The script generates the site using `/` as the base path, then starts
Python's built-in HTTP server. Press `Ctrl+C` to stop the server.

If a script isn't executable, run `chmod +x main.sh build.sh test.sh`.

## Build for GitHub Pages

Run:

``` bash
./build.sh
```

This generates the production website in `docs/`, using
`/Static-Site-Generator/` as the base path.

The GitHub Pages publishing settings are:

-   **Source:** Deploy from a branch
-   **Branch:** `main`
-   **Folder:** `/docs`

Because GitHub Pages publishes the generated files, the `docs/`
directory is committed to the repository. Run `./build.sh` before
committing any new production changes, especially after running the
local development script.

## Run Tests

``` bash
./test.sh
```

The unit tests exercise the HTML node classes, Markdown parsing, block
classification, title extraction, and HTML generation.

## Example

**Markdown input:**

``` md
# My First Page

This is a **bold** word and an _italic_ word.

- First item
- Second item
```

**Generated content:**

``` html
<div><h1>My First Page</h1><p>This is a <b>bold</b> word and an <i>italic</i> word.</p><ul><li>First item</li><li>Second item</li></ul></div>
```

The generated content is inserted into the HTML template to create a
full webpage.

## What I Learned

Building this project strengthened my understanding of:

-   Object-oriented programming, inheritance, and recursive tree
    structures
-   Recursive directory traversal and file-system operations
-   Regular expressions and text parsing
-   Unit testing and debugging
-   Separating parsing, rendering, and file generation into reusable
    modules
-   Building and deploying a multi-page static website

## Acknowledgments

Built as part of the [Boot.dev](https://www.boot.dev/) curriculum to strengthen Python programming, software engineering, and backend development skills.