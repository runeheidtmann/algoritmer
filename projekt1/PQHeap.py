def createEmptyPQ():
    return []
    
def parent( i):
    return (i - 1) // 2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def minHeapify(A, i): 
    l = left(i)
    r = right(i)

    if l <= len(A)-1 and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    
    if  r <= len(A)-1 and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        return minHeapify(A,smallest)
    return A

def buildMinHeap(A):
    size = len(A)
    for i in range(size//2-1,-1,-1):
        A = minHeapify(A,i)
    return A

def extractMin(A):
    min = A[0]
    A[0] = A[len(A)-1]
    A.pop()
    A = minHeapify(A,0)
    return min

def insert(A,key):
    A.append(key)
    i = len(A)-1
    
    while i > 0 and A[parent(i)] > A[i]:
        temp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = temp
        i = parent(i)

    return A