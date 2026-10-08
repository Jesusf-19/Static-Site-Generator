from enum import Enum
from htmlnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnodes, text_to_children

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    blocks = []
    for block in split_blocks:
        block = block.strip()
        if block != "":
            blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block: str) -> BlockType:
    # Heading
    for i in range(1,7):
        if block.startswith("#" * i + " "):
            return BlockType.HEADING

    # Code
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    lines = block.split("\n")

    # Quote
    is_quote = True
    
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break

    if is_quote == True:
        return BlockType.QUOTE

    # Unordered List
    is_unordered_list = True

    for line in lines:
        if not line.startswith("- "):
            is_unordered_list = False
            break
    if is_unordered_list == True:
        return BlockType.UNORDERED_LIST

    # Ordered List
    is_ordered_list = True
    for i, line in enumerate(lines):
        expected = f"{i + 1}. "
        if not line.startswith(expected):
            is_ordered_list = False
            break

    if is_ordered_list == True:
        return BlockType.ORDERED_LIST

    # If everything doesn't pass, then it must be a paragraph
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks_of_markdown = markdown_to_blocks(markdown)
    children = []
    for block in blocks_of_markdown:
        block_type = block_to_block_type(block)

        # For paragraph block types
        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            node = ParentNode("p", text_to_children(text))
            children.append(node)

        # For heading block types
        elif block_type == BlockType.HEADING:
            heading_level = 0

            for char in block:
                if char == "#":
                    heading_level += 1
                else:
                    break

            text = block[heading_level + 1:]
            tag = f"h{heading_level}"
            node = ParentNode(tag, text_to_children(text))
            children.append(node)

        # For Quote block types
        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            quote_lines = []

            # Removes the ">" from quote lines
            for line in lines:
                quote_lines.append(line.lstrip(">").strip())

            #Rejoins the list into full text
            text = " ".join(quote_lines)
            node = ParentNode("blockquote", text_to_children(text))
            children.append(node)


        # For unordered lists block types
        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            # Remove the "-" from every line
            for line in lines:
                text = line[2:]
                item = ParentNode("li", text_to_children(text))
                list_items.append(item)

            node = ParentNode("ul", list_items)
            children.append(node)


        # For ordered lists block types
        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []

            # Removes the number list and ". "
            for line in lines:
                text = line.split(". ", 1)[1]
                item = ParentNode("li", text_to_children(text))
                list_items.append(item)

            node = ParentNode("ol", list_items)
            children.append(node)

        # For code block types
        elif block_type == BlockType.CODE:
            text = block[4:-3]
            if not text.endswith("\n"):
                text += "\n"

            text_node = TextNode(text, TextType.TEXT)
            code_leaf = text_node_to_html_node(text_node)

            code_node = ParentNode("code", [code_leaf])
            node = ParentNode("pre", [code_node])
            children.append(node)
    return ParentNode("div", children)



        