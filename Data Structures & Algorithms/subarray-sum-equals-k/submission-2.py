class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixes = {0:1}

        prefix = 0
        res = 0 
  

        for num in nums:
            prefix += num
            sums = prefix - k

            res += prefixes.get(sums, 0)

            prefixes[prefix] = prefixes.get(prefix, 0) + 1
            
        return res
        