from enum import Enum 

class TextType(Enum):
    NORMAL = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"


class TextNode():
    def __init__(text,text_type,url=None):
        self.text = text
        self.text_type 
        self.url = url