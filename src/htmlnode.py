
class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children_nodes: list["HTMLNode"] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children_nodes
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is not None:
            html_props = ""
            for key, value in self.props.items():
                html_props += f' {key}="{value}"'
            return html_props
        return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")

        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children_nodes: list, props: dict[str, str] | None = None):
        super().__init__(tag, None, children_nodes, props)
        self.tag = tag
        self.childrens = children_nodes
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parentnode must have a tag")

        if self.childrens is None:
            raise ValueError("Error need HTML child node")

        child_html = ""
        for child in self.childrens:
            child_html += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>'

    def __repr__(self):
        return f'ParentNode({self.tag}, {self.childrens}, {self.props})'