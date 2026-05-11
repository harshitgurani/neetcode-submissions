class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start = 0
        # max_water = 0
        # while start < len(heights)-1:
        #     for i in range(start+1,len(heights)):
        #         water = (i-start)*min(heights[start],heights[i])
        #         max_water = max(max_water,water)
        #     start = start+ 1
        # return max_water

        left,right = 0,len(heights)-1
        max_water = 0

        while left < right : 
            water = (right-left)* min(heights[left],heights[right])
            max_water = max(max_water,water)
            if heights[left]>heights[right]:
                right = right -1
            else:
                left = left + 1
        return max_water


        