class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        items = {}
        n = len(nums)
        majority = None
        for x in nums:

            items[x] = items.get(x, 0) + 1

        for key, value in items.items():

            if items[key] > n//2:
                majority = key
        
        return majority
        