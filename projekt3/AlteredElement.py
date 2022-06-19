from functools import total_ordering

@total_ordering
class Element:
    """
    Elements used to store data and frequency of data.
    
    Functionality added by Rune og Lauge:
        Elements are also used as nodes in a binary Huffman tree
    ...

    Attributes
    ----------
    key : int
        If Element is the root or a leaf in a binary tree, key describes the frequency of its data.
    data : int
        Whole number representing a byte. E.g. If data is text data = 97 = a
    left: Element
        Left child of node element in a binary tree.
    Right: Element
        Right child of node element in a binary tree.

    """
    def __init__(self,key = None, data = None):
        self.key = key
        self.data = data
        
        #Added by Rune og Lauge
        self.left = None
        self.right = None

    def __eq__(self,other):
        return self.key == other.key

    def __lt__(self,other):
        return self.key < other.key

