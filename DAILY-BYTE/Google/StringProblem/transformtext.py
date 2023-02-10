# You are typing on a computer when all of a sudden you realize
# you’ve been typing with caps lock on. Given a string s, 
#return a new string containing all of its alphabetical character
#transformed to lowercase.
# Note: Do you not use an built in library functions.

# Ex: Given the following string s…

# s = "ABC", return "abc".
# Ex: Given the following string s…

# s = "ABCa", return "abca".

def text_transform(s):
    res = ''
    for char in s:
        if ord(char) >= 65 and ord(char) < 90:

            res += chr (ord(char) + 32)
        else:
            res += char
    return print(res)


if __name__ == "__main__":
    text_transform('ABC')