class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        shift = 0
        smallest_num = None
        while l<r:
            mid = (l+r)//2
            
            print("index", l, mid, r)
            print("Nums", nums[l], nums[mid], nums[r])

            if nums[mid] > nums[r]:
                l = mid + 1
                
            else:
                r = mid 

        return nums[l]
