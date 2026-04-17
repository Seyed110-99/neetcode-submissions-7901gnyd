class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        

        for r in range(len(nums)):
            l = 0
            while l < r:
                if nums[l] == nums[r] and abs(l-r) <= k:
                    return True
                else:
                    l += 1
        return False

        
        