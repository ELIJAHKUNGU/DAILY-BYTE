items  = []
for i in range(0,366):
    items.append(i)
   

SumOf = sum(items)
print(SumOf)
    
# Add all numbers from 0 to 365 and print the result.

def sumOfNumbers(n):
    # explain = "Add all numbers from 0 to " + str(n) + " and print the result."
    if n == 0:
        return 0
    # explain the code here why n-1 is used
    # it is because the function is recursive and it will keep calling itself until it reaches the base case
    # the base case is when n is equal to 0

    return n + sumOfNumbers(n-1)
    
print(sumOfNumbers(365))


