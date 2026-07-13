from abc import get_cache_token
class Solution:
    def getKth(self, a: List[int], b: List[int], k: int) -> int:
        if len(a) > len(b):
            return self.getKth(b, a, k) # always keep as 'a' the shorter one
        if not a:
            return b[k - 1]
        if k == 1:
            return min(a[0], b[0])
        
        i = min(len(a), k // 2)
        j = min(len(b), k // 2)

        if a[i - 1] > b[j - 1]:
            return self.getKth(a, b[j:], k - j)
        else:
            return self.getKth(a[i:], b, k - i)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        left = (total + 1) // 2
        right = (total + 2) // 2
        return (self.getKth(nums1, nums2, left) + self.getKth(nums1, nums2, right)) / 2.0

