class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for i in range(n):
            cnt = 1
            j = i + 1
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                cnt += 1
            cnt = 0 if j == n else cnt
            res.append(cnt)
        return res