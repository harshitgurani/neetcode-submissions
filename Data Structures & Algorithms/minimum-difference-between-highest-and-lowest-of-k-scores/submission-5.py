class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')
        for i in range(k-1,len(nums)):
            diff = nums[i] - nums[i-k+1]
            min_diff = min(diff,min_diff)
        return min_diff









        


        