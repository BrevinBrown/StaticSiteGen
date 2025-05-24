from textnode import *
def main():
    test = TextNode("test",TextType.NORMAL)
    print(test.__repr__())
    test2 = TextNode("tet",TextType.NORMAL)
    print(test == test2)
main()