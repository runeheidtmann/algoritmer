############################################################
#
#    Authors
#    -------
#    Rune Heidtmann, ruhei08@student.sdu.dk
#    Lauge Løvig Thomassen, lthom19@student.sdu.dk
#
###########################################################

import PQHeap
from AlteredElement import Element


class Huffman:
    """
    A class used to Huffman encoding and decoding. Utilizes different datastructures to do so.

    ...

    Attributes
    ----------
    frequencyTable : List
        List that holds frequencies of each byte in original input file.
    Q : PQHeap
        Minimum heap used to generate Huffman tree.
    Root: Element
        Root of generated huffman tree.

    Methods
    -------
    buildHuffmanTree()
        Generates a Huffman-tree corresponding to optimal code in a bottom up manner.
        Runs in O(n * log n) time, since for every entry in C it does 1*extractMin + 0.5*insert both running log n time. 
    
    getHuffmanCodeTable(self):
        Gets a table with generated huffman codes, that each repressent the new codes(series of bits) for each (old)byte.
    
    fillHuffCodeTable(self, x, codeTable,  code="", leftOrRight="")
        Recursive method similar to inorder() for binary trees. 
        It recurses down to each leaf, holding a code-string that is recording the path down the tree.
                
        Runs in O(n) time. Since after the inital call, the method calls itself twice for each node.

    """
    
    def __init__(self, C):
        
        #Save frequencyTabel for later
        self.frequencyTable = C
        
        #Use frequencytabel to make minimum heap of elements.
        self.Q = []
        for i in range(len(C)):
            e = Element(C[i], i)
            PQHeap.insert(self.Q, e)

        #generate tree
        self.root = self.buildHuffmanTree()
       

    def buildHuffmanTree(self):
        """
        Returns the root of created huffman tree.

        """
        for i in range(len(self.Q)-1):
            z = Element()
            z.left = PQHeap.extractMin(self.Q)
            z.right = PQHeap.extractMin(self.Q)
            z.key = z.left.key + z.right.key
            PQHeap.insert(self.Q, z)
        return PQHeap.extractMin(self.Q)

    def getHuffmanCodeTable(self):
        """
        Returns a list of generated huffman codes.

        """
        codeTable = [0 for x in range(256)]
        self.fillHuffCodeTable(self.root, codeTable)
        return codeTable

    def fillHuffCodeTable(self, x, codeTable,  code="", leftOrRight=""):
        """
        Returns list of huffmancodes.

        Parameters
        ----------
        x : Element, required
            A node in the tree
        
        codeTable : list, required
            A list that holds the generated huffman codes.

        code : string, required
            A string that hold the current code. A code is completed at a tree leaf.

        leftOrRight : string, required
            If we walked left in the tree, we record 0 to the code. If right we record 1.

        """
        
        newcode = code+leftOrRight

        #Element overloads __eq__, we therefor cant write x != None, but we can check if x is an instance of Element and therefor not None.
        if isinstance(x,Element): 
            
            if isinstance(x.left,Element):
               self.fillHuffCodeTable(x.left,codeTable,newcode,'0')
            
            if isinstance(x.right,Element):
               self.fillHuffCodeTable(x.right,codeTable,newcode,'1')

            if not isinstance(x.right,Element) and not isinstance(x.left,Element):
                codeTable[x.data] = newcode