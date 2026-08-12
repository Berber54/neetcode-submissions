class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            one = heapq.heappop(maxHeap)
            two = heapq.heappop(maxHeap)
            if one == two:
                continue
            else:
                heapq.heappush(maxHeap, one - two)
        
        return 0 if not maxHeap else -maxHeap[-1]