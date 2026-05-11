class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        left = 0
        max_operations = float('inf')
        while left <= len(blocks) - k:
            operations =0
            for right in range(left,left+k):
                if blocks[right] == 'W':
                    operations = operations + 1
            max_operations = min(operations,max_operations)
            left = left + 1
        return max_operations
 


        