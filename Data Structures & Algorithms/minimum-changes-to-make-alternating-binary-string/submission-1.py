class Solution:
    def minOperations(self, s: str) -> int:
        cur = cnt1 = 0
        for c in s:
            if int(c) != cur:
                cnt1 += 1
            cur ^= 1
        
        cur = 1
        cnt0 = 0
        for c in s:
            if int(c) != cur:
                cnt0 += 1
            cur ^= 1
        return min(cnt0, cnt1)