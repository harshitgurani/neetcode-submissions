class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for number in nums:
            if number in seen:
                seen[number]+=1
            else:
                seen[number]=1
        for number , frequency in seen.items():
            if frequency >= len(nums)//2:
                return number

        