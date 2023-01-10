# Given an array of integers, nums, and a value k, 
# return the maximum average value from any contiguous subarray of size
#  k in nums.

# Ex: Given the following nums and k…

# nums = [4, -1, 4, 2], k = 2, return 3.0 ((4 + 2) / 2 = 3.0).
# Ex: Given the following nums and k…

# nums = [5, 1, -3, 5, 2], k = 3, return 1.33.


def maximum_average (arr, k):
    count_elements = 0
    max_average = 0 
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if k == 2 :
                if ((arr[i] + arr[j ])) > max_average:
                    max_average  =( (arr[i] + arr[j] ) / k)
            elif k == 3 :
                for h in range(j+1 , len(arr)):
                    if ((arr[i] + arr[j] + arr[h])) > max_average:
                        max_average  =( (arr[i] + arr[j] + arr[h] ) / k)

    return print(round( max_average, 2))

    


if __name__ == "__main__":
    maximum_average(arr = [4, -1, 4, 2], k = 2)
    maximum_average(arr = [5, 1, -3, 5, 2], k = 3)