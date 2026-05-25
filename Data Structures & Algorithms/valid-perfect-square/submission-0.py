class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right = 0,num

        while left <= right :
            mid = left + (right-left)//2
            sq_num = mid*mid
            if sq_num == num:
                return True
            elif sq_num > num:
                right = mid -1
            else:
                left = mid + 1
        return False