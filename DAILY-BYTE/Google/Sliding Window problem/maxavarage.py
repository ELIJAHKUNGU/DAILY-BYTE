# Given an array of integers, nums, and a value k, 
# return the maximum average value from any contiguous subarray of size
#  k in nums.

# Ex: Given the following nums and k…

# nums = [4, -1, 4, 2], k = 2, return 3.0 ((4 + 2) / 2 = 3.0).
# Ex: Given the following nums and k…

# nums = [5, 1, -3, 5, 2], k = 3, return 1.33.


# One way to solve this problem is to use a sliding window approach. 
# You can start by initializing a variable to store the current sum of
# the first k elements of the array, and then iterate through the array
# starting from the kth element. At each step, you can calculate the 
# average of the current subarray of size k by subtracting the first
# element of the subarray from the current sum, and then dividing by k. 
# You can also update the current sum by adding the current element and
# subtracting the first element of the subarray. Keep track of the
# maximum average seen so far, and return it at the end.


def max_average(nums, k):
    current_sum = sum(nums[:k])
    max_average = current_sum / k
    
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        current_average = current_sum / k
        max_average = max(max_average, current_average)
    
    return print(max_average)


if __name__ == "__main__":
    max_average(nums = [5, 1, -3, 5, 2], k = 3)
    max_average(nums = [4, -1, 4, 2], k = 2)
