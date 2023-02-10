# Given an integer array, nums, return the total number of integers within nums 
# that have an even number of digits.

# Ex: Given the following nums…

# nums = [1, 12, 123], return 1 (12 is the only integer with an even number of digits).
# Ex: Given the following nums…

# nums = [1, 32, 3492, 23], return 3.

def integer_digits_arr(nums):
    count = 0
    for num in nums:
        # print(num)
        converting_digit_String = str(num)

        
        if len(converting_digit_String) % 2 == 0 :
            count += 1

    return print(count)

# Using the list Compression

def integer_digits_arr_compression(nums):
    return  print(len([num for num in nums if len(str(num)) % 2 ==0  ]) )

if __name__ == "__main__":
    integer_digits_arr([1, 12, 123])
    integer_digits_arr([1, 32, 3492, 23])
    integer_digits_arr_compression([1, 32, 3492, 23])
    integer_digits_arr_compression([1, 12, 123])

