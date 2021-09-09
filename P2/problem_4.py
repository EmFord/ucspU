def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if len(input_list) <= 1:
        return input_list

    lo = 0
    hi = len(input_list) - 1
    mid = 0

    while mid <= hi:
        # if the mid is higher than the lo reverse the numbers
        if input_list[mid] == 0:
            input_list[lo], input_list[mid] = input_list[mid], input_list[lo]
            lo = lo + 1
            mid = mid + 1
        # if it is same then do nothing
        elif input_list[mid] == 1:
            mid = mid + 1
        # otherwise mid will be 2 so reverse with the high because it must be less than or equal to the high
        elif input_list[mid] == 2:
            input_list[mid], input_list[hi] = input_list[hi], input_list[mid]
            hi = hi - 1
        else:
            return -1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])


# Test cases

# all the same numbers
assert sort_012([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0] # should be the same
print(sort_012([0, 0, 0, 0, 0, 0, 0, 0, 0]))

# empty list should return
assert sort_012([]) == []
print(sort_012([]))

# Non valid number
assert sort_012([1, 2, 0, 4]) == -1
print(sort_012([1, 2, 0, 4]))


