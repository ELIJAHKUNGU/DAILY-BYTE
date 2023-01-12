# Given an array nums. We define a running sum of an array as
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
import itertools

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         ans = [0] * len(nums)
#         ans[0] = nums[0]
#         for i in range(1, len(nums)):
#             ans[i] = ans[i-1] + nums[i]
#         return ans

def iter_sum(nums):
    return print(list(itertools.accumulate(nums)))


if __name__ == "__main__":
    iter_sum([1,2,3,4])

