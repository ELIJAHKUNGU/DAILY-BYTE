# Given a string, s, return the length of the longest 
# substring that only contains one unique character.
# Note: s is non-empty and it is guaranteed there is 
# a single answer.

# Ex: Given the following string s…

# s = "aabc", return 2 ("aa" is length 2).
# Ex: Given the following string s…

# s = "abcabbccabccc", return 3.


def longest_string(strings):
    current_count = 1
    max_count = 1
    current_string = strings[0]
    for s in range(1, len(strings)):
        if  strings[s] == current_string:
            current_count += 1
        else:
            current_count = 1
            strings[s]
            max_count = max(max_count, current_count)
            


    return  print(max_count)


if __name__ == "__main__":
    longest_string("aabc")


