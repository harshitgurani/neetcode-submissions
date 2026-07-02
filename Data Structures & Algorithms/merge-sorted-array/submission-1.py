class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n-1
        last = m+n -1

        while left+1 > 0 and right+1 > 0:
            if nums1[left] >= nums2[right]:
                nums1[last] = nums1[left]
                left = left - 1
            else:
                nums1[last] = nums2[right]
                right = right - 1
            last = last - 1
        while right+1 > 0:
            nums1[last] = nums2[right]
            right = right - 1
            last = last - 1
            



            



        