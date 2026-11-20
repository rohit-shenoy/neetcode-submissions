class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 1
        multiplier = 1
        for idx in range(len(digits) - 1, -1, -1):
            sum += multiplier * digits[idx]
            multiplier *= 10
        return [int(d) for d in str(sum)]