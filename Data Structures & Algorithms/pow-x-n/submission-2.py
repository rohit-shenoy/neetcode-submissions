class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        if n == 0:
            return 1.0
        half = self.myPow(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x