############################################################
#
#    Authors
#    -------
#    Rune Heidtmann, ruhei08@student.sdu.dk
#    Lauge Løvig Thomassen, lthom19@student.sdu.dk
#
###########################################################


import sys
from DictBinTree import DictBinTree

# Init empty dictionary
# Constructor acts as createEmptyDict()
ordered_dict = DictBinTree()

# Read inputs and insert into tree1
for line in sys.stdin:
    ordered_dict.insert(int(line))

# Get ordered list from dictionary
for key in ordered_dict.orderedTraversal():
    print(key)
