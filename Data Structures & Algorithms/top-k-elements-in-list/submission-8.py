class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqs = {}
        
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1

        freq_lst = [[] for _ in range(len(nums)+1)]

        for num, freq in freqs.items():
            freq_lst[freq].append(num)

        lst = []
        
        for i in range(len(freq_lst)-1, -1, -1):
            for num in freq_lst[i]:
                lst.append(num)
                if len(lst) == k:
                    return lst


   