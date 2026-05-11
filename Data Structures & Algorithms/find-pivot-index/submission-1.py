class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sum_arr = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = sum_arr - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            else:
                leftSum+=nums[i]
        return -1

            

        