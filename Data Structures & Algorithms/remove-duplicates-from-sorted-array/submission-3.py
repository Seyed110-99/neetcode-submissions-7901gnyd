class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 1
        write = 1

        while i < len(nums):

            j = i - 1 

            if nums[i] != nums[j]:
                nums[write] = nums[i]
                write += 1
                print(i, j, write)
            i += 1

        return write
      
                

            
