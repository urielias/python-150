from typing import List

"""
1. Create two pointers (p1, p2). Set one at the start of the array and the other to the end.
2. Loop while the pointers don't meet. In each iteration:
   3. Check if the element in p2 is val. If so, move p2 to the left and continue to next
   iteration.
   4. Check if the element in p1 is val. If so, swap the elements in p1 and p2 and move p2 to
   the left.
   5. Move p1 to the left.
6. Return p1
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1, p2 = 0, len(nums) - 1
        while p1 < p2:
            if (nums[p2] == val):
                p2 -= 1
                continue
            if (nums[p1] == val):
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            p1 += 1
        return p1
