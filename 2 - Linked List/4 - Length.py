"""
In this problem, you have to implement the length() function which will find the length of a given linked list.

Input
A linked list.

Output
The number of nodes in the list.

Sample Input
linkedlist = 0->1->2->3->4

Sample Output
5
"""

from Node import Node
from LinkedList import LinkedList


def length(lst):
    if lst.get_head() is None:
        return 0
    tmp = lst.get_head()
    l = 1
    while tmp.next_element:
        l += 1
        tmp = tmp.next_element
    return l



lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
print(length(lst))