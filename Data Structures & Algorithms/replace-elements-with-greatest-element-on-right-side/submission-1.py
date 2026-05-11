class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)-1):
            maxx = 0
            for j in range(i+1 ,len(arr)):
                if arr[j]>maxx:
                    maxx = arr[j]
            arr[i] = maxx
            maxx = 0
        arr[-1] = -1
        return arr


                
        