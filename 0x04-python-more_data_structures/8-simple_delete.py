#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary.keys():
        return a_dictionary
    else:
        del a_dictionary[key]
    
    return a_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'tra')
print(new_dict)
