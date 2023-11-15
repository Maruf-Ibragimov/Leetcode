"""
                                Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""


# Here is my solution. It passed 72 tests from 96. It works!!!
def is_valid(s: str) -> bool:
    char = {"(": ")", "[": "]", "{": "}"}
    for key, value in char.items():
        for i in range(len(s)):
            if s[i] == key and s[i + 1] == value:
                return True
            else:
                return False


print(is_valid("(]"))


# Here is solution from ChatGPT
def isValid(s):
    lst_el = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not lst_el or lst_el.pop() != mapping[char]:
                return False
        else:
            lst_el.append(char)
    return not lst_el


print(isValid("()[]{}"))  # Output: True
