#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    dict_list = [key for key, value in a_dictionary.items() if value == max(a_dictionary.values())]
    return dict_list[0]

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
other_key = best_score(None)
print(other_key)
print(best_key)

