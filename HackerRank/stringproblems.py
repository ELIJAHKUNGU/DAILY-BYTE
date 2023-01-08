

# Task
# Given a string, S, of length N that is indexed from 0 to N – 1,
# print its even-indexed and odd-indexed characters as 2
#  space-separated strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

def print_odd_even_from_string(s):
    # s = "Helllo world"

    odd_string = []
    even_string = []
    len_string = len(s)
    for i in range(len_string):
        if (i % 2 == 0):
            even_string.append(i)
        else:
            odd_string.append(i)

    print("Even string: ", even_string)
    print("Odd string: ", odd_string)

    # PRINT EVEN STRING
    for i in even_string:
        print(s[i], end="")
    print("", " ", end="")

    # PRINT ODD STRING
    for i in odd_string:
        print(s[i], end="")
    print("ODD STRING", " ", end="")
    print("")
    return





def reverse_string(s):
    # s = "Hello world"
    print(s[::-1])
    return
    


if __name__ == '__main__':
    # print_odd_even_from_string("Hello world")
    a = [1, 4, 3, 2]
    # print_array_reverse(a)
    print_array_reverse2(a)
