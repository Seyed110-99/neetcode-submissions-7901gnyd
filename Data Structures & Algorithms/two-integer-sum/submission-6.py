class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differences = defaultdict(list)

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference in differences.keys():
                return [differences[difference], i]

            else:
                differences[nums[i]] = i

    


            
        
                
            

