from typing import List

"""
1. Use one pointer for each list (i, j), starting at their respective last position (m and n).
2. Loop through the list nums1 in reverse (use k as pointer).
3. In each iteration, check if nums2 has been traversed completely. If so, break the loop.
4. Check if nums1 has been traversed completely. If so, directly set position k in nums1 to
   nums2[j] and move j to the left.
5. If previous conditions not met, check both arrays in their current pointer position and set
   nums1[k] to bigger value, while moving used pointer to the left. 
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1

        for k in range(m + n - 1, -1, -1):
            if (j < 0):
                break
            elif (i < 0):
                nums1[k] = nums2[j]
                j -= 1
            else:
                if (nums1[i] > nums2[j]):
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
