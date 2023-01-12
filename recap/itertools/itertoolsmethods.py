# itertools.chain() is a function in the itertools module
#  that takes one or more iterable objects as input and 
#  returns an iterator that concatenates the elements of the input iterables. The input iterables can be any type of iterable, such as lists, tuples, strings, etc. The chain() function effectively "flattens" the input iterables into a single iterable.

# Here's an example of how you might use the itertools.
# chain() function to concatenate elements of multiple 
# lists:

import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# create an iterator that concatenates the elements of the three lists
iterator = itertools.chain(list1, list2, list3)
iterator1 = itertools.chain(*list1, *list2, *list3)

# print the concatenated elements
for i in iterator:
    print(i)
    
for j in iterator1:
    print(j) 
    # 1, 2,3, 4 -----


# 
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
def runningSum(nums):
    return list(itertools.accumulate(nums))

