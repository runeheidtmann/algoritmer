import PQHeap
import HeapVisualizer
pq = PQHeap.createEmptyPQ()

n = 0
with open('./projekttest/mixed.txt') as f:
    for line in f.readlines():
        PQHeap.insert(pq,int(line))
        #HeapVisualizer.heap_visualizer(pq)
        #print(n)

        n = n+1
    
    print()
    while n > 0:
        print(PQHeap.extractMin(pq))
        #HeapVisualizer.heap_visualizer(pq)
        #print(n)
        n = n-1

