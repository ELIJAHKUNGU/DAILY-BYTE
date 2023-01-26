# Given an array, nums, every value appears twice except for one which only appears once. The value that only appears once is the lucky number. Return the lucky number.

# Ex: Given the following nums…

# nums = [1, 2, 1], return 2.
# Ex: Given the following nums…

# nums = [1, 3, 1, 2, 2], return 3.

# 
# One way to solve this problem is to use the XOR operator.
#  The XOR operator returns 1 if the bits being compared are different, and 0
# if they are the same. If we XOR all the elements in the array together, the 
# result will be the lucky number, because every other value will be XORed with
# itself, resulting in 0, and the lucky number will be XORed with 0, resulting in the lucky number.

from collections import Counter
def double_numbercheck(nums):
   lucky_no = 0
   for num in nums:
    lucky_no ^= num
   return print(lucky_no)
        
   
# Second method
def find_luckyNo(nums):
    count = Counter(nums)

    for key, value in count.items():
        if value == 1:
            return print(key)
    

if __name__ == "__main__":
    double_numbercheck([1, 3, 1, 2, 2])
    find_luckyNo([1, 3, 1, 2, 2])

                


