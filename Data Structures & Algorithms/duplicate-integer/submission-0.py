class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # iterate sequentially, keep a dict for O1 lookups,
        numbers_seen = dict()
        for num in nums:
            if num in numbers_seen.keys():
                return True
            # not there
            numbers_seen[num] = "True"
        return False