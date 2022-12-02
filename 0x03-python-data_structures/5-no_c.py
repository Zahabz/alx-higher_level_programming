#!/usr/bin/python3

def no_c(my_string):
    my_string = my_string.translate({ord(letter): None for letter in 'Cc'})
    return my_string
