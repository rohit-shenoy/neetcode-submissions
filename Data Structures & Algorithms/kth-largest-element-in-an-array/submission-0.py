class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minHeap of size k
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        # exactly k elements
        return nums[0]
        