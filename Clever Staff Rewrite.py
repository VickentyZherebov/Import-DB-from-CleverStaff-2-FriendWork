from openpyxl import load_workbook

# загружаем эксель файл который надо пересобрать
wb = load_workbook('AIHUB.xlsx')

# Загружаем модуль OS - он поможет открывать Excel файл в конце работы программы с помощью (os.startfile('AIHUB.xlsx'))
import os

# Запоминаем и выводим названия листов
sn = wb.sheetnames
print(f'1. В документе есть следующие листы -{sn}')

# Выводим название активного листа
print(f'2. Активный лист на данный момент -"{wb.active.title}"')

# Делаем активным лист с номером 4 и выводим его название
wb.active = 4
print(f'3. Делаем активным лист с номером 4 и выводим его название - "{wb.active.title}"')

# Узнаем количество заполненных строк на странице "кандидаты", вычетаем строку с заголовком и получаем количество кандидатов
maxcolumn = wb['кандидаты'].max_row
print(f'4. Количество строк на странице "кандидаты" равно - {maxcolumn}')
NumberOfCandidates = maxcolumn - 1
print(f'5. Количество кандидатов должно быть меньше количества строк на единицу (заголовок) и равно - {NumberOfCandidates}')

# Сохраняем проделанную работу в файл
wb.save('AIHUB.xlsx')

# Открываем файл с помощью программы, указанной в реестре Windows для файлов этого типа
os.startfile('AIHUB.xlsx')