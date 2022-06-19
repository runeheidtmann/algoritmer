# Helper function for the deletion method.
# It rotates nodes in a manner corresponding to the deletion-case.
def transplant(self,u,v):
    if u.parent == None:
        self.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent

# Callable method for deleting nodes in the tree.
# It has four cases.
def delete(self,z):
    if z.left == None:              #Case 1
        self.transplant(z,z.right)
    elif z.right == None:           # Case 2
        self.transplant(z,z.left)
    else:                           
        y = self.minimum(z.right)
        
        if y.parent != z:               # Case 3
            self.transplant(y,y.right)
            y.right = z.right
            y.right.parent = y
        
        self.transplant(z,y)           # Case 4
        y.left = z.left
        y.left.parent = y

# Recursive method that returns the minimum of a tree.
# In the book the algorithm is described iteratively.
# Exercise 12.2-2 is to write a recursive version of it:
def minimum(self, x):
    if x.left == None:
        return x
    return self.minimum(x.left)