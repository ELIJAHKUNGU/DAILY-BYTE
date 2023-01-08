# Given an array, A, of N integers, print A‘s elements
#  in reverse order as a single line of space-separated numbers.
# 4
# 1 4 3 2
# https://www.codingbroz.com/day-7-arrays-solution/
def reverseArray(a):
    return print(a[::-1])

def print_array_reverse(a):
    # a = [1, 4, 3, 2]
    for i in range(len(a)-1, -1, -1):
        print(a[i], end=" ")
    print("")
    return


def print_array_reverse2(a):
    # a = [1, 4, 3, 2]
    for i in a:
        reverse = a[::-1]
    for i in reverse:
        print(i, end=" ")

    print("")
    return


def print_array_reverse3(a):
    # a = [1, 4, 3, 2]
    for i in a[::-1]:
        print(i, end=" ")
    # what is purpose of this line a[::-1] ? it is because
    #it loops through the array in reverse order
    print("")
    return

# Find the maximum sum array
def find_max(arr):
    arr = [1, 2, 3, 4, 5]
    max_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            max_sum = max(max_sum, sum)
    print(max_sum)
    return
   
# Find the maximum sum array
def find_max2(arr):
    arr = [1, 2, 3, 4, 5]
    print(sum(arr))
    return
    # expected output: 15

# sum any two numbers in an array and return the max sum and  print the numbers we sum to get the max sum
def sum_two_numbers(array):
    # array = [21,22, 13, 44, 5]
    max_sum = 0
    num1 = 0
    num2 = 0
    for i in range(len(array)):
        # why do we need to start at i+1?
        # because we don't want to add the same number to itself what does to do prevent that?
        print("i: ", i)
        # range (len(array) returns the length of the array which is 
        for j in range(i+1, len(array)):
            # range (i+1, len(array)) returns the length of the array which is 
            if array[i] + array[j] > max_sum:
                max_sum = array[i] + array[j]
                num1 = array[i]
                num2 = array[j]
    return print("The max sum is: ", max_sum, " and the numbers are: ", num1, " and ", num2)




if __name__ == '__main__':
    reverseArray([1, 4, 3, 2])
    sum_two_numbers([21,22, 13, 44, 5])


