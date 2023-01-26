# "'This question is asked by Facebook. Given an array of unsorted integers,
#  return the length of its longest increasing subsequence.
# Note: You may assume the array will only contain positive numbers.'"
# nums = [1, 9, 7, 4, 7, 13] return 4



def lis(nums):
    n = len(nums)
    # Declare the list (num say) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range (1, n):
        for j in range(0, i):
            if nums[i] > nums[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
 
    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])
 
    return maximum
# end of lis function
 
# Driver program to test above function
nums = [1, 9, 7, 4, 7, 13]
print("Length of lis is", lis(nums))