from typing import List

"""
1. If array length is 1, return 0.
2. Create two pointers and set them to 1.
3. Loop while p1 is lower than the array length. In each iteration:
   4. Check if the element in p1 and the element before it are different. If so,
   set the element in p2 to the element in p1 and move p2 to the right.
   5. Move p1 to the right
6. Return p2
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0

        p1, p2 = 1, 1
        while p1 < len(nums):
            if (nums[p1] != nums[p1 - 1]):
                nums[p2] = nums[p1]
                p2 += 1
            p1 += 1
        return p2
