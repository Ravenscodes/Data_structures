"""
Given an integer list, return the maximum sublist sum.
The list may contain both positive and negative integers and is unsorted.

Input#
a list lst
Output#
a number (maximum subarray sum)

Sample input
[-4, 2, -5, 1, 2, 3, 6, -5, 1]

Sample output
largest_sum = 12
"""


def find_max_sum_sublist(lst):
    if not lst:
        return None

    global_max, curr_sum = lst[0], lst[0]
    for elem in lst[1:]:
        if curr_sum < 0:
            curr_sum = elem
        else:
            curr_sum += elem
        if global_max < curr_sum:
            global_max = curr_sum
    return global_max


print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
print(find_max_sum_sublist([1, 2, 3]))