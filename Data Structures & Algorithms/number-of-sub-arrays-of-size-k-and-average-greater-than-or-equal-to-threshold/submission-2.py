class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sum_window = sum(arr[:k])
        window_avg = sum_window/k
        if window_avg>=threshold:
            count+=1


        for i in range(k,len(arr)):
            sum_window = sum_window + arr[i]
            sum_window = sum_window - arr[i-k]
            window_avg = sum_window/k
            if window_avg>=threshold:
                count+=1
        return count

            




        
