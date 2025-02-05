# Find the k closest points to the origin. 
# points = [[1,3],[-2,2]]
# k=1
# output = [-2,2]

import heapq

def k_closest(points, k):
    heap = [((x**2 + y**2), [x, y]) for x, y in points]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]

points = [[1, 3], [-2, 2]]
k = 1
output = k_closest(points, k)
print(output)
