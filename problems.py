"""
                        Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]
#
#
# print(two_sum([2, 7, 11, 15], 9))


"""
                            Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

# def is_palindrome(x):
#     if x < 0:
#         return False
#
#     reversed_x = int(str(x)[::-1])
#     return x == reversed_x
#
#
# print(is_palindrome(121))


"""
                            Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""


def roman_to_int(x):
    roman_nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    ans = 0

    for i in range(len(x)):
        if i < len(x) - 1 and roman_nums[x[i]] < roman_nums[x[i + 1]]:
            ans -= roman_nums[x[i]]
        else:
            ans += roman_nums[x[i]]

    return ans
