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
        print(len(values))
        for i in range(len(values[0])):
            print(i+1, row), type(values), type(values[0]), type((values[0])[i])
            sheet.cell(row = row, column=i+1).value = (values[0])[i]
        values.remove(values[0])
        row+=1
    book.save(name + '.xlsx')
    book.close()
    return name



def round_function(value_float, e_float):
    value = []
    for i in str(value_float):
        value.append(i)
    e = []
    for i in str(e_float):
        e.append(i)
    if value[0] != '-':
        if len(value)>len(e)+1:
            if value[len(e)+1]=='5' and len(value)<len(e)+2:
                value[len(e)] = str(int(value[len(e)])+1) if int(value[len(e)])%2!=0 else value[len(e)]
            else:   
                value[len(e)] = str(int(value[len(e)])+2) if int(value[len(e)+1])>5 else value[len(e)]
        else:
            while len(value)<len(e)+2:
                value.append('0')
        value_str = ''
        for i in value[:len(e)+1]:
            value_str+=i
        return float(value_str)
    else:
        if len(value)>len(e)+2:
            if value[len(e)+2]=='5' and len(value)<len(e)+3:
                value[len(e)+1] = str(int(value[len(e)])+1) if int(value[len(e)+1])%2!=0 else value[len(e)+1]
            else:   
                value[len(e)+1] = str(int(value[len(e)+1])+1) if int(value[len(e)+1])>5 else value[len(e)+1]
        else:
            while len(value)<len(e)+3:
                value.append('0')
        value_str = ''
        for i in value[:len(e)+1]:
            value_str+=i
        return float(value_str)

def derivative(expression, argument, serial_number):
    for i in range(serial_number):
        create_script('''import math
import sympy as sym
def derivative_calculation(argument):
    symbol = sym.Symbol(argument)
    function = '''+expression.replace('math', 'sym').replace(argument, 'symbol')+'''
    return str(function.diff(symbol))''', 'derivative')
        import derivative
        importlib.reload(derivative)
        expression = derivative.derivative_calculation(argument) if expression != '0' else '0'
    os.remove('derivative.py')
    return expression