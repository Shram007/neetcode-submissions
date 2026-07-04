class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}
        for c in chars:
            count[c] = 1 + count.get(c, 0)
        
        res = 0
        for w in words:
            cur_word = defaultdict(int)
            good = True
            for c in w:
                cur_word[c] += 1
                if cur_word[c] > count.get(c, 0):
                    good = False
                    break
            if good:
                res += len(w)
        return res