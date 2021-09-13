def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    l = len(ints)
    min = 0
    max = 0

    if l == 0:
        return(-1, -1)

    for i in range(0, l):
        if min > ints[i] or min == ints[i]:
            min = ints[i]
                     
        elif max < ints[i] or max == ints[i]:
            max = ints[i]

    return (min, max)        


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# Test cases

print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print(get_min_max([0])) # (0, 0)


print("Pass" if ((-1, -1) == get_min_max([])) else "Fail")
print(get_min_max([])) # (-1, -1)


print("Pass" if ((-4, 3) == get_min_max([0, -1, -2, 3, -4])) else "Fail")
print(get_min_max([0, -1, -2, 3, -4]))  # (-4, 3)



