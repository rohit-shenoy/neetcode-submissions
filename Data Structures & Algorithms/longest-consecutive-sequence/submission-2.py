class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        unique = set(nums)

        for idx, num in enumerate(nums):
            current_length = 1
            # check if its the start of sequence
            if (num - 1) not in unique:
                val = num
                while (val + 1) in unique:
                    current_length += 1
                    val += 1
                longest = max(longest, current_length)
        return longest

