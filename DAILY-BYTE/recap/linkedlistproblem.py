# str = 'ABC, x, 3d ,efg ,%x,e, $~'
# a python program to get reverse the string without affecting special characters
def reverse(str):
    # split the string into a list
    str = list(str)
    # initialize the left and right pointers
    r = len(str) - 1
    l = 0
    # loop till the left pointer crosses the right pointer
    while l < r:
        # if the left pointer is not an alphabet
        if not str[l].isalpha():
            l += 1
        # if the right pointer is not an alphabet
        elif not str[r].isalpha():
            r -= 1
        # if both the pointers are alphabets
        else:
            str[l], str[r] = str[r], str[l]
            l += 1
            r -= 1
    # join the list and return the string
    return ''.join(str)
# Driver code
if __name__ == '__main__':
    str = 'ABC, x, 3d ,efg ,%x,e, $~'
    print(reverse(str))

# Output:
# CBA, x, 3d ,gfe ,%x,e, $~

