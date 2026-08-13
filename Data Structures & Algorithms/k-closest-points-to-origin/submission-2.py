class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for x in points:
            distance = - math.sqrt(x[0] ** 2 + x[1] ** 2)
            heapq.heappush(maxHeap, [distance, x[0], x[1]])
            print([distance, x[0], x[1]])

            while len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [[y[1], y[2]] for y in maxHeap]