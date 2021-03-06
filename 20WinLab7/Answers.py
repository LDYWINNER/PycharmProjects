# CSE 101
# Lab 7
# Name:
# Email address:

###############################################################
# Write recursive functions in this file whenever possible.
# You can assume the pre-condition will always be true when you
# run your code.
###############################################################

def is_even(n):
    return n % 2 == 0

# Computes n!
# Pre-condition: n >= 0
#
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)

# Computes 0 + 1 + 2 + ... + n
# Pre-condition: n >= 0
#
def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)

# Computes 0 + 2 + 4 + ... + n
# Pre-condition: n >= 0
#
def sum_even_to(n):
    if n == 0:
        return 0
    elif n % 2 == 1:
        return (n-1) + sum_even_to(n - 3)
    elif n % 2 == 0:
        return n + sum_even_to(n - 2)

# Concatenates the numbers in forward order to form a string.
# If n = 9, it returns '0123456789'
# If n = 13, it returns '012345678910111213'
# Pre-condition: n >= 0
#
def concat_to(n):
    if n == 0:
        return '0'
    return concat_to(n - 1) + str(n)

# Concatenates the numbers in reverse order to form a string.
# If n = 9, it returns '9876543210'
# If n = 13, it returns '131211109876543210'
# Pre-condition: n >= 0
#
def concat_reverse_to(n):
    if n == 0:
        return '0'
    return str(n) + concat_reverse_to(n - 1)


###################################################
# Now dealing with lists
###################################################

# Computes the sum of all the elements in the list u.
# sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] returns 55
#
def sum(u):
    if u == []:
        return 0
    return u[0] + sum(u[1:])

# Computes the sum of all the even elements in the list u.
# sum_evens([1, 2, 3, 4] returns 6
# sum_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] returns 30
#
def sum_evens(u):
    if u == []:
        return 0
    elif u[0] % 2 == 0:
        return u[0] + sum_evens(u[1:])
    elif u[0] % 2 == 1:
        return sum_evens(u[1:])

# Finds and returns only the even elements in the list u.
# find_evens([1, 2, 3, 4] returns [2, 4]
# find_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] returns [2, 4, 6, 8, 10]
#
def find_evens(u):
    if u == []:
        return []
    elif u[0] % 2 == 0:
        return [u[0]] + find_evens(u[1:])
    elif u[0] % 2 == 1:
        return find_evens(u[1:])

""" Uncomment one function at a time and its corresponding test cases in 
    the main function below and continue until you are done with all of 
    the functions. You can do this by moving the triple quotes (") 
    after each function. 
"""


###################################################
# Now the testing part. . .
###################################################

def main():
    print('Testing fac')
    print(' fac(0): ' + str(fac(0)))
    print(' fac(6): ' + str(fac(6)))
    print()

    print('Testing sum_to')
    print(' sum_to(5): ' + str(sum_to(5)))
    print(' sum_to(10): ' + str(sum_to(10)))
    print()

    print('Testing sum_even_to')
    print(' sum_even_to(5): ' + str(sum_even_to(5)))
    print(' sum_even_to(10): ' + str(sum_even_to(10)))
    print()


    print('Testing concat_to')
    print(' concat_to(3): ' + concat_to(3))
    print(' concat_to(13): ' + concat_to(13))
    print()

    print('Testing concat_reverse_to')
    print(' concat_reverse_to(3): ' + concat_reverse_to(3))
    print(' concat_reverse_to(13): ' + concat_reverse_to(13))
    print()

    print('Testing sum')
    u = [1, 2, 3, 4]
    v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(' sum(u): ' + str(sum(u)))
    print(' sum(v): ' + str(sum(v)))
    print()

    print('Testing sum_evens')
    print(' sum_evens(u): ' + str(sum_evens(u)))
    print(' sum_evens(v): ' + str(sum_evens(v)))
    print()

    print('Testing find_evens')
    print(' find_evens(u): ' + str(find_evens(u)))
    print(' find_evens(v): ' + str(find_evens(v)))
    print()

# End of testing
"""Uncomment testing of one function at a time and continue until you are done. """

if __name__ == '__main__':
    main()
