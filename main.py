import os
import math

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
    a = str(input('---'))
    my_file = open('oaoa.py', 'w')
    text_for_file = 'def oaoa(a=3, b=4):\n\treturn '+a
    my_file.write(text_for_file)
    my_file.close()


input_function()
import helper
print(helper.calculate())


print(round_function(str_to_list('5.315')))