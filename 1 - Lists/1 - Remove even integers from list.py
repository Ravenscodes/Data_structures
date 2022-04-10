"""
Implement a function that removes all the even elements from a given list. Name it remove_even(lst).

Input:
A list with random integers.

Output:
A list with only odd integers

Sample Input:
my_list = [1,2,4,5,10,6,3]
Sample Output:
my_list = [1,5,3]

"""


def remove_even(lst):
    # List comprehension to iter over List and add to new list if not even
    return [number for number in lst if number % 2 != 0]


print(remove_even([3, 2, 41, 3, 34]))