class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        if not nums:
            return 0
        longest = 1 
        
        for num in nums:
            if num - 1 not in nums:
                count = 1
                next_num = num + 1
                while next_num in nums:
                    count += 1
                    next_num += 1
                    if longest < count:
                        longest = count

        return longest



            