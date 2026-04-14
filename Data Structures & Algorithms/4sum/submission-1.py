class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 1):

            for j in range(i, len(nums) - 1):
                if j == i:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l<r and i != j != l != r:

                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res_loc = [nums[i], nums[j], nums[l], nums[r]]
                        if res_loc not in res:
                            res.append(res_loc)
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1

                    else:
                        r -= 1

        return res

            
