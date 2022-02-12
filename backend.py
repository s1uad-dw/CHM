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

def float_to_list(value_float):
    value = []
    for i in str(value_float):
        value.append(i)
    return value

def list_to_str(value):
    value_str = ''
    for i in value:
        value_str+=i
    return float(value_str)

def round_function(value):
    if value[0] != '-':
        if len(value)>4:
            if value[4]=='5' and len(value)<5:
                value[3] = str(int(value[3])+1) if int(value[3])%2!=0 else value[3]
                return list_to_str(value[:4])
            else:   
                value[3] = str(int(value[3])+1) if int(value[4])>5 else value[3]
                return list_to_str(value[:4])
        else:
            while len(value)<5:
                value.append('0')
            return list_to_str(value[:4])
    else:
        if len(value)>5:
            if value[5]=='5' and len(value)<6:
                value[4] = str(int(value[4])+1) if int(value[4])%2!=0 else value[4]
                return list_to_str(value[:5])
            else:   
                value[4] = str(int(value[4])+1) if int(value[5])>5 else value[4]
                return list_to_str(value[:5])
        else:
            while len(value)<6:
                value.append('0')
            return list_to_str(value[:5])
def result_line():
    from helper import calculate
    global a, b, fx, e, e_last
    fa = round_function(float_to_list(calculate(a)))
    fb = round_function(float_to_list(calculate(b)))
    printa = a
    printb = b
    c=round_function(float_to_list((a+b)/2))
    fc = round_function(float_to_list(calculate(c)))
    e_last = round_function(float_to_list(b-a))

    if fa*fc<0:
        b = c
    elif fb*fc<0:
        a = c

    return printa, fa, printb, fb,  c, fc, e_last

def start(take_a, take_b, take_e, take_fx):
    global a, b, fx, e, e_last
    fx = ''
    a = 0
    b = 0
    e = 0
    e_last = None
    a = take_a
    b = take_b
    fx = take_fx
    e = take_e
    create_fx()
    i = -1
    output = ''
    while(e_last == None or e<e_last):
        i+=1
        aret, fa, bret, fb, c, fc, e_last = result_line()
        if len(str(aret))<4:
            aret = str(aret) + '     |  '
        elif len(str(aret))<5:
            aret = str(aret) + '   |  '
        else:
            aret = str(aret) + ' |  '
        if len(str(fa))<4:
            fa = str(fa) + '     |  '
        elif len(str(fa))<5:
            fa = str(fa) + '   |  '
        else:
            fa = str(fa) + ' |  '
        if len(str(bret))<4:
            bret = str(bret) + '     |  '
        elif len(str(bret))<5:
            bret = str(bret) + '   |  '
        else:
            bret = str(bret) + ' |  '
        if len(str(fb))<4:
            fb = str(fb) + '     |  '
        elif len(str(fb))<5:
            fb = str(fb) + '   |  '
        else:
            fb = str(fb) + ' |  '
        if len(str(c))<4:
            c = str(c) + '     |  '
        elif len(str(c))<5:
            c = str(c) + '   |  '
        else:
            c = str(c) + ' |  '
        if len(str(fc))<4:
            fc = str(fc) + '     |  '
        elif len(str(fc))<5:
            fc = str(fc) + '   |  '
        else:
            fc = str(fc) + ' |  '
        output += str(i)+'  |  '+str(aret)+str(fa)+str(bret)+str(fb)+str(c)+str(fc)
        output += str(e_last)+'  |  \n'
    return output

