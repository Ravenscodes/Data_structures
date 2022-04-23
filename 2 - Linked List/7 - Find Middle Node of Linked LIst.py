"""
You have to implement the find_mid() function which will take a linked list as an input
and return the value of the middle node.
If the length of the list is even, the middle value will occur at length/2
​For a list of odd length, the middle value will be length/2 +1

Input
A singly linked list.

Output
The integer value of the middle node.

Sample Input
LinkedList = 7->14->10->21

Sample Output
14
"""

from LinkedList import LinkedList
from Node import Node


def find_mid(lst):
    if lst.is_empty():
        return None

    tmp = lst.get_head()
    l = lst.length()

    if l % 2 == 0:
        mid = l // 2 - 1
    else:
        mid = l // 2

    i = 0
    while tmp and i != mid:
        i += 1
        tmp = tmp.next_element
    return tmp.data


lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.print_list()
print(find_mid(lst))
lst.insert_at_head(12)
print(find_mid(lst))