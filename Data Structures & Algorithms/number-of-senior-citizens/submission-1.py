class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for d in details:
            ten = ord(d[11]) - ord('0')
            one = ord(d[12]) - ord('0')
            age = 10 * ten + one
            if age > 60:
                res += 1
        return res