"""
In the find_nth function, a certain N is specified as an argument.
You simply need to return the node which is N spaces away from the None end of the linked list.

Input
A linked list and a position N.

Output
The value of the node n positions from the end. Returns -1 if n is out of bounds.

Sample Input
LinkedList = 22->18->60->78->47->39->99 and n = 3

Sample Output
47
"""

from LinkedList import LinkedList
from Node import Node


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


def find_nth_at_head(lst, n):
    if lst.is_empty():
        return -1
    node = lst.get_head()
    for i in range(n-1):
        if node is None:
            return -1
        node = node.next_element
    return node.data


def find_nth(lst, n):
    tmp = reverse(lst)
    return find_nth_at_head(tmp, n)


list1 = LinkedList()
list1.insert_at_tail(22)
list1.insert_at_tail(18)
list1.insert_at_tail(60)
list1.insert_at_tail(78)
list1.insert_at_tail(47)
list1.insert_at_tail(39)
list1.insert_at_tail(99)

list1.print_list()
print(find_nth(list1, 3))