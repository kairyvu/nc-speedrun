class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            nums1Val = nums1[i] if i >= 0 else float("-inf")
            if nums1Val >= nums2[j]:
                nums1[k] = nums1Val
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
