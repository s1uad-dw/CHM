import importlib
import os

def create_script(script, name):
    my_file = open(name + '.py', 'w')
    my_file.write(script)
    my_file.close()

def create_excel(name, values, title):
    import openpyxl
    book = openpyxl.Workbook()
    sheet = book.active
    row = 1
    len(title)>0 and values.insert(0, title)
    while len(values)>0:
        for i in range(len(values[0])):
            sheet.cell(row = row, column=i+1).value = (values[0])[i]
        values.remove(values[0])
        row+=1
    book.save(name + '.xlsx')
    book.close()
    return name

def round_function(value_float, e):
    value = []
    for i in str(value_float):
        value.append(i)
    e += (value.index('.')+1)
    #e = 3
    #0.0945
    #e = 6
    # if value[0] != '-':
    if len(value)>=e+1:
        if value[e]=='5' and len(value)==e+1:
            value[e-1] = str(int(value[e-1])+1) if int(value[e-1])%2!=0 else str(value[e-1])
        else:
            value[e-1] = str(int(value[e-1])+1) if int(value[e])>=5 else str(value[e-1])
            if value[e] == 9:
                value[e] = '0' if int(value[e])>=5 else str(value[e])
    else:
        while len(value)<e:
            value.append('0')
    value_str = ''
    for i in value[:e]:
        value_str+=i
    return float(value_str)
print(round_function(0.0945, 3))
    # else:
    #     if len(value)>e:
    #         if value[e]==5 and len(value)<+1:
    #             value[e-1] = str(int(value[e-2])+1) if int(value[e-1])%2!=0 else value[e-1]
    #         else:   
    #             value[e-1] = str(int(value[e-1])+1) if int(value[e-1])>5 else value[e-1]
    #     else:
    #         while len(value)<e+1:
    #             value.append('0')
    #     value_str = ''
    #     for i in value[:e-1]:
    #         value_str+=i
    #     return float(value_str)

def derivative(expression, argument, serial_number, value):
    print(type(expression))
    for i in range(serial_number):
        expression = expression.replace('math', 'sym')
        create_script('''import math
import sympy as sym
def derivative_calculation(argument):
    symbol = sym.Symbol(argument)
    function = '''+expression.replace(argument, 'symbol')+'''
    return str(function.diff(symbol))''', 'derivative')
        import derivative
        importlib.reload(derivative)
        expression = derivative.derivative_calculation(argument) if expression != '0' else '0'
        for i in ['cos', 'sin']:
            expression = expression.replace(i, 'math.'+i)
    # os.remove('derivative')
    create_script('''def derivative_calculation(x):
    import math
    return ''' + expression, 'derivative')
    import derivative
    importlib.reload(derivative)
    return derivative.derivative_calculation(value)

def result_tanget():
    import general_functions
    import fx
    if e_last == None:
        e_last =  0
    xn = xn-e_last
    fxn=fx.fx(xn)
    f1x=general_functions.derivative(fxn, 'x', 1, xn)
    e_last=fxn/f1x
    return xn, fxn, f1x, e_last