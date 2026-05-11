class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        right = 0
        max_freq = 0 
        total = 0
        while right < len(nums):
            total = total + nums[right]
            while (nums[right] * (right - left + 1) - total) > k:
                total = total - nums[left]
                left = left+1
            max_freq = max(max_freq, right - left + 1)
            right = right+1
        return max_freq



