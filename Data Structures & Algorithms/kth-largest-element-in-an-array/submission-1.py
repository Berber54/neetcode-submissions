class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [n for n in nums]
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        return maxHeap[0]