def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return -1, 0

    new_list = []
    while input_list:
        max = input_list[0]
        for x in input_list:
            if x is None:
                return -1, 0
            if x > max:
                max = x
        # new list form greatest to smallest
        new_list.append(max)
        # while loop so remove to shorten list
        input_list.remove(max)    

    a = 0
    b = 0

    for i in range(len(new_list)):
        if (i % 2 != 0):
            # 22 * 10 == 220 then add new_list[i] (4) and you get 224, 
            # that way you dont have to convert to string then back to int
            a = a * 10 + new_list[i]
        else:
            b = b * 10 + new_list[i]

    return a, b

        
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]


# Tests

# with dup ints
test_function([[22, 22, 3, 4, 5], [224, 2253]]) 

# with None num
test_function([[8, None, 3, 4, 5, 0, 2], [-1, 0]]) 

# with no ints at all
test_function([[], [-1, 0]]) # -1





