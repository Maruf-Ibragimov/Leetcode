"""
                            Write a function
Given a year, determine whether it is a leap year.
If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
It is only necessary to complete the is_leap function.

Sample Input 0
1990

Sample Output 0
False

Explanation 0
1990 is not a multiple of 4 hence it's not a leap year.
"""


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print(is_leap(1900))
