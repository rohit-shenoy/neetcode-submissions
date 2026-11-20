class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # solution space for k - rate can't be zero
        l, r = 1, max(piles)
        result = r  # minimize it

        while l <= r:
            k = l + ((r - l) // 2)

            hours_needed = 0
            # check if this rate is enough
            for p in piles:
                hours_needed += math.ceil(p / k)

            if hours_needed <= h:
                result = min(result, k)
                # even smaller k?
                r = k - 1
            else:
                l = k + 1

        return result