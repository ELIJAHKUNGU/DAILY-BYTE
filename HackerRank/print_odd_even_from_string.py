

# Task
# Given a string, S, of length N that is indexed from 0 to N – 1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.




# s = "Helllo world"

# odd_string = []
# even_string = []
# len_string = len(s)
# # for i in range(len(s)):
# #     if(i% 2 == 0):
# #         even_string.append(i)
# #     else:
# #         odd_string.append(i)

# for i in s:
#     if(s.index())



# Given an array, A, of N integers, print A‘s elements in reverse order as a single line of space-separated numbers.
# 4
# 1 4 3 2
# https://www.codingbroz.com/day-7-arrays-solution/

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print (*arr[::-1], sep=' ')