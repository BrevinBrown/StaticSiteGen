from enum import Enum 

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"


class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type 
        self.url = url

    def __eq__(self,node1):
        if (node1.text == self.text and
        node1.text_type == self.text_type and
        node1.url == self.url):
            return True
        return False

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")

