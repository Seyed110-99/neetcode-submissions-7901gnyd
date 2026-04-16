class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums = nums1[:m]

        i, j, k = m-1, n-1, m+n-1

        while i >= 0 and j >= 0:
            print(nums[i], nums2[j])
            if nums[i] > nums2[j]:
                nums1[k] = nums[i]
                i -= 1

            elif nums[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums[i]
                i -= 1
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

