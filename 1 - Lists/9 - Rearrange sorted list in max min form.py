"""
Implement a function called max_min(lst)
which will re-arrange the elements of a sorted list such that the 0th index will have the largest number,
the 1st index will have the smallest, and the 2nd index will have second-largest, and so on.
In other words, all the even-numbered indices will have the largest numbers in the list in descending order
and the odd-numbered indices will have the smallest numbers in ascending order.

Input:
A sorted list

Output:
A list with elements stored in max/min form

Sample Input
lst = [1,2,3,4,5]

Sample Output
lst = [5,1,4,2,3]
"""


def max_min(lst):
    new_lst = []
    start, finish = 0, len(lst)-1
    while start < finish:
        new_lst.append(lst[finish])
        new_lst.append(lst[start])
        start += 1
        finish -= 1
    if start == finish:
        new_lst.append(lst[start])
    return new_lst


def max_min_without_extra_space(lst):
    # Return empty list for empty list
    if len(lst) is 0:
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


print(max_min([1, 2, 3, 4, 5]))
print(max_min([1, 2, 3, 4, 5, 6]))
