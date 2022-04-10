"""
In this problem, you have to implement the find_sum(lst,k)
function which will take a number k as input and return two numbers that add up to k.

Input
A list and a number k

Output
A list with two integers a and b that add up to k

Sample Input
lst = [1,21,3,14,5,60,7,6]
k = 81

Sample Output
lst = [21,60]

"""


def find_sum(lst, k):
    # Solution with extra memory
    d = dict()
    for elem in lst:
        if d.get(elem) is not None:
            return [d.get(elem), elem]
        else:
            d[k - elem] = elem
    return []


def find_sum_2(lst, k):
    # Solution without extra memory but with sort
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    sum = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while index1 != index2:
        sum = lst[index1] + lst[index2]
        if sum < k:
            index1 += 1
        elif sum > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    return False


print(find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))
print(find_sum([1, 2, 3, 4, -2, -3], 1))