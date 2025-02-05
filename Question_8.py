
# arr = [1,3,7,9,12,10,8,16,18,22,27]
#          Create a buildHeap method that returns a minheap and max heap.
import heapq


def heap(arr):
    min_heap =[]
    for n in arr:
        heapq.heappush(min_heap,n)

    max_heap = []
    for n in arr:
        heapq.heappush(max_heap,-n)

    print("Min Heap")
    while min_heap:
        print(heapq.heappop(min_heap),end=" ")
    print("\n")

    print("Max Heap")
    while max_heap:
        print(heapq.heappop(max_heap),end=" ")
    return ""    

arr = [1,3,7,9,12,10,8,16,18,22,27]
result = heap(arr)
print(result)

# arr = [1,3,7,9,12,10,8,16,18,22,27]
#          Create a buildHeap method that returns a minheap and max heap.
import heapq


def heap(arr):
    min_heap =[]
    for n in arr:
        heapq.heappush(min_heap,n)

    max_heap = []
    for n in arr:
        heapq.heappush(max_heap,-n)

    print("Min Heap")
    while min_heap:
        print(heapq.heappop(min_heap),end=" ")
    print("\n")

    print("Max Heap")
    while max_heap:
        print(heapq.heappop(max_heap),end=" ")
    return ""    

arr = [1,3,7,9,12,10,8,16,18,22,27]
result = heap(arr)
print(result)

