"""
Implement a function that merges two sorted lists of m and n elements respectively,
into another sorted list. Name it merge_lists(lst1, lst2).

Input:
Two sorted lists.

Output:
A merged and sorted list consisting of all elements of both input lists.

Sample Input:
list1 = [1,3,4,5]
list2 = [2,6,7,8]

Sample Output:
arr = [1,2,3,4,5,6,7,8]
"""


def merge_lists(lst1, lst2):
    i, j = 0, 0
    total_list = []
    while i != len(lst1) and j != len(lst2):
        if lst1[i] <= lst2[j]:
            total_list.append(lst1[i])
            i += 1
        else:
            total_list.append(lst2[j])
            j += 1

    for elem in lst2[j:]:
        total_list.append(elem)
    for elem in lst1[i:]:
        total_list.append(elem)

    return total_list


def merge_arrays(lst1, lst2):
    # merging in place without new list
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if lst1[ind1] > lst2[ind2]:
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1


print(merge_lists([1, 3, 4, 5], [2, 6, 7, 8]))
print(merge_arrays([1, 5], [2, 3, 4, 8, 9]))