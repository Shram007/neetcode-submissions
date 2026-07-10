class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftMax , rightMax = [0] * n, [0] * n
        leftMax[0] = nums[0]
        rightMax[n - 1] = nums[n - 1]

        for i in range(1, n):
            if i % k == 0:
                leftMax[i] = nums[i]
            
            else:
                leftMax[i] = max(leftMax[i - 1], nums[i])

            j = n - 1 - i
            if (j + 1) % k == 0:
                rightMax[j] = nums[j]
            else:
                rightMax[j] = max(rightMax[j + 1], nums[j])

        res = [0] * (n - k + 1)
        for i in range(n - k + 1):
            res[i] = max(leftMax[i + k - 1], rightMax[i])
        return res