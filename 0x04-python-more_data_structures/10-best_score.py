#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    dict_list = [key for key, value in a_dictionary.items() if value == max(a_dictionary.values())]
    return dict_list[0]
