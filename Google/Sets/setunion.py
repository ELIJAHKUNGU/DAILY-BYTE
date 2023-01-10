# Given three integer arrays, nums1, nums2, and nums3, 
# sorted in ascending order, return a list containing all 
# integers that are common to all three arrays.
# Note: There are no duplicate values in any of the arrays.

# Ex: Given the following nums1, nums2, and nums3…

# nums1 = [1, 2, 3], nums2 = [1, 2], nums3 = [1], return [1].
# Ex: Given the following nums1, nums2, and nums3…

# nums1 = [4, 5, 6], nums2 = [7, 8, 9], nums3 = [10], return [].
def set_union(nums1, nums2, nums3):
    return print(list(set(nums1) & set(nums2) & set(nums3)))
    # INTERSECTION takes in a list of sets and returns a set of elements 
    # that are common to all the sets.
    # return list(set(nums1).intersection(set(nums2), set(nums3)))
    # return print(list(set(nums1).intersection(set(nums2), set(nums3))))
if __name__ == "__main__":
    set_union(nums1 = [1, 2, 3], nums2 = [1, 2], nums3 = [1])
    set_union(nums1 = [4, 5, 6], nums2 = [7, 8, 9], nums3 = [10])