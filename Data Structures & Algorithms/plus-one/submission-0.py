class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join([str(d) for d in digits])) + 1
        return [int(s) for s in str(num)]