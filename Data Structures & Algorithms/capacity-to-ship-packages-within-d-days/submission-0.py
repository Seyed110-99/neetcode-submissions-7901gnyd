class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        r = sum(weights)

        while l<=r:

            mid = (l+r)//2

            carry_weight = 0
            day = 1

            for weight in weights:
                
                if weight + carry_weight <= mid:
                    carry_weight += weight
                    
                else:
                    day += 1
                    carry_weight = weight

            if day > days:
                l = mid + 1
            else:
                ans = mid
                r = mid - 1
        
        return ans
                    
