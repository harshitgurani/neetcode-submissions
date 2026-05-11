class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        max_water = 0
        while start < len(heights)-1:
            for i in range(start+1,len(heights)):
                water = (i-start)*min(heights[start],heights[i])
                max_water = max(max_water,water)
            start = start+ 1
        return max_water

        