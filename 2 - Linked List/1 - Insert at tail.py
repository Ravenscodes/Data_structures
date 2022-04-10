"""
We need to insert a new object at the end of the linked list.
You can naturally guess that this newly added node will point to None as it is at the tail.

Input
A linked list and an integer value.

Output
The updated linked list with the value inserted.

Sample Input
Linked List = 0->1->2
integer = 3

Sample Output
Linked List = 0->1->2->3
"""
from LinkedList import LinkedList
from Node import Node

# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Node class  {int data ; Node next_element;}

# Inserts a value at the end of the list


def insert_at_tail(lst, value):
    new_node = Node(value)

    if lst.get_head() is None:
        lst.head_node = new_node
        return

    temp = lst.get_head()

    while temp.next_element:
        temp = temp.next_element

    temp.next_element = new_node
    return


lst = LinkedList()
lst.print_list()
insert_at_tail(lst, 0)
lst.print_list()
insert_at_tail(lst, 1)
lst.print_list()
insert_at_tail(lst, 2)
lst.print_list()
insert_at_tail(lst, 3)
lst.print_list()

