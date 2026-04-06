class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        l = len(nums)
        ans = [0] * 2 * l
        for z in range(2*len(nums)):
            if z >= l:
                ans[z] = nums[z-l]
            else:
                ans[z] = nums[z]
        return ans