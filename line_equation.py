from unittest import result
import general_functions
import importlib
import os
import math

def gaus(equations=[], e=0.0005, elements = 0, last_result=[]):
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
            if i != 0 and result!=[]:
                line.insert(0,
                general_functions.round_function(-line[0]/result[0][1], len(str(e))-2))#m
            #контрольные суммы, довести до естественного вида
            line.append('')
            result.append(line)
    else:
        #подсчёт 2ого блока
        line = []
        for i in last_result:
            for z in range(len(i)):
                if z < elements:
                    line.append('')
                else:
                    line.append()
                    q+=1
            line.append(general_functions.round_function(last_result[0][-2]*last_result[1][0]+last_result[1][-2])) #Контрольные суммы
            result.append(line)
        #Рекурсия для блоков таблицы
    if line[-1] == '' or line[-1] > e:
        result.append(gaus(e=e, elements=elements+1, last_result = result))
    return result

if __name__ == '__main__':
    equations=[
        '0.68x+0.75x-0.5x=0',
        '0.21x+2x-12x=0'
    ]
    printing = gaus(equations=equations)
    print(printing)

