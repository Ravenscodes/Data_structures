"""
Implement a function findMinimum(lst) which finds the smallest number in the given list.

Input:
A list of integers

Output:
The smallest number in the list

Sample Input
arr = [9,2,3,6]

Sample Output
2
"""


def find_minimum(arr):
    if not arr:
        return None
    minv = arr[0]
    for elem in arr[1:]:
        if elem < minv:
            minv = elem
    return minv


print(find_minimum([9, 2, 3, 6]))