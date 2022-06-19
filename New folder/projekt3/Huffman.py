import PQHeap
from Element import Element


class Huffman:
    def __init__(self, C):
        
        #Save frequencyTabel for later
        self.frequencyTable = C
        
        #Use frequencytabel to make minimum heap.
        self.Q = []
        for i in range(len(C)):
            e = Element(C[i], i)
            PQHeap.insert(self.Q, e)

        #gemerate tree
        self.root = self.build_huffman_tree()
       

    def build_huffman_tree(self):
        for i in range(len(self.Q)-1):
            z = Element()
            z.left = PQHeap.extractMin(self.Q)
            z.right = PQHeap.extractMin(self.Q)
            z.key = z.left.key + z.right.key
            PQHeap.insert(self.Q, z)
        return PQHeap.extractMin(self.Q)

    def get_huffman_code_table(self):
        code_table = [0 for x in range(256)]
        self.fill_huffcode_table(self.root, code_table)
        return code_table

    def fill_huffcode_table(self, x, code_table,  code="", leftOrRight=""):
        
        newcode = code+leftOrRight

        #Element overloads __eq__, we therefor cant write x != None, but we can check if x is an instance of Element and therefor not None.
        if isinstance(x,Element): 
            
            if isinstance(x.left,Element):
               self.fill_huffcode_table(x.left,code_table,newcode,'0')
            
            if isinstance(x.right,Element):
               self.fill_huffcode_table(x.right,code_table,newcode,'1')

            if not isinstance(x.right,Element) and not isinstance(x.left,Element):
                code_table[x.data] = newcode
        
  
                

























                
    # def printRoute(self, code, root, path):
    #     if not isinstance(root, Element):
    #         return

    #     # append this node to the path array
    #     code.append(path)
    #     if not isinstance(root.left, Element) and not isinstance(root.left, Element):

    #         # print out all of its
    #         # root - to - leaf
    #         self.code_table[root.data] = ''.join([str(i) for i in code])

    #     # otherwise try both subtrees
    #     self.printRoute(code, root.left, '0')
    #     self.printRoute(code, root.right, '1')
    #     code.pop()