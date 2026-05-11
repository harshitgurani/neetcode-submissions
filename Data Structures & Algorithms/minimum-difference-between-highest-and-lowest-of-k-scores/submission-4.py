class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort(reverse=False)
        print(nums)
        min_diff = float('inf')
        diff = 0
        left,right = 0 , k-1
        while right<len(nums):
            diff = nums[right]-nums[left]
            min_diff = min(min_diff,diff)
            left = left + 1
            right = right + 1
        return min_diff



        


        