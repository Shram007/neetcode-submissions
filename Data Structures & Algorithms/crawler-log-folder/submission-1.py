class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for i in range(len(logs)):
            if logs[i] == '../':
                if cnt >= 1:
                    cnt -= 1
                else:
                    cnt = 0
            elif logs[i] == './':
                continue
            else:
                cnt += 1
        return cnt