#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        sentence[0] = None
    else:
        mul_tuple = len(sentence), sentence[0]
        return mul_tuple
