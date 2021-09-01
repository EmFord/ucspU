
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

# find the pivot point (which is just the middle of the array?)
    if len(input_list) < 1:
        return -1 

    low = 0
    high = len(input_list) - 1
    pivot_point_indx = (low+high) // 2
    # print(input_list)

    if input_list[pivot_point_indx] == number:
        return pivot_point_indx

    if input_list[low] <= input_list[pivot_point_indx]:
        if input_list[low] <= number and input_list[pivot_point_indx] >= number:
            return rotated_array_search(input_list[low:pivot_point_indx-1], number)
        
        return rotated_array_search(input_list[pivot_point_indx+1:high], number)

    if input_list[pivot_point_indx] <= number and input_list[high] >= number:
        return rotated_array_search(input_list[pivot_point_indx+1:high], number)
    else:
        return rotated_array_search(input_list[low:pivot_point_indx-1], number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# Tests
test_function([6, 7, 8, None, 10, 1, 2, 3, 4], 6])
test_function([6, 7, 8, 2, 10, 1, 2, 3, 4], None])
test_function([6, 7, 8, 2, 10, 1, 2, 3, 4], 800])