class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        flag = False
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(i - seen[nums[i]])<=k:
                    flag = True
                seen[nums[i]]=i
            else:
                seen[nums[i]]=i
        return flag

        
            






