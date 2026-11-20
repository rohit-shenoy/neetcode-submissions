class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        # retain only k elements - minHeap of size k exactly
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # only pop if more than k
        if len(self.minHeap) > self.k:
             heapq.heappop(self.minHeap)

        # now exactly k, so return min of it (thats kth largest)
        return self.minHeap[0]
