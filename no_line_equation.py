import general_functions
import importlib
import os

def half_division(a, b, e, fx):
    general_functions.create_script(
'''def fx(x):
    import math
    return ''' + fx, 'fx')
    import fx
    importlib.reload(fx)
    values = []
    i = -1
    e_last = None
    while(e_last == None or e<e_last):
        i+=1
        fa = general_functions.round_function(fx.fx(a), e)
        fb = general_functions.round_function(fx.fx(b), e)
        c = general_functions.round_function(((a+b)/2), e)
        fc = general_functions.round_function(fx.fx(c), e)
        e_last = general_functions.round_function((b-a), e)

        values.append([i, a, fa, b, fb, c, fc, e_last])
        if fa*fc<0:
            b = c
        elif fb*fc<0:
            a = c
        i > 1 or 'ERROR'
    return values
# derivative - производная
def chord (a, b, e, fx):
    general_functions.create_script(
'''def fx(x):
    import math
    return ''' + fx, 'fx')
    import fx
    importlib.reload(fx)
    xn = b if fx.fx(a) and general_functions.derivative(fx, 'x', 2) else a
    n = -1
    e_last = None
    values = []
    while (e_last == None or e < e_last):
        n += 1
        xn = general_functions.round_function(b-a, e)



