# Given an array, nums, every value appears twice except for one which only appears once. The value that only appears once is the lucky number. Return the lucky number.

# Ex: Given the following nums…

# nums = [1, 2, 1], return 2.
# Ex: Given the following nums…

# nums = [1, 3, 1, 2, 2], return 3.

def double_numbercheck(nums):
    count = 0
    current_value = nums[:1]
   
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
               if  nums[i] == nums[j]:
                    count += 1
                    print("NUMS", nums[i], "Compare", nums[j])
               else:
                current_notrepeated = nums[i]
    print(current_notrepeated)

    


if __name__ == "__main__":
    double_numbercheck([1, 3, 1, 2, 2])

                


