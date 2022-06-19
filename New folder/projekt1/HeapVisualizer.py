import math
import PQHeap
def heap_visualizer(A):
  nl = len(str(max(A)))
  h = math.floor(math.log2(len(A)) + 1)
  l = int(math.pow(2,math.floor(math.log2(len(A)))))
  tl = (3 + nl) * l - 1
  i = 0
  outst = ""
  for hi in range(1,h + 1):
    outst += math.ceil(tl / int(math.pow(2,hi))) * " "
    li = 0
    while li < int(math.pow(2,(hi - 1))) and i < len(A):
      outst += "[" + (nl - len(str(A[i]))) * " " + str(A[i]) + "]"
      if li < int(math.pow(2,hi)) - 1:
        if hi < h:
          outst += (math.ceil((tl - nl - 2) / int(math.pow(2,hi - 1))) - hi + 2 - nl) * " "
        elif hi == h:
          outst += " "
      li += 1
      i += 1
    if hi < h:
      outst += "\n\n"
  print(outst)

A = [3,2,1,55,-1,-23,123,33,-23,21,23,12,13,14,-14]*2
pq = PQHeap.buildMinHeap(A)
heap_visualizer(pq)


