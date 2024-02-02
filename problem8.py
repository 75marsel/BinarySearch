# Link: https://leetcode.com/submissions/detail/1160178677/

""" 
Find First and Last Position of Element in Sorted Array
Submission Detail
88 / 88 test cases passed.
Status: Accepted
Runtime: 63 ms
Memory Usage: 17.9 MB
"""

class Solution(object):
    def searchRange(self, nums: list[int], target: int) -> list[int]:
            size = len(nums)
            l, h = 0, size - 1
            pos = []

            while l <= h:
                mid = (l+h) // 2

                if nums[mid] == target:
                    temp = mid
                    while temp >= 0:
                        if nums[temp] == target and temp != 0:
                            temp -= 1
                        else:
                            pos.append(temp+1 if nums[temp] != target else temp)
                            break
                    temp = mid
                    while temp < size:
                        if nums[temp] == target and temp != 0 and temp+1 < size:
                            temp += 1
                        else:
                            if nums[temp] != target:
                              temp -= 1
                            elif temp+1 < size:
                              if nums[temp+1] == target:
                                temp += 1
                            
                            pos.append(temp)
                            break
                    return pos

                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    h = mid - 1
                
            return [-1, -1]