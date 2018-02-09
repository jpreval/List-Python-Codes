
"""
You are going to be given an array of integers. 
Your job is to take that array and find an index N where 
the sum of the integers to the left of N is equal to the sum of the integers to the right of N. 
If there is no index that would make this happen, return -1.
"""

def find_even_index(arr):
    n = arr
    if sum(n[1:]) == 0 : return 0
    if sum(n[:-1]) == 0 : return len(n) -1 
    for i in range(len(n)):
        if sum(n[:i]) == sum(n[i+1:]): return i
    return -1
