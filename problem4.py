# Link: https://leetcode.com/submissions/detail/1159133725/

"""
Binary Search
Submission Detail
47 / 47 test cases passed.
Status: Accepted
Runtime: 187 ms
Memory Usage: 18.1 MB
"""
    
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return -1