class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        seen = {}
        fruit_count = 0
        max_fruit_count = 0
        while right<len(fruits):
            if fruits[right] in seen:
                seen[fruits[right]]+=1
            else:
                seen[fruits[right]]=1
            while len(seen) > 2:
                seen[fruits[left]] = seen[fruits[left]] - 1
                if seen[fruits[left]] == 0:
                    del seen[fruits[left]]
                left = left + 1
            fruit_count = right - left + 1
            max_fruit_count = max(max_fruit_count,fruit_count)
            right = right + 1
        return max_fruit_count
            

            



        