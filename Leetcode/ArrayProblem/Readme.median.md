python
def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
Here, m and n are the lengths of the two input arrays nums1 and nums2, respectively.

    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
This line of code checks if m is greater than n, and if so, it swaps the two arrays so that nums1 is always the shorter array. This optimization is based on the idea that the binary search algorithm is more efficient when searching a smaller array.

    imin, imax, half_len = 0, m, (m + n + 1) // 2
imin and imax are the lower and upper bounds for the binary search. half_len is the half length of the combined array, rounded up if the total number of elements is odd.


    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
Here, i is the partition point for nums1, and j is the partition point for nums2. The partition points are calculated based on the half length of the combined array.


        if i < m and nums2[j-1] > nums1[i]:
            imin = i + 1
This line of code checks if i is too small, i.e., the partition point for nums1 is too far to the left. If this is the case, then the partition point must be increased, so imin is set to i + 1.


        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
This line of code checks if i is too big, i.e., the partition point for nums1 is too far to the right. If this is the case, then the partition point must be decreased, so imax is set to i - 1.

        else:
            if i == 0: max_of_left = nums2[j-1]
            elif j == 0: max_of_left = nums1[i-1]
            else: max_of_left = max(nums1[i-1], nums2[j-1])
Here, the maximum element on the left side of the partition is calculated. If i is 0, meaning that the partition point for nums1 is at the beginning of the array, then max_of_left is set to the last element on the left side of the partition in nums2. Similarly, if j is 0, meaning that the partition point for nums2 is at the beginning of the array, then max_of_left is set to the last element on the left side of the partition in nums1. Otherwise, max_of_left is set to the maximum of the last elements on the left side of the partition in both arrays.

``