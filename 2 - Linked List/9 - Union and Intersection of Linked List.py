"""
Union and intersection are two of the most popular operations which can be performed on data sets.
Now, you will be implementing them for linked lists! Let’s take a look at their definitions:

Union:
Given two lists, A and B, the union is the list that contains elements or objects that
belong to either A, B, or to both.

Intersection:
Given two lists, A and B, the intersection is the largest list which contains all
the elements that are common to both the sets.

The union function will take two linked lists and return their union.

The intersection function will return all the elements that are common between two linked lists.

Input
Two linked lists.

Output
A list containing the union of the two lists.
A list containing the intersection of the two lists.

Sample Input
list1 = 10->20->80->60
list2 = 15->20->30->60->45

Sample Output
union = 10->20->80->60->15->30->45
intersection = 20->60
"""

from LinkedList import LinkedList
from Node import Node


def union(list1, list2):
    result = LinkedList()
    if list2.is_empty():
        return list1
    if list1.is_empty():
        return list2

    n = list1.get_head()
    while n:
        result.insert_at_tail(n.data)
        n = n.next_element

    n2 = list2.get_head()
    while n2:
        result.insert_at_tail(n2.data)
        n2 = n2.next_element
    result.remove_duplicates()

    return result


def intersection(list1, list2):
    result = LinkedList()
    if list1.is_empty() or list2.is_empty():
        return result
    l1 = list1.get_head()
    while l1:
        if list2.search(l1.data) and not result.search(l1.data):
            result.insert_at_head(l1.data)
        l1 = l1.next_element
    return result


list1 = LinkedList()
list2 = LinkedList()
list1.insert_at_tail(10)
list1.insert_at_tail(20)
list1.insert_at_tail(80)
list1.insert_at_tail(60)

list2.insert_at_tail(15)
list2.insert_at_tail(20)
list2.insert_at_tail(30)
list2.insert_at_tail(60)
list2.insert_at_tail(45)

list1.print_list()
list2.print_list()

l3 = union(list1, list2)
print('union')
l3.print_list()

l3 = intersection(list1, list2)
print('intersection')
l3.print_list()