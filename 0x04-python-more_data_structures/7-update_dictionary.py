#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value

    for key, value in a_dictionary.items():
        print('{}: {}'.format(key, value))


a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
new_dict


