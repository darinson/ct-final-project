'''
Two Sum Problem
---------------
Create a function that given a list of numbers (that are sorted) and a target number as a sum, 
return the two index numbers that when added equal the target number
If numbers don't exist, return -1
Example Input: [2,7,11,15], target = 9
Example Output: [0,1]
Example 2: twosum([2,4,6,12], target = 8) [0,2]


'''


def twosum(arr, tar):
    di = {x: (tar-x) for x in arr if x < tar}  # O(n)
    for x, y in di.items():  # O(1)
        if x in arr and y in arr:
            if arr.index(x) != arr.index(y):
                return [arr.index(x), arr.index(y)]
    return(-1)


print(twosum([2, 7, 11, 15], 9))
print(twosum([2, 4, 10, 12], 8))
