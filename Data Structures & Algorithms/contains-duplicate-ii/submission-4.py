class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False

        seen = {}

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                if abs(i-seen[nums[i]])<=k:
                    return True
                seen[nums[i]] = i
        return False
