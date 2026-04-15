class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_mix = []
        nums.sort()
        target = 0
        print(nums)

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l<r:
                add = nums[i] + nums[l] + nums[r]

                if add > target:
                    r -= 1
                elif add < target:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in nums_mix:
                        nums_mix.append([nums[i], nums[l], nums[r]])
                        l += 1
                    else:
                        l += 1
                    
            
                    
        return nums_mix