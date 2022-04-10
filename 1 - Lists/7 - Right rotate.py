"""
Implement a function right_rotate(lst, k) which will rotate the given list by k.
This means that the right-most elements will appear at the left-most position in the list and so on.
You only have to rotate the list by one element at a time.

Input
A list and a positive number by which to rotate that list

Output:
The given list rotated by k elements

Sample Input
lst = [10,20,30,40,50]
k = 3
What if the given input k is greater than the length of the lst?

Sample Output
lst = [30,40,50,10,20]
"""


def right_rotate(lst, k):
    # Pythonic rotation
    if not lst:
        return []

    k = k % len(lst)
    return lst[- k:] + lst[: - k]


def right_rotate_without_slice(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    rotated_list = []
    # get the elements from the end
    for item in range(len(lst) - k, len(lst)):
        rotated_list.append(lst[item])
    # get the remaining elements
    for item in range(0, len(lst) - k):
        rotated_list.append(lst[item])
    return rotated_list


print(right_rotate([10, 20, 30, 40, 50], 3))