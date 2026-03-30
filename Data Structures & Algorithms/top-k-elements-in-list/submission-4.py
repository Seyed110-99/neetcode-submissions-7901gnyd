class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        repeats = {}

        bucket = [[] for _ in range(len(nums) + 1)]
        
        final = []
        for num in nums:
            
            repeats[num] = repeats.get(num, 0) + 1


        for key, value in repeats.items():

            bucket[value].append(key)
        print(bucket)
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                final.append(num)
                if len(final) == k:
                    return final
