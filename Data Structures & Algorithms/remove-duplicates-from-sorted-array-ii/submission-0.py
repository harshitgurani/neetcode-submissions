class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        k = 2   # allow at most 2 duplicates
        
        while right < len(nums):
            
            # new number starts → reset k
            if right == 0 or nums[right] != nums[right - 1]:
                k = 2
            
            # only write if we still have quota
            if k > 0:
                nums[left] = nums[right]
                left += 1
                k -= 1
            
            right += 1
        return left
        
