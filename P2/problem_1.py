
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not number:
        return None

    if number <= 1:
        return number

    first = 1
    last = number
    # while in range of the number
    while first <= last:
        # total of first and last floor divided by 2
        # floor division rounds the result down to the nearest whole number
        mid = (first + last) // 2

        # if that divided number times itself equals number then answer
        if (mid*mid == number):
            return mid
        
        # if that number is less add 1 and answer
        if (mid*mid < number):
            first = mid + 1
            floor = mid
        
        # otherwise subtract 1 to get floor number
        else:
            last = mid - 1

    return floor


print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if  (5 == sqrt(27)) else "Fail")

# Test cases
result = sqrt(None)
print(result)
assert result is None 

result = sqrt(490.56)
print(result)
assert result == 22.0

result = sqrt(4397498732947)
print(result)
assert result == 2097021 

