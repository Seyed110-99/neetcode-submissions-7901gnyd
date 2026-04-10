class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        if not nums:
            return 0
        longest = 1 
        
        for num in nums:
            next_num = num + 1
            count = 1
            while next_num in nums:
                count += 1
                next_num += 1
                if longest < count:
                    longest = count

        return longest



            