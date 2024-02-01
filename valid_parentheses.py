"""
                                        #20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


# My Solution
def valid_parentheses(s: str):
    characters = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    for c in s:
        if c in characters:
            if stack and stack[-1] == characters[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    if not stack:
        return True
    else:
        return False


# print(valid_parentheses("()[]{}"))


# Solution from ChatGPT
def valid_p(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():  # If it is an open bracket
            stack.append(char)
        elif char in mapping.keys():  # If it is a close bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            return False  # If the character is neither an open nor a close bracket

    return not stack  # The string is valid if the stack is empty


# Example usage:
print(valid_p("()"))  # Output: True
# print(valid_p("()[]{}"))  # Output: True
# print(valid_p("(]"))  # Output: False
