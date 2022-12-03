#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        return None
    
    mul_tuple = len(sentence), sentence[0]

    return mul_tuple


sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
