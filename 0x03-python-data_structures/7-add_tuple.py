#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 :
        tuple_a = tuple_a + (0,)
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)
    
    element_1 = int(tuple_a[0]) + int(tuple_b[0])
    element_2 = int(tuple_a[1]) + int(tuple_b[1])
    new_tuple = (element_1, element_2)
    
    return new_tuple
