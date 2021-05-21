'''
Given an array words of strings made only from lowercase letters, return a list of all 
characters that show up in all strings within the list (including duplicates).  
For example, if a character occurs 3 times in all strings but not 4 times, you need to 
include that character three times in the final answer.
You may return the answer in any order.
Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: ["coool","lock","cook"]
Output: ["c","o"]
 
Note:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''

'''
def common(arr):
    unique = {x: 0 for x in set(list("".join(arr)))}
    for word in arr:
        for letter in word:
            unique[letter] += 1
    ul = []
    for x, y in unique.items():
        if y % len(arr) == 0 or y // len(arr) >= 1:
            ul.extend([x] * (y // len(arr)))
    return(ul)


print(common(["coool", "lock", "cook"]))
'''


def common2(arr):
    c = arr[0].split()
    print(c)


(common2(["coool", "lock", "cook"]))
