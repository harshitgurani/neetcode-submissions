class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest_map = {}
        for i in range(len(nums2)):
            next_greatest_map[nums2[i]] = -1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    next_greatest_map[nums2[i]] = nums2[j]
                    break
                else:
                    continue
        result = []
        for number in nums1:
            result.append(next_greatest_map[number])
        return result
            

        