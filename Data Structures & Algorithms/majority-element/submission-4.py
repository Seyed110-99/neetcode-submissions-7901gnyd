class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res = None
        count = 0

        for n in nums:

            if count == 0:
                res = n
                count += 1

            elif n == res:
                count += 1

            else:
                count -= 1
            print(res, count)
        return res
        