class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo
        '''
        maxSum, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum
        '''

        # Divide and Conquer Algo
        def dfs(l, r):
            if l > r: return float('-inf')

            m = (l + r) >> 1
            LeftSum = RightSum = CurSum = 0
            for i in range(m - 1, l - 1, -1):
                CurSum += nums[i]
                LeftSum = max(LeftSum, CurSum)
            
            CurSum = 0
            for i in range(m + 1, r + 1):
                CurSum += nums[i]
                RightSum = max(RightSum, CurSum)

            return (max(dfs(l, m - 1), dfs(m + 1, r), LeftSum + nums[m] + RightSum))

        return dfs(0, len(nums) - 1)