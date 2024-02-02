"""
                                    #26. Remove duplicates from sorted array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
element appears only once. The relative order of the elements should be kept the same. Then return the number of
unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were
present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


# My Solution. It's working. But not accepted on leetcode
def remove_duplicates(nums: list):
    unique_list = []
    for num in nums:
        if num not in unique_list:
            unique_list.append(num)
        else:
            continue
    return unique_list


print(remove_duplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates(nums=[1, 1, 2]))


# Solution from YouTube.(Neetcode)
def remove(nums: list):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left


print(remove([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


# Solution from ChatGPT
def remove_duplicates(nums):
    if not nums:
        return 0

    # Initialize variables
    unique_count = 1  # Number of unique elements
    current_index = 1  # Index to insert the next unique element

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Check for uniqueness
        if nums[i] != nums[i - 1]:
            # Update the unique count and insert the unique element at the current index
            unique_count += 1
            nums[current_index] = nums[i]
            current_index += 1

    return unique_count


# Example 1
nums1 = [1, 1, 2]
result1 = remove_duplicates(nums1)
print(result1, nums1[:result1])

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = remove_duplicates(nums2)
print(result2, nums2[:result2])
