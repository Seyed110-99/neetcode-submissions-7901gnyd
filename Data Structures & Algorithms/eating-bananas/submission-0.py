class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:

            mid = (l+r)//2
            hour = 0
            
            for pile in piles:
                hour += (pile + mid - 1) // mid

            if hour <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
                

            