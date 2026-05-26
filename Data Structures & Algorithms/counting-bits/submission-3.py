class Solution:
    def countBits(self, n: int) -> List[int]:
        ''' res = []
        for num in range(n+1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        return res '''

        ''' res = [0] * (n + 1)
        for i in range(1, n + 1):
            num = i
            while num != 0:
                res[i] += 1
                num &= (num - 1)
        return res '''

        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp