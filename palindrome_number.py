"""
                            Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


def is_palindrome(x):
    if x < 0:
        return False

    reversed_x = int(str(x)[::-1])
    return x == reversed_x


print(is_palindrome(121))
