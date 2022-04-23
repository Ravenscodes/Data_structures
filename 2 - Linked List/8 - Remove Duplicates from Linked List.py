"""
You will now be implementing the remove_duplicates() function.
When a linked list is passed to this function, it removes any node which is a duplicate of another existing node.

Input
A linked list.

Output
A list with all the duplicates removed.

Sample Input
LinkedList = 1->2->2->2->3->4->4->5->6

Sample Output
LinkedList = 1->2->3->4->5->6
"""

from LinkedList import LinkedList
from Node import Node


def remove_duplicates(lst):
    if lst.is_empty():
        return None
    n = lst.get_head()
    visited = []
    prev_node = None
    while n:
        if n.data not in visited:
            visited.append(n.data)
            prev_node = n
            n = n.next_element
        else:
            prev_node.next_element = n.next_element
            n = n.next_element
    return lst


lst = LinkedList()

lst.insert_at_head(14)
lst.insert_at_head(21)
lst.insert_at_head(7)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(22)
lst.print_list()
lst2 = remove_duplicates(lst)
lst2.print_list()

