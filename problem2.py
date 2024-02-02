# Link: https://leetcode.com/submissions/detail/1158448454/

"""
Sqrt(x)
Submission Detail
1017 / 1017 test cases passed.
Status: Accepted
Runtime: 42 ms
Memory Usage: 16.3 MB
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x

        while l <= h:
            # get the middle value of the given number starting from 0
            mid = (l + h) // 2
            # multiply itself 
            ans = mid * mid 
            
            # if the ans is <= x 
            # then move right from left side starting from the current middle
            if ans <= x:
                l = mid + 1
            else:
                # else we knew that the range is too large based from square 
                h = mid - 1

        return h