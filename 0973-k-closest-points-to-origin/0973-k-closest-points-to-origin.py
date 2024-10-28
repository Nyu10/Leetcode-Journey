import queue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for (x, y) in points:
            distance = -(x * x + y * y)  # Store negative distance for max-heap simulation
            heapq.heappush(max_heap, (distance, [x, y]))
            
            # Maintain a heap size of k
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the k closest points from the heap
        return [point for (_, point) in max_heap]
        