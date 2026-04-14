class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        print(k)

        def change_pos(nums, l, r):
            l, r = l, r
            while l < r:
                num1, num2 = nums[l], nums[r]
                nums[l], nums[r] = num2, num1
                l, r = l + 1, r - 1
        change_pos(nums,0 , len(nums)-1)
        change_pos(nums, 0, k-1)
        change_pos(nums, k, len(nums)-1) 

            

                


                     
