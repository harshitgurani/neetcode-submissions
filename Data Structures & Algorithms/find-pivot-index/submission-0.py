class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        pivot_index = -1
        for i in range(0,len(nums)):
            if i == 0 and sum(nums)==0:
                return 0
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
            if i == len(nums)-1 and sum(nums)==0:
                return len(nums)-1
        return pivot_index
        