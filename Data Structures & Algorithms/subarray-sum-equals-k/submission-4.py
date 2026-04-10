class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixes = {0:1}

        prefix = 0
        res = 0 
  

        for num in nums: 
            prefix += num
            needed = prefix - k

            res += prefixes.get(needed, 0)

            prefixes[prefix] = prefixes.get(prefix, 0) + 1

        return res
        