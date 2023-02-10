# Given a binary array, bits, return the maximum number of
#  contiguous ones within the array.

# Ex: Given the following bits…

# bits = [1, 0, 1, 1], return 2.
# Ex: Given the following bits…

# bits = [0, 0, 0], return 0.

# You can solve this problem by iterating through the array and
#  keeping track of the current count of contiguous ones and
#   the maximum count of contiguous ones seen so far. When a zero 
#   is encountered, reset the current count to 0. The maximum count
#  seen so far will be the maximum number of contiguous ones.

def max_contiguous_ones(bits):
    max_count = 0
    current_count = 0
    for bit in bits:
        if bit == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count



if __name__ == "__main__":
    max_contiguous_ones([1, 0, 1, 1])