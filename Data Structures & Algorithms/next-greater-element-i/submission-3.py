class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ''' 
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        for num in stack:
            next_greater[num] = -1
        
        return [next_greater[num] for num in nums1] 
        '''
        nums1Idx = { num : i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and stack[-1] < cur:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
        