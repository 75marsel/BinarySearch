# Link: https://leetcode.com/submissions/detail/1159174036/

""" 
Find Smallest Letter Greater Than Target
Submission Detail
167 / 167 test cases passed.
Status: Accepted
Runtime: 103 ms
Memory Usage: 16.8 MB
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l , h = 0, len(letters) - 1

        while l <= h:
            mid = (l + h) // 2
            
            if target < letters[mid]:
                if (target != letters[mid-1]) and (target < letters[mid-1]):
                    h = mid - 1
                else:
                    return letters[mid]
            elif target >= letters[mid]:
                l = mid + 1
                
        return letters[0]