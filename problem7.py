# Link: https://leetcode.com/submissions/detail/1159316470/

"""
Count Negative Numbers in a Sorted Matrix
Submission Detail
44 / 44 test cases passed.
Status: Accepted
Runtime: 101 ms
Memory Usage: 17.7 MB
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        
        for g in grid:
            size = len(g)
            l, h = 0, size-1
            
            while l <= h:
                mid = (l+h) // 2

                if g[mid] < 0:
                    if g[mid-1] < 0 and not (mid-1) < 0:
                        l = mid - 1
                        h -= 1
                    else:
                        count += (size - mid)
                        break

                else:
                    l = mid + 1
        
        return count