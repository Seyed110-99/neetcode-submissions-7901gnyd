class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        no_dup = set()

        for num in nums:
            no_dup.add(num)

        no_dup = list(no_dup)
        no_dup.sort()
        
        for i in range(len(no_dup)):
            nums[i] = no_dup[i]

        return(len(no_dup)) 
      
                

            
