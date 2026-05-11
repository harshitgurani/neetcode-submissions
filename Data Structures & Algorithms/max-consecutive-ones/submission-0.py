class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        counter = 0
        i=j=0
        while j < len(nums):
                if nums[j] == 1:
                    j+=1
                    counter+=1
                else:
                    i = j
                    j+=1
                    maxx = max(maxx,counter)
                    counter = 0
        return max(maxx,counter)
        
                
            

        