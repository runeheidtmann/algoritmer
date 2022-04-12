import sys
from DictBinTree import DictBinTree,Node

# Init empty dictionary
# Constructor acts as createEmptyDict()
ordered_dict = DictBinTree()

# Read inputs and insert into tree
for line in sys.stdin:
    ordered_dict.insert(int(line))

# Get ordered list from dictionary
for key in ordered_dict.orderedTraversal():
    print(key)
