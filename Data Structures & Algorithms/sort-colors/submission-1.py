class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        mid = 1

        while j <= k:

            num1 = nums[j]
            num2 = nums[i] 
            num3 = nums[k]

            if nums[j] < mid:
                nums[j] = num2
                nums[i] = num1
                i += 1
                j += 1

            elif nums[j] > mid:
                nums[j] = num3
                nums[k] = num1
                k -= 1

            else:
                j += 1
            
            
        
        