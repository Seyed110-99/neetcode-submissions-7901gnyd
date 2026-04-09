class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_r = [[]for _ in range(len(nums))]
        num = 1
        for i in range(len(nums)):
            l_r[i] = num
            num *= nums[i]

        print(l_r)

        r_l = [[]for _ in range(len(nums))]
        num = 1
        for i in range(len(nums)-1, -1, -1):
            r_l[i] = num
            num *= nums[i]
        
        print(r_l)
        res = []

        for i in range(len(nums)):
            res.append(r_l[i]*l_r[i])


        return res

            