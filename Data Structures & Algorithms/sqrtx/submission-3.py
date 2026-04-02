class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        r = x
        sqrt = 0
        while l<=r:

            mid = (l+r)//2
            print(mid)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                sqrt = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return r