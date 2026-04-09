class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freqs = {}
        n = len(nums)

        for num in nums:

            freqs[num] = freqs.get(num, 0) + 1
        
        output = []

        for num, freq in freqs.items():
            if freq > n/3:
                output.append(num)

        return output

