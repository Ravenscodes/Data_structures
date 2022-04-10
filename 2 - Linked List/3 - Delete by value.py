"""
In this lesson, you’ll be implementing the delete by value strategy.
We’ll describe its functionality, which should give you a clearer idea of what you have to do.

If you fully understood the last lesson, this should be a piece of cake.

In this function, we can pass a particular value that we want to delete from the list.
The node containing this value could be anywhere in the list.
It is also possible that such a node may not exist at all.

Therefore, we would have to traverse the whole list until we find the value which needs to be deleted.
If the value doesn’t exist, we do not need to do anything.

Input
A linked list and an integer to be deleted.

Output
True if the value is deleted. Otherwise, False.

Sample Input
LinkedList = 3->2->1->0
Integer = 2

Sample Output
True
"""

from LinkedList import LinkedList
from Node import Node


def delete(lst, value):
    deleted = False
    if lst.is_empty():  # Check if list is empty -> Return False
        print("List is Empty")
        return deleted
    current_node = lst.get_head()  # Get current node
    previous_node = None  # Get previous node
    if current_node.data == value:
        lst.delete_at_head()  # Use the previous function
        deleted = True
        return deleted

    # Traversing/Searching for Node to Delete
    while current_node is not None:
        # Node to delete is found
        if value == current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            deleted = True
            break
        previous_node = current_node
        current_node = current_node.next_element

    if deleted == False:
        print(str(value) + " is not in list!")
    else:
        print(str(value) + " deleted!")

    return deleted


lst = LinkedList()
lst.insert_at_head(1)
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.print_list()
delete(lst, 4)
lst.print_list()

delete(lst, 5)
lst.print_list()

delete(lst, 2)
lst.print_list()