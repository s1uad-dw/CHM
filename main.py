import os
import math

fx = ''
def str_to_list(value_str):
    value = []
    for i in value_str:
        value.append(i)
    return value

def list_to_str(value):
    value_str = ''
    for i in value:
        value_str+=i
    return value_str

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
        
def input_function():
    global fx 
    a = int(input('Введите а: '))
    b = int(input('Введите b: '))
    fx = str(input('Введите функцию:\nf(x)='))

def calculate_fx(x):
    my_file = open('helper.py', 'w')
    text_for_file = 'def calculate(x):\n\treturn '+fx
    my_file.write(text_for_file)
    my_file.close()
    import helper
    return helper.calculate(x)

def print_help():
    print('#Подсказка')
    print('#')
    print('#match')
    print('#    .pi         число пи')
    print('#    .exp(x)     экспонента числа е^x')
    print('#    .log(x, y)  лог х по основанию у')
    print('#    .pow(x, y)  x - число у - стерпень')
    print('#')
    print('#    .sin(x)')
    print('#    .cos(x)')
    print('#    .tan(x)')
    print('#    .atan(x)    инверсия')
    print('#')
    print('#    .degrees(x) из градусов в радианы')
    print('#    .radians(x) из радианов в градусы')
