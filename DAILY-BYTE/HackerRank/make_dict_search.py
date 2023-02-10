# # The first line contains an integer, n, denoting the number of entries in the phone book.
# # Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line. The first value is a friend’s name, and the second value is an 8-digit phone number.

# # After the n lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a name to look up, and you must continue reading lines until there is no more input.

# # Note: Names consist of lowercase English alphabetic letters and are first names only.

# Query 0: sam
# Sam is one of the keys in our dictionary, so we print sam=99912222.

# Query 1: edward
# Edward is not one of the keys in our dictionary, so we print Not found.

# Query 2: harry
# Harry is one of the keys in our dictionary, so we print harry=12299933.

import sys 

# Read input and assemble Phone Book
n = int(input())
phoneBook = {}
for i in range(n):
    contact = input().split(' ')
    phoneBook[contact[0]] = contact[1]

# Process Queries
lines = sys.stdin.readlines()
for i in lines:
    name = i.strip()
    if name in phoneBook:
        print(name + '=' + str( phoneBook[name] ))
    else:
        print('Not found')