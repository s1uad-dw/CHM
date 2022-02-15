import general_functions
import importlib
import os
import math
def a_and_b(a, b):
    general_functions.create_script(
'''def a_and_b_calculate(a, b):
    import math
    return '''+ str(a) +', ' + str(b), 'a_and_b_calculate')
    import a_and_b_calculate
    importlib.reload(a_and_b_calculate)
    return a_and_b_calculate.a_and_b_calculate(a, b)


def half_division(a, b, e, fx):
    a, b = a_and_b(a, b)
    general_functions.create_script(
'''def fx_calculate(x):
    import math
    return ''' + fx, 'fx_calculate')
    import fx_calculate
    importlib.reload(fx_calculate)
    values = []
    k = -1
    e_last = None
    while(e_last == None or e<e_last and k<1001):
        k+=1
        fa = general_functions.round_function(fx_calculate.fx_calculate(a), 3)
        fb = general_functions.round_function(fx_calculate.fx_calculate(b), 3)
        c = general_functions.round_function(((a+b)/2), 3)
        fc = general_functions.round_function(fx_calculate.fx_calculate(c), 3)
        e_last = general_functions.round_function((b-a), 3)

        values.append([k, a, fa, b, fb, c, fc, e_last])
        if fa*fc<0:
            b = c
        elif fb*fc<0:
            a = c

    return values if k < 1000 else 'ERROR'

def chord (a, b, e, fx):
    a, b = a_and_b(a, b)
    general_functions.create_script('''def fx_calculate(x):
    import math
    return ''' + fx, 'fx_calculate')
    import fx_calculate
    importlib.reload(fx_calculate)
    n = -1
    e_last = None
    values = []
    if (fx_calculate.fx_calculate(a)>=0 and general_functions.derivative(fx, 'x', 1, a)>=0) or (fx_calculate.fx_calculate(a)<0 and general_functions.derivative(fx, 'x', 1, a)<0):
        xn = b
        bxn = round((a - xn), 15)
    elif (fx_calculate.fx_calculate(b)>=0 and general_functions.derivative(fx, 'x', 1, b)>=0) or (fx_calculate.fx_calculate(b)<0 and general_functions.derivative(fx, 'x', 1, b)<0):
        xn = a
        bxn = round((b - xn), 15)
    else:
        return 'ERROR'
    while (e_last == None or e < float(str(e_last)[1:])):
        n += 1
        fxn = general_functions.round_function(fx_calculate.fx_calculate(xn), 5)
        e_last = general_functions.round_function(-1*(fxn*bxn)/(fx_calculate.fx_calculate(b)-fxn), 5)
        values.append([n, xn, fxn, bxn, e_last])
        xn += e_last
        bxn = general_functions.round_function(b-xn, 5)
        
    return values if n<100 else 'ERROR'