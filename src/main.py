from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is a link", TextType.LINK, "http://www.boots.dev")
    print(text_node)

main()