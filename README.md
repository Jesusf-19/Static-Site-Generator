# Static-Site-Generator

A static site generator built from scratch using Python. This project converts Markdown content into structured HTML and prepares static assets for a website.

This project focuses on Python fundamentals, object-oriented programming, recursion, file handling, Markdown parsing, and automated testing.

## Project Overview

The goal of this project is to build a static site generator without relying on existing Markdown-to-HTML conversion libraries.

The generator processes Markdown text, identifies its formatting and structure, converts it into HTML nodes, and produces HTML output.

The project is being developed incrementally, with each component tested before integration.

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

**Current development milestone**

The project is being extended to manage static website assets.

The static-file copying functionality is designed to:

- Copy files from `static/` to `public/`.
- Recursively process nested directories.
- Preserve the original directory structure.
- Remove previously generated content before copying.
- Log copied files for debugging.

The `public/` directory is excluded from version control because its contents can be regenerated.

## Project Structure

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
| `public/` | Generated website files |
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

## Getting Started

### Prerequisites

- Python 3 installed
- Git installed
- A terminal or development environment such as WSL

### Clone the Repository

Clone the repository using its GitHub URL:

`git clone <repository-url>`

Navigate into the project directory:

`cd static-site-gen`

### Run the Application

From the project root, execute:

`./main.sh`

During the static-file copying stage, this command prepares the `public/` directory and copies the contents of `static/`.

### Run Unit Tests

Execute:

`./test.sh`

This runs the Python unit tests using the `unittest` framework.

The tests cover TextNode behavior, HTML generation, Markdown parsing, block classification, and Markdown-to-HTML conversion.

## Example Markdown Conversion

**Input Markdown:**

`This is **bold** text with an _italic_ word.`

**Generated HTML:**

`<div><p>This is <b>bold</b> text with an <i>italic</i> word.</p></div>`

The generator uses nested HTML nodes to construct the output instead of directly manipulating HTML strings throughout the parsing process.

## Development Progress

**Completed components:**

- TextNode representation and conversion
- HTMLNode class hierarchy
- Inline Markdown parsing
- Markdown block identification
- Markdown-to-HTML node conversion
- Unit tests for parsing and HTML generation

**Current focus:**

- Recursive static asset copying
- Integration with `main.py`

**Upcoming development:**

- Generating HTML pages from Markdown files
- Integrating HTML templates
- Building a complete static website
- Finalizing the project documentation

## What I Learned

This project has provided practical experience with:

- Object-oriented programming and class inheritance
- Recursive functions and tree structures
- String manipulation and regular expressions
- File and directory management
- Modular software design
- Unit testing and debugging
- Breaking complex problems into smaller reusable functions
- Integrating independently developed components into a larger application

## Project Status

**In Development**

The Markdown parsing and HTML conversion components have been implemented. Development is continuing toward a complete static site generator capable of generating a website from Markdown source files.

## Acknowledgments

Built as part of the [Boot.dev](https://www.boot.dev/) curriculum to strengthen Python programming, software engineering, and backend development skills.