from math import log2
from math import ceil

A = [x for x in range(1,2**5)]

k = log2(len(A))+1

j = 0
i = int(j/2)
spaces = int(k)
m = int(k)

while j < int(k):
    start = int((2**m)/2)-1
    print(" "*start,end='')
    while i < 2**(j+1)-1:
        print(A[i],end ='')   
        i = i + 1 
        print(" "*2**(int(k)-(int(k)-m)), end='')
    j = j+1
    m = m-1
    print("")
    