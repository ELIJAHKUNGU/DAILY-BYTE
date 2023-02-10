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
    combined_arr = itertools.chain(nums1,nums2)
    # sort_Arr = combined_arr.sort()
    # print(sort_Arr)
    for i in combined_arr:
        all_arr.append(i)
    
#    sort
    sorted_arr =sorted(all_arr)
    median = int(len(sorted_arr) / 2)
    print(median)
   

    if (median % 2 != 0):
        print(sorted_arr[median])
    else:
        # print(sorted_arr[median-1],  sorted_arr[median])

        median = (sorted_arr[median-1] +sorted_arr[median]) / 2
        
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
        arr_median = (sorted_all_arr[arr_median] + sorted_all_arr[arr_median] +1 ) / 2
        print(arr_median)



    

if __name__ == "__main__":
    findMedianSortedArrays1([1,3], nums2 = [2, 10])

