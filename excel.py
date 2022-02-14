import openpyxl

def create_excel(name, values):
    book = openpyxl.Workbook()
    sheet = book.active
    row = 1
    while len(values)>0:
        for i in range(1, len(values[0])+1):
            sheet[row][i] = values[i]
            values.remove(values.index(0))
    row+=1
    book.save(name+'xlsx')
    book.close()