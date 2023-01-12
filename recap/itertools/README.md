
# ITERTOOLS
`itertools` is a module in the Python standard library that provides a variety of functions for working with iterators. These functions can be used to perform operations such as `filtering`, `mapping`, and `reducing `over the elements of an iterable. Some of the most commonly used functions in the itertools module include:

`accumulate(iterable, func=operator.add): returns an iterator` that applies the given function to the items of an input iterable, so that the cumulative sum is computed.

`chain(*iterables): returns an iterator` that concatenates the elements of the input iterables.

`groupby(iterable, keyfunc): groups the elements `of an iterable based on the result of the keyfunc function.

`permutations(iterable, r=None): returns an iterator` that generates all possible r-length permutations of the elements in the input iterable.

`product(*iterables, repeat=1): returns an iterator` that generates the Cartesian product of the input iterables.

These are just a few examples of the many functions provided by the itertools module. For more information and examples, you can refer to the official Python documentation: `https://docs.python.org/3/library/itertools.html`


### Accumulate 
You can also use the built-in `itertools.accumulate() `function which returns an iterator that applies the given function to the items of an input iterable, so that the cumulative sum is computed.

```
def runningSum(nums):
    return [sum(nums[:i+1]) for i in range(len(nums))]
    
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
```


### CHAIN 

itertools.chain() is useful when you need to iterate over multiple iterables in a single for loop or when you want to concatenate the elements of multiple iterables into a single iterable.

```
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# create an iterator that concatenates the elements of the three lists
iterator = itertools.chain(list1, list2, list3)

# print the concatenated elements
for i in iterator:
    print(i)

```

itertools.chain() is useful when you need to iterate over multiple iterables in a single for loop or when you want to concatenate the elements of multiple iterables into a single iterable.

### Permutations

`itertools.permutations()` is a function in the itertools module that returns an iterator that generates all possible r-length permutations of the elements in an input iterable. The input iterable can be any type of iterable, such as a list, tuple, string, etc. The permutations() function takes two arguments:

iterable: the input iterable
r: the length of the permutations (default is None, which means that the length of the permutations is the length of the input iterable)
Here's an example of how you might use the itertools.permutations() function to generate all possible 2-length permutations of the elements in a list:


```
import itertools

list1 = [1, 2, 3]

# create an iterator that generates all possible 2-length permutations of the elements in list1
iterator = itertools.permutations(list1, 2)

# print the permutations
for i in iterator:
    print(i)
#This will output:
#(1, 2)
#(1, 3)
#(2, 1)
#(2, 3)
#(3, 1)
#(3, 2)
```
If you don't provide the second argument r for the permutations length, then it returns permutations of the given iterable's length


iterator = itertools.permutations(list1)
itertools.permutations() is useful when you need to generate all possible permutations of a set of elements, such as in combinatorics and mathematical problems, or when you want to generate all possible combinations of elements in an iterable.
