class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        Sum = 0
        for i in range(1, n):
            Mod =  abs((ord(s[i]) - ord((s[i - 1]))))
            Sum += Mod
        return Sum
