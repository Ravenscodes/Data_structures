"""
Implement a function, find_product(lst), which modifies a list so that each index has a product
of all the numbers present in the list except the number stored at that index.

Input:
A list of numbers (could be floating points or integers)

Output:
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input
arr = [1,2,3,4]

Sample Output
arr = [24,12,8,6]

"""


def find_product(lst):
    mul = 1
    cnt_zeroes = 0
    final_list = []

    for elem in lst:
        if elem == 0:
            cnt_zeroes += 1
        else:
            mul *= elem
    if cnt_zeroes > 1:
        return [0] * len(lst)

    for elem in lst:
        if cnt_zeroes == 1:
            if elem != 0:
                final_list.append(0)
            else:
                final_list.append(mul)
        else:
            final_list.append(mul/elem)
    return final_list


print(find_product([1, 2, 3, 4]))
print(find_product([4, 2, 1, 5, 0]))
print(find_product([4, 0, 1, 5, 0]))