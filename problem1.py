# Link: https://leetcode.com/submissions/detail/1158422571/

"""
Count Pairs Whose Sum is Less than Target
Submission Detail
707 / 707 test cases passed.
Status: Accepted
Runtime: 51 ms
Memory Usage: 16.6 MB
"""

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # binary search works well with sorted
        nums.sort()
        # length of array
        n = len(nums)
        l, h = 0, n - 1 # get low and high
        count = 0 # to store the total counts

        while l < h:
            if nums[l] + nums[h] < target:
                # since we knew the highest number we can subtract with current nums[l] then
                # we can assume that numbers before it can be subtracted to nums[l]
                count = count + (h - l)

                # since we already used the current nums[l] add 1 index to try the next index
                # we dont reset the high index as we already know the fact that any number added
                # to it is higher than the target
                l += 1
            else:
                # this will be executed if the number added to the lower results in > target
                # down size the array
                h -= 1
        
        # return the result of counting if the l is >= h 
        return count