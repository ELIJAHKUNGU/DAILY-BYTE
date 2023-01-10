# Given a string, sequence, and a word to search for,
#  return the total number of times that word can be repeated a
# nd still exist as a substring within sequence.

# Ex: Given the following sequence and word…

# sequence = "abcabcab", word = "abc", return 2 ("abcabc" exists within our 
# sequence but "abcabcabc" does not).
# Ex: Given the following sequence and word…

# sequence = "ccc", word = "c", return 3.

# def substring_check (sequence,word ):
#     count = 0 
#     if word in sequence:
#         for word in sequence:
#             count += 1
#         print(count)
# Not efficient
import re
def repeat_count(sequence, word):
    # re.finditer(pattern, string)
    itr = re.finditer(word, sequence)
    #  I have simply converted the iterable object from finditer 
    # to a list and returned its length, which gives total number of matches of word in sequence
    print(len(list()))
    return 

# Method 2 This approach is simple and efficient, but it does not work for overlapping instances of the word,
# for example for example sequence = "abcabcabc" and word = "abc" it will return 1.# For handling overlapping
# instances, you could use python's re module's finditer() function, this will return all the match object of 
# the word in the sequence and you can count it.

def substring_check(sequence, word):
    count = 0
    while word in sequence:
        count += 1
        sequence = sequence.replace(word, "", 1)
    return print( count)
# Check the strig , indexs
def extra_method():
    text = "cat in the hat, cat on the mat"
    for match in re.finditer("cat", text):
        print(match.group(), match.start(), match.end())
if __name__ == "__main__":
    substring_check(sequence= 'ccc', word='c')
    # sequence = "abcabcab", word = "abc", return 2
    repeat_count( sequence = "abcabcab", word = "abc")


# NOTES 
# pattern is a regular expression that defines the search pattern.
# string is the input string to search for the pattern.
# The finditer() function returns an iterator object, 
# which you can use in a for loop to iterate over all the matches.
#  Each match object has several useful methods 
# that you can use to extract information about the match, like group() which returns the matched ""string""
# and start() and end() which returns the starting and ending index of the match respectively.

# Here is an example of using finditer() to search for all occurrences of the word "cat" in a string:

# import re
# text = "cat in the hat, cat on the mat"
# for match in re.finditer("cat", text):
#     print(match.group(), match.start(), match.end())

# output 
# string from group, start index and end index
# cat 0 3
# cat 18 21

