"""
You have to define the reverse function, which takes a singly linked list and produces the exact opposite list, i.e.,
the links of the output linked list should be reversed.

Input
A singly linked list.

Output
The reversed linked list.

Sample Input
The input linked list object:

LinkedList = 0->1->2->3-4

Sample Output
The reversed linked list:

LinkedList = 4->3->2->1->0
"""

from Node import Node
from LinkedList import LinkedList


def reverse(lst):
    tmp = lst.get_head()
    if tmp is None:
        return LinkedList()
    new_lst = LinkedList()
    while tmp.next_element:
        new_lst.insert_at_head(tmp.data)
        tmp = tmp.next_element
    new_lst.insert_at_head(tmp.data)
    return new_lst

lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
lst = reverse(lst)
lst.print_list()