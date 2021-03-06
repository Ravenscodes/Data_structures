"""
By definition, a loop is formed when a node in your linked list points to a previously traversed node.

You must implement the detect_loop() function which will take a linked list
as input and deduce whether or not a loop is present.

Input
A singly linked list.

Output
Returns True if the given linked list contains a loop. Otherwise, it returns False

Sample Input
LinkedList = 7->14->21->7 # Both '7's are the same node. Not duplicates.

Sample Output
True
"""
from LinkedList import LinkedList
from Node import Node


def detect_loop(lst):
    # Floyd's Cycle Finding Algorithm
    # Keep two iterators
    onestep = lst.get_head()
    twostep = lst.get_head()
    while onestep and twostep and twostep.next_element:
        onestep = onestep.next_element  # Moves one node at a time
        twostep = twostep.next_element.next_element  # Skips a node
        if onestep == twostep:  # Loop exists
            return True
    return False


lst = LinkedList()

lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)

# Adding a loop
head = lst.get_head()
node = lst.get_head()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element

print(detect_loop(lst))