from unittest import result
import general_functions
import importlib
import os
import math

def gaus(equations, e=0, elements = 1):
    result = []
    x = 1
    simbol = '0123456789.-'
    switch = False
    # signs = '+-/*='
    for i  in range(len(equations)):
        value = ''
        line = []
        if i == 0:
            line.append('')
        for z in range(len(equations[i])):
            if equations[i][z] in simbol:
                value+=equations[i][z]
            elif equations[i][z] == 'x':
                line.append(float(value))
                value= ''
            if z == len(equations[i])-1:
                line.append(float(value))
                value = ''
        if i != 0:
            line.insert(0, general_functions.round_function(-line[0]/result[0][1], len(str(e))-2))
        # добавить контрольные суммы
        # if elements == 0:
        #     line.append("")
        result.append(line)

    return result

if __name__ == '__main__':
    equations=[
        '0.68x+0.75x-0.5x=0',
        '0.21x+2x-12x=0'
    ]
    printing = gaus(equations)
    print(printing)

