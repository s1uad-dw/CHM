from unittest import result
import general_functions
import importlib
import os
import math

def gaus(equations=[], e=0, elements = 0, last_result=[]):
    result = []
    x = 1
    simbol = '0123456789.-'
    if elements == 0:
        for i  in range(len(equations)):
            value = ''
            line = []
            if i == 0:
                line.append('')
            for z in range(len(equations[i])):#  x1   x2   xn   свободные_члены 
                if equations[i][z] in simbol:
                    value+=equations[i][z]
                elif equations[i][z] == 'x':
                    line.append(float(value))
                    value= ''
                if z == len(equations[i])-1:
                    line.append(float(value))
                    value = ''
            if i != 0:
                line.insert(0,
                general_functions.round_function(-line[0]/result[0][1], len(str(e))-2))#m
            #контрольные суммы, довести до естественного вида
            line.append("")
    else:
        pass    #подсчёт 2ого блока 
    if elements != 0:
        line.append(general_functions.round_function(last_result[0][-2]*last_result[1][0]+last_result[1][-2])) 
        result.append(line)
        #Рекурсия для блоков таблицы
    for i in equations:
        if i[-1] == '' or i[-1] > e:
            result.append(gaus(e=e, elements=elements+1, last_result = result))
            break
    return result

if __name__ == '__main__':
    equations=[
        '0.68x+0.75x-0.5x=0',
        '0.21x+2x-12x=0'
    ]
    printing = gaus(equations=equations)
    print(printing)

