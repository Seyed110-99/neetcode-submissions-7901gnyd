class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            
            while n >= nums[i] >= 1 and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        print(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


                