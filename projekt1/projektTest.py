import PQHeap

pq = PQHeap.createEmptyPQ()

n = 0
with open('./projekttest/positive.txt') as f:
    for line in f.readlines():
        PQHeap.insert(pq,int(line))
        n = n+1
    
    print()
    while n > 0:
        print(PQHeap.extractMin(pq))
        n = n-1

