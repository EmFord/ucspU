
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

# find the pivot point (which is just the middle of the array?)
    if number is None:
        return -1 

    if len(input_list) < 1:
        return -1

    start = 0
    end = len(input_list) - 1

    while start <= end:

        mid = (start+end) // 2
        if input_list[mid] == number:
            return mid

        if input_list[start] <= input_list[mid]:
            if input_list[start] <= number < input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
            
        elif input_list[mid] < number <= input_list[end]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


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
test_function([[6, 7, 8, None, 10, 1, 2, 3, 4], 3]) # print with finding 3
test_function([[6, 7, 8, 2, 10, 1, 2, 3, 4], None]) # returns -1 for none
test_function([[6, 7, 8, 2, 10, 1, 2, 3, 4], 800]) # returns -1 for not in list

