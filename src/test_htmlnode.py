import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", 
            "this is a test node", 
            props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')   

    def test_children(self):
        node = HTMLNode("p", 
            "this is a test node", 
            props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p",
            "this is test node 2",
            node)
        self.assertIs(node2.children,node)

    def test_repr(self):
        node = HTMLNode("p", 
            "this is a test node", 
            props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p",
            "this is test node 2",
            node)
        self.assertEqual(node.__repr__(), "HTMLNode(tag: p, value: this is a test node, children: None, props: {'href': 'https://www.google.com', 'target': '_blank'})")
        self.assertEqual(node2.__repr__(), "HTMLNode(tag: p, value: this is test node 2, children: HTMLNode(tag: p, value: this is a test node, children: None, props: {'href': 'https://www.google.com', 'target': '_blank'}), props: None)")
      