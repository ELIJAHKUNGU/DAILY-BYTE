def power_set(s):
    if len(s) == 0:
        return [[]]
    else:
        # EXPLANATION OF THE CODE
        # power_set(s[1:]) = [[], [2], [3], [2, 3]]
        # power_Ser(s[1:]) this does not include the first element of the list
        #  but includes the rest of the elements of the list
        # x for x in power_set(s[1:]) = [[], [2], [3], [2, 3]]
        #  [[s[0]] + x for x in power_set(s[1:])] why square brackets because we are adding a list to a list 
        return power_set(s[1:]) + [[s[0]] + x for x in power_set(s[1:])]

# SIMPLE FORMULA FOR POWER SET
def power_seT(s):
    # Explanation of the code 
    # s[i] for i in range(len(s)) if (j & (1 << i))] for j in range(2**len(s))
    # s[i] for i in range(len(s)) = [1, 2, 3]
    # if (j & (1 << i))] for j in range(2**len(s)) = [1, 2, 3]
    # if (j & (1 << i)) it checks if the bit is set or not

    return    [[s[i] for i in range(len(s)) if (j & (1 << i))] for j in range(2**len(s))]


if __name__ == "__main__":
    print(power_set([1, 2, 3]))
    print(power_seT([1, 2, 3]))
