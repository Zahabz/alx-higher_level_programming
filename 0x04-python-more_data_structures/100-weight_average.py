#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    else:
        total = 0
        total2 = 0
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                tuple_mul = my_list[i][0] * my_list[i][1]
                total += tuple_mul
                total2 += my_list[i][1]
        
        return (total / total2)
