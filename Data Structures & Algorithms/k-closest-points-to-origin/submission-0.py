import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def getDistance(x, y) -> float:
            return math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    
        distances = [(getDistance(x, y), x, y) for x,y in points] # Dist, x , y
        # Orders using first 
        heapq.heapify(distances)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1
        return res
