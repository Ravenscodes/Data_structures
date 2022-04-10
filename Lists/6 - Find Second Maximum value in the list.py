"""
Implement a function find_second_maximum(lst) which returns the second largest element in the list.

Input:
A List

Output:
Second largest element in the list

Sample Input
[9,2,3,6]

Sample Output
6
"""


def find_second_maximum(lst):
    if len(lst) < 2:
        return None
    max1 = max(lst[0], lst[1])
    max2 = min(lst[0], lst[1])
    for elem in lst[2:]:
        if elem > max1:
            max2 = max1
            max1 = elem
        elif elem > max2:
            max2 = elem
    return max2


print(find_second_maximum([9, 2, 3, 6]))