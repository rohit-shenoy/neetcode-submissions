class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Validation / early exit
        if len(stones) == 1:
            return stones[0]
        
        negativeStones = [stones[i] * -1 for i in range(len(stones))]
        heapq.heapify(negativeStones)
        # [-8, -7, -4, -2, -1, -1]

        # How many steps: until 1 stone or 0 stones
        # Do what?
        while len(negativeStones) > 1:
            stoneA = heapq.heappop(negativeStones) * -1
            stoneB = heapq.heappop(negativeStones) * -1

            if stoneA == stoneB:
                continue
            else:
                diff = stoneA - stoneB if stoneA > stoneB else stoneA - stoneB
                heapq.heappush(negativeStones, diff * -1)

        # At end return 
        return negativeStones[0] * -1 if len(negativeStones) == 1 else 0