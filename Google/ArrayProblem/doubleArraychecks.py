# Given an integer array, nums, return true if for any value within 
# nums its double also exists within the array.

# Ex: Given the following nums…

# nums = [4, 3, 9, 8], return true (4 and 8 both appear in nums).
# Ex: Given the following nums…

# nums = [9, 2, 3, 5], return false.   
def double_check(nums):
    for num in nums:
        if num * 2 in nums:
            print(True)
            

if __name__ == "__main__":
    double_check([4, 3, 9, 8])