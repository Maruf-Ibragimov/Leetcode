"""
                            Plus One
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


# # Here is my code which actually passed 93/111
# def plus_one(digits):
#     x = digits[-1] + 1
#     digits[-1] = x
#     if len(digits) == 1:
#         split_digits = [int(digit) for digit in str(digits[0])]
#         return split_digits
#     else:
#         return digits

# # Here is the solution given by ChatGPT
# def plus_one(digits):
#     n = len(digits)
#     for i in range(n - 1, -1, -1):
#         if digits[i] < 9:
#             digits[i] += 1
#             return digits
#         else:
#             digits[i] = 0
#
#     return [1] + digits

# Here is the solution from YouTube guy

def plus_one(digits):
    text = ""
    for i in digits:
        text += str(i)
    end = int(text)
    end += 1
    str_list = list(str(end))
    for i, v in enumerate(str_list):
        str_list[i] = int(v)
    return str_list


print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
print(plus_one([99]))
