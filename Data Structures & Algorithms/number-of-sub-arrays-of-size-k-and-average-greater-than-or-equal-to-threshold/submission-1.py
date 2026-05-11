class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # res = 0
        # for i in range(0,len(arr)-k+1):
        #     summ = 0
        #     for j in range(i,k+i):
        #         summ+=arr[j]
        #     if summ/k >=threshold:
        #         res+=1
        # return res

        counter = 0
        summ = 0
        for i in range(0,k):
            summ+=arr[i]
        if summ/k >= threshold : 
            counter = 1

        for i in range(k,len(arr)):
             summ = summ + arr[i] - arr[i-k]
             if summ/k >= threshold: 
                counter +=1
        return counter



        
