"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, 

which should be separated by an ampersand.

"""

def namelist(names):
    a = names
    c = [i['name'] for i in a]
    if len(c) == 0:
        r = ''
    elif len(c) == 1:
        r = c[0]
    else:
        r = ', '.join(c[:-1]) + ' & ' + a[-1]['name']
    return r
    
    
