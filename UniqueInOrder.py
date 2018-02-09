"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
without any elements with the same value next to each other and preserving the original order of elements.

"""

def unique_in_order(iterable):
    x = list(iterable)
    if len(x) == 0: return []
    l = []
    l.append(x[0])
    if len(x) == 1: return l
    for i in range(1,len(x)):
        if x[i] != l[-1] : 
            l.append(x[i])
        else : pass
    return l
