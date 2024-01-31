"""
                                    #14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


# Solution from ChatGPT
def longest_cmn(strs):
    # Check if the input list is empty
    if not strs:
        return ""

    # Sort the list of strings lexicographically (alphabetically)
    strs.sort()

    # Initialize an empty string to store the common prefix
    prefix = ""

    # Iterate through the characters of the first string in the sorted list
    for i in range(len(strs[0])):
        # Check if the current character matches the corresponding character in the last string
        if i < len(strs[-1]) and strs[0][i] == strs[-1][i]:
            # If they match, append the character to the common prefix
            prefix += strs[0][i]
        else:
            # If they don't match, break out of the loop
            break

    # Return the computed common prefix
    return prefix


# Example usage
print(longest_cmn(["flower", "flow", "flight"]))


# My Solution
def longest_common_prefix(strs):
    result = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result


print(longest_cmn(["flower", "flow", "flight"]))
