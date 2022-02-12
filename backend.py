import os
import math

fx = ''
a = 0
b = 0
e = 0
e_last = None

def create_fx():
    my_file = open('helper.py', 'w')
    text_for_file = 'def calculate(x):\n\timport math\n\treturn '+fx
    my_file.write(text_for_file)
    my_file.close()
    import helper

def str_to_list(value_str):
    value = []
    for i in value_str:
        value.append(i)
    return value

def list_to_str(value):
    value_str = ''
    for i in value:
        value_str+=i
    return float(value_str)

def round_function(value):
    if len(value)>4:
        if value[4]=='5':
            value[3] = str(int(value[3])+1) if int(value[4])%2!=0 else value[3]
            return list_to_str(value)
        else:   
            value[3] = str(int(value[3])+1) if int(value[4])>5 else value[3]
            return list_to_str(value)
    else:
        return list_to_str(value)

def result_line():
    from helper import calculate
    global a, b, fx, e, e_lest
    fa = round_function(str_to_list(str(calculate(a))))
    fb = round_function(str_to_list(str(calculate(b))))
    printa = a
    printb = b
    c=round_function(str_to_list(str((a+b)/2)))
    fc = round_function(str_to_list(str(calculate(c))))
    e_last = b-a

    if fa*fc<0:
        b = c
    elif fb*fc<0:
        a = c

    return printa, fa, printb, fb,  c, fc, e_last

def start(take_a, take_b, take_e, take_fx):
    global a, b, fx, e
    a = take_a
    b = take_b
    fx = take_fx
    e = take_e
    create_fx()
    i = -1
    return_list = []
    while(e_last == None or e<e_last):
        i+=1
        aret, fa, bret, fb, c, fc, e_last = result_line()
        return_list.append(str(i)+ ' ' + str(aret) + ' ' + str(fa) + ' ' + str(bret) + ' ' + str(fb) + ' ' + str(c) + ' ' + str(fc) + ' ' + str(e_last))
    return return_list

