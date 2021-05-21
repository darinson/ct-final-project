'''
Perfect Squares
---------------
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
Example 1:
Input: num = 16
Output: True
Example 2:
Input: num = 14
Output: False
Constraints:
1 <= num <= 2^31 - 1

'''


def ps(num):
    if (num ** (0.5)) == int(num ** (0.5)):
        return True
    return False


print(ps(16))
print(ps(14))
