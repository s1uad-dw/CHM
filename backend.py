from dataclasses import replace
import os
import math

from CHM.helper import calculate

fx = ''
a = 0
b = 0
e = 0
e_last = None
xn=0
bx=0
fxsy=''

def create_fx(fx):
    my_file = open('helper.py', 'w')
    text_for_file = 'def calculate(x):\n\timport math\n\treturn '+fx
    my_file.write(text_for_file)
    my_file.close()

def create_sy(fx):
    my_file = open('proiz.py', 'w')
    text_for_file = '''def fxsy():
                        \n\timport sympy as sym 
                        \n\tx = sym.Symbol("x")
                        \n\tf='''+ fx +'''
                        \n\treturn str(f.diff(x))'''
    my_file.write(text_for_file)
    my_file.close()

def create_sy_2(fx):
    my_file = open('proiz_2.py', 'w')
    text_for_file = '''def fxsy():
                        \n\timport sympy as sym 
                        \n\tx = sym.Symbol("x")
                        \n\tf='''+ fx +'''
                        \n\tf=f.diff(x)
                        \n\treturn str(f.diff(x))'''
    my_file.write(text_for_file)
    my_file.close()

def create_calc_sy(fx):
    fx = fx.replace('sym', 'math')
    my_file = open('proiz_calcul.py', 'w')
    text_for_file = '''def fxsy_1(x):
                        \n\timport math
                        \n\treturn '''+fx
    my_file.write(text_for_file)
    my_file.close()

def create_calc_sy_2(fx):
    fx = fx.replace('sym', 'math')
    my_file = open('proiz_calcul_2.py', 'w')
    text_for_file = '''def fxsy_2(x):
                        \n\timport math
                        \n\treturn '''+fx
    my_file.write(text_for_file)
    my_file.close()

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

def round_function(value, e):
    if value[0] != '-':
        if len(value)>len(e)+1:
            if value[len(e)+1]=='5' and len(value)<len(e)+2:
                value[len(e)] = str(int(value[len(e)])+1) if int(value[len(e)])%2!=0 else value[len(e)]
            else:   
                value[len(e)] = str(int(value[len(e)])+2) if int(value[len(e)+1])>5 else value[len(e)]
        else:
            while len(value)<len(e)+2:
                value.append('0')
        return list_to_str(value[:len(e)+1])
    else:
        if len(value)>len(e)+2:
            if value[len(e)+2]=='5' and len(value)<len(e)+3:
                value[len(e)+1] = str(int(value[len(e)])+1) if int(value[len(e)+1])%2!=0 else value[len(e)+1]
            else:   
                value[len(e)+1] = str(int(value[len(e)+1])+1) if int(value[len(e)+1])>5 else value[len(e)+1]
        else:
            while len(value)<len(e)+3:
                value.append('0')
        return list_to_str(value[:len(e)+2])

def result_division_line():
    from CHM.helper import calculate
    global a, b, fx, e, e_last
    fa = round_function(float_to_list(calculate(a)), float_to_list(e))
    fb = round_function(float_to_list(calculate(b)), float_to_list(e))
    printa = a
    printb = b
    c=round_function(float_to_list((a+b)/2), float_to_list(e))
    fc = round_function(float_to_list(calculate(c)), float_to_list(e))
    e_last = round_function(float_to_list(b-a), float_to_list(e))

    if fa*fc<0:
        b = c
    elif fb*fc<0:
        a = c

    return printa, fa, printb, fb,  c, fc, e_last

def result_chord_line(first_run=False, mode=False):
    from CHM.helper import calculate
    global a, b, fx, e, e_last, xn, bx
    if mode:
        xn = xn+e_last
        fxn=calculate(xn)
        bx=xn-a
        e_last=-(fxn*bx)/(fxn-calculate(a))
        
    else:
        xn = xn+e_last
        fxn=calculate(xn)
        bx=b-xn
        e_last=-(fxn*bx)/(calculate(b)-fxn)
    
    return xn, fxn, bx, e_last

def result_tanget():
    xn = xn+e_last
    fxn=calculate(xn)
    bx=xn-a
    e_last=-(fxn*bx)/fxsy_1(xn)
    return xn, fxn, bx, e_last

def half_division(take_a, take_b, take_e, take_fx):
    global a, b, fx, e, e_last
    a = take_a
    b = take_b
    fx = take_fx
    e = take_e
    create_fx(fx)
    output = ''
    i = -1
    while(e_last == None or e<e_last):
        i+=1
        aret, fa, bret, fb, c, fc, e_last = result_division_line()
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

    fx = ''
    a = 0
    b = 0
    e = 0
    e_last = None
    xn=0
    bx=0

    return output

def chord(take_a, take_b, take_e, take_fx, proizfx=0):
    global a, b, fx, e, e_last, xn
    create_sy(proizfx)
    create_calc_sy(fxsy())
    import proiz
    import proiz_calcul
    a = take_a
    b = take_b
    fx = take_fx
    e = take_e
    create_fx(fx)
    output = ''
    i=-1
    if calculate(a)>0:
        mode=True
        xn = b
    else:
        mode=False
        xn = a

    while(e_last == None or e<e_last):
        i+=1
        if i == 0:
            e_last=0
            xn, fxn, bx, e_last = result_chord_line(True,mode)
        else:
            xn, fxn, bx, e_last = result_chord_line(mode=mode)
        #вывод переменных в таблицу
    fx = ''
    a = 0
    b = 0
    e = 0
    e_last = None
    xn=0
    bx=0

def tangent(take_a, take_b, take_e, take_fx, proizfx=0):
    global a, b, fx, e, e_last, xn
    create_sy(proizfx)
    import proiz
    create_calc_sy(fxsy())
    import proiz_calcul
    create_sy_2(proizfx)
    import proiz_2
    create_calc_sy_2(fxsy())
    import proiz_calcul_2
    a = take_a
    b = take_b
    fx = take_fx
    e = take_e
    create_fx(fx)
    output = ''
    i=-1
    if ((calculate(a)>0 and fxsy_2(a)>0) or (calculate(a)<0 and fxsy_2(a)<0))==False:
        xn=a
    elif ((calculate(b)>0 and fxsy_2(b)>0) or (calculate(b)<0 and fxsy_2(b)<0))==False:
        xn = b
    else:
        return 'Данным способом невозможно решить уриавнение'

    while(e_last == None or e<e_last):
        i+=1
        xn, fx, bx, e_last = result_tanget()

    fx = ''
    a = 0
    b = 0
    e = 0
    e_last = None
    xn=0
    bx=0
    fxsy=''
