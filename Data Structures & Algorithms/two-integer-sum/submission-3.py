class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        differences = {}

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference not in differences.keys():
                differences[nums[i]] = i
            else:
                return [differences[difference], i]