"""'
MEDIAN OF TWO SORTED ARRAYS
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

'"""
import itertools


def findMedianSortedArrays(nums1, nums2):
    all_arr = []
    combined_arr = itertools.chain(nums1, nums2)
    # sort_Arr = combined_arr.sort()
    # print(sort_Arr)
    for i in combined_arr:
        all_arr.append(i)

#    sort
    sorted_arr = sorted(all_arr)
    median = int(len(sorted_arr) / 2)
    print(median)

    if (median % 2 != 0):
        print(sorted_arr[median])
    else:
        # print(sorted_arr[median-1],  sorted_arr[median])

        median = (sorted_arr[median-1] + sorted_arr[median]) / 2

        print(median)


def findMedianSortedArrays1(nums1, nums2):
    all_arr = []
    for i in nums1:
        all_arr.append(i)
    for j in nums2:
        all_arr.append(j)

    print(sorted(all_arr))
    sorted_all_arr = sorted(all_arr)
    arr_median = int(len(sorted_all_arr)/2)

    if arr_median % 2 != 0:
        print(sorted_all_arr[arr_median])
    else:
        arr_median = (sorted_all_arr[arr_median] +
                      sorted_all_arr[arr_median] + 1) / 2
        print(arr_median)


def findMedianSortedArraysTwo(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j-1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
        else:
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])
            if (m + n) % 2 == 1:
                return max_of_left
            if i == m: min_of_right = nums2[j]
            elif j == n: min_of_right = nums1[i]
            else: min_of_right = min(nums1[i], nums2[j])
            return (max_of_left + min_of_right) / 2.0



if __name__ == "__main__":
    findMedianSortedArrays1([1, 3], nums2=[2, 10])
