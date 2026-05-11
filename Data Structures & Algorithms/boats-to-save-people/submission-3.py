class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right = 0,len(people)-1
        counter = 0
        boat = 0
        for weight in people:
            if weight == limit:
                counter+=1
                boat+=1
        while left < right:
            if people[left] + people[right] <= limit:
                counter+=2
                boat+=1
                left+=1
                right -= 1
            else:
                right -= 1
        return boat+len(people)-counter


        






        