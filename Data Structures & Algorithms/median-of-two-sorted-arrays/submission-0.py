class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self._find_kth_num(nums1, nums2, (len1 + len2) // 2 + 1)
        else:
            small = self._find_kth_num(nums1, nums2, (len1 + len2) // 2)
            big = self._find_kth_num(nums1, nums2, (len1 + len2) // 2 + 1)
            return (small + big) / 2

    def _find_kth_num(self, nums1, nums2, k):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self._find_kth_num(nums2, nums1, k)
        if len1 == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        part1 = min(k // 2, len1)
        part2 = k - part1
        if nums1[part1-1] <= nums2[part2-1]:
            return self._find_kth_num(nums1[part1:], nums2, k-part1)
        else:
            return self._find_kth_num(nums1, nums2[part2:], k-part2)
