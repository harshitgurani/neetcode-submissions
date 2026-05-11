class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')
        window_sum = 0
        for i in range(len(blocks[:k])):
            if blocks[i]=='B':
                window_sum = window_sum + 1
        min_operations = min(min_operations,(k-window_sum))

        for i in range(k,len(blocks)):
            if blocks[i] == 'B':
                window_sum = window_sum + 1
            if blocks[i-k] == 'B':
                window_sum = window_sum -1 

            min_operations = min(min_operations,(k-window_sum))
        return min_operations



            


 


        