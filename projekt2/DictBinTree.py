############################################################
#
#    Authors
#    -------
#    Rune Heidtmann, ruhei08@student.sdu.dk
#    Lauge Løvig Thomassen, lthom19@student.sdu.dk
#
###########################################################


class Node:
    """
    Node class to help represent a tree by a linked data structure
    in which each node is an object. 
    
    ...

    Attributes
    ----------
    key : int
        Key which represents data.
    left : Node
        points to node < key
    right : Node
        points to node > key
    parent : Node
        points to parent node at a higher level.
       
    """

    def __init__(self,key = None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class DictBinTree:
    """
    A class used for representing an Ordered Dictionary data structure.
    Uses a binary search tree to offer certain operations in a good running time.

    ...

    Attributes
    ----------
    root : Node
        The root in the binary searchtree
    inOrderList : List
        List of ordered keys

    Methods
    -------
    insert(key)
        Generates a new node with the inputted parameter as the key.
        Runs in O(height_of_tree) time.
    
    search()
        Returns boolean value wether a node with given key exists in tree or not.
        Runs in O(height_of_tree) time.

    inorder_tree_walk(node)
        Recursive method that walks through binary search tree and saves the ordered keys in the class attribute inOrderList.
        Runs in O(n).
    
    inorder()
        Returns a list of keys in ascending order. 
    
    """
    def __init__(self):
        self.root = None
        self.inOrderList = []
    
    def createEmptyDict():
        return DictBinTree()

    def insert(self,z):
        """
        Creates a new node with given key z and puts it in the right place in a binary search tree structure

        Parameters
        ----------
        z : int, required
            whole number functioning as key
        """
        z = Node(z)
        y = None
        x = self.root

        #Find the right place the tree.
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        
        #Weave node into thre tree structure
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def search(self,x,k):
        """
        Returns boolean value wether a given node key exists in the tree or not.

        Parameters
        ----------
        x : Node, required
            Node that tells search method in which tree/subtree to start search.
            Given the root, the method seach in the whole tree.

        k : int, required
            Key to search for.
        """
        #Base case
        if x == None:
            return False

        # Successful seach
        if k == x.key:
            return True

        # Bottom reach, seach unsuccessful
        if x.left == None and x.right == None:
            return False
   
       # recurse either left or right.
        if k < x.key:
            return self.search(x.left,k)
        else:
            return self.search(x.right,k) 
        

    def inorder_tree_walk(self, x):
        """
        Recursive method that saves tree/subtree in numerical order in internal attribute inOrderList

        Parameters
        ----------
        x : Node, required
            Node that tells method in which tree/subtree to start.
            Given the root, the method will enlist all keys in tree in ascending order.

        """
        if x != None:
            self.inorder_tree_walk(x.left)
            self.inOrderList.append(x.key)
            self.inorder_tree_walk(x.right)

    def orderedTraversal(self):

        """
        Method that returns ordered key list.
        """    
        self.inOrderList = [] # Truncate existing list if exists.
        self.inorder_tree_walk(self.root)
        return self.inOrderList