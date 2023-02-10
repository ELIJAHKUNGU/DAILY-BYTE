# Given a non-negative integer array, nums, return the maximum product you can create with two separate indices i and j.
# Note: You may assume the product will not overflow.

# Ex: Given the following nums…

# nums = [4, 2, 5, 3], return 20 (5 * 4).
# Ex: Given the following nums…

# nums = [6, 2, 4, 3], return 24.


def max_array(nums):
   
    max_total = 0

    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            product = nums[i] * nums[j]
            max_total = max(max_total, product)

    return print(max_total)


if __name__ == "__main__":
    max_array([6, 2, 4, 3])



