import math 

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # gifts[i] is positive, maxHeap with every elem * -1
        gifts = [-1 * g for g in gifts]
        heapq.heapify(gifts)

        # Edge case: len(gifts) < k
        while k > 0:
            maximum = heapq.heappop(gifts) * -1
            rooted = math.floor(math.sqrt(maximum))
            heapq.heappush(gifts, rooted * -1)
            k -= 1
        
        return sum(gifts) * -1
