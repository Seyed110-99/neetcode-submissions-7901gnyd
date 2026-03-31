class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        window_len = float("inf")
        window_sum = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                window_sum -= nums[l]
                window_len = min(window_len, r - l + 1)
                l += 1
        if window_len == float("inf"):
            return 0
        return window_len 


        


            
            