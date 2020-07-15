from openpyxl import load_workbook
from openpyxl.utils import get_column_letter, column_index_from_string

# загружаем эксель файл который надо пересобрать
wb = load_workbook('AIHUB.xlsx')

# Загружаем модуль OS - он поможет открывать Excel файл в конце работы программы с помощью (os.startfile('AIHUB.xlsx'))
import os

# Запоминаем и выводим названия листов
sn = wb.sheetnames
print(f'1. В документе есть следующие листы -{sn}')

# Выводим название активного листа
print(f'2. Активный лист на данный момент -"{wb.active.title}"')

# Делаем активным лист с номером 0 и выводим его название
wb.active = 0
print(f'3. Делаем активным лист с номером 0 и выводим его название - "{wb.active.title}"')

# Узнаем количество заполненных строк на странице "кандидаты",
# вычетаем строку с заголовком и получаем количество кандидатов
maxcolumn = wb['кандидаты'].max_row
print(f'4. Количество строк на странице "кандидаты" равно - {maxcolumn}')
number_of_candidates = maxcolumn - 1
print(f'5. Количество кандидатов должно быть меньше количества строк на единицу (заголовок) и равно - '
      f'{number_of_candidates}')


# Вызываем Candidate Class
class Candidate:
    def __init__(self, number, first_name, patro_nymic, last_name, desired_position, current_position, current_place,
                 birth_date, sex, status, phone, email, skype, facebook, linkedin, type_of_employment,
                 field_of_activity, work_experience, salary, currency, language, language_level, region, date_of_adding,
                 local_id, action_date, action_creator, action, comment_date, comment_creator, comment):
        self.number = number
        self.first_name = first_name
        self.patro_nymic = patro_nymic
        self.last_name = last_name
        self.desired_position = desired_position
        self.current_position = current_position
        self.current_place = current_place
        self.birth_date = birth_date
        self.sex = sex
        self.status = status
        self.phone = phone
        self.email = email
        self.skype = skype
        self.facebook = facebook
        self.linkedin = linkedin
        self.type_of_employment = type_of_employment
        self.field_of_activity = field_of_activity
        self.work_experience = work_experience
        self.salary = salary
        self.currency = currency
        self.language = language
        self.language_level = language_level
        self.region = region
        self.date_of_adding = date_of_adding
        self.local_id = local_id
        self.action_date = action_date
        self.action_creator = action_creator
        self.action = action
        self.comment_date = comment_date
        self.comment_creator = comment_creator
        self.comment = comment


letter_number = 1
print('_________________________________________________')
while letter_number <= maxcolumn:
    print(f'6. Cтартовое значение = {letter_number}')
    number = wb.active[f'A{letter_number}'].value
    first_name = wb.active[f'B{letter_number}'].value
    patro_nymic = wb.active[f'C{letter_number}'].value
    last_name = wb.active[f'D{letter_number}'].value
    desired_position = wb.active[f'E{letter_number}'].value
    current_position = wb.active[f'F{letter_number}'].value
    current_place = wb.active[f'G{letter_number}'].value
    birth_date = wb.active[f'H{letter_number}'].value
    sex = wb.active[f'I{letter_number}'].value
    status = wb.active[f'J{letter_number}'].value
    phone = wb.active[f'K{letter_number}'].value
    email = wb.active[f'L{letter_number}'].value
    skype = wb.active[f'M{letter_number}'].value
    facebook = wb.active[f'N{letter_number}'].value
    linkedin = wb.active[f'O{letter_number}'].value
    type_of_employment = wb.active[f'P{letter_number}'].value
    field_of_activity = wb.active[f'Q{letter_number}'].value
    work_experience = wb.active[f'R{letter_number}'].value
    salary = wb.active[f'S{letter_number}'].value
    currency = wb.active[f'T{letter_number}'].value
    language = wb.active[f'U{letter_number}'].value
    language_level = wb.active[f'U{letter_number}'].value
    region = wb.active[f'V{letter_number}'].value
    date_of_adding = wb.active[f'Z{letter_number}'].value
    local_id = wb.active[f'AB{letter_number}'].value
    # делаем активным лист с Историей по кадидатам

    wb.active = 1
    ln = 3
    while wb.active[f'D{ln}'].value == str(local_id):
        print('я чет нашел')
        print(wb.active[f'D{ln}'].value)
        ln = ln + 1
    wb.active = 0


    #for i in range (3, 6052)
    #    in


    # ws = wb.active
    # for row in ws.iter_rows(2, 6052, 4, 4, "D"):
    #     for cell in row:
    #         if cell == local_id:
    #             print(ws.cell(cell.row, 4).value)
    # wb.active = 0
    action_date = wb.active[f'W{letter_number}'].value
    action_creator = wb.active[f'X{letter_number}'].value
    action = wb.active[f'Y{letter_number}'].value
    comment_date = wb.active[f'Z{letter_number}'].value
    comment_creator = wb.active[f'A{letter_number}'].value
    comment = wb.active[f'B{letter_number}'].value
    candidate = Candidate(number, first_name, patro_nymic, last_name, desired_position, current_position, current_place,
                          birth_date, sex, status, phone, email, skype, facebook, linkedin, type_of_employment,
                          field_of_activity, work_experience, salary, currency, language, language_level,
                          region, date_of_adding, local_id, action_date, action_creator, action, comment_date,
                          comment_creator, comment)
    print(candidate.number)
    print(candidate.first_name)
    print(candidate.patro_nymic)
    print(candidate.last_name)
    print(candidate.desired_position)
    print(candidate.current_position)
    print(candidate.current_place)
    print(candidate.birth_date)
    print(candidate.sex)
    print(candidate.status)
    print(candidate.phone)
    print(candidate.email)
    print(candidate.skype)
    print(candidate.facebook)
    print(candidate.linkedin)
    print(candidate.type_of_employment)
    print(candidate.field_of_activity)
    print(candidate.work_experience)
    print(candidate.salary)
    print(candidate.currency)
    print(candidate.language)
    print(candidate.region)
    print(candidate.date_of_adding)
    print(candidate.local_id)
    print(candidate.action_date)
    print(candidate.action_creator)
    print(candidate.action)
    print(candidate.comment_date)
    print(candidate.comment_creator)
    print(candidate.comment)
    print("____________________________________________")
#    for row in wb['история'].iter_rows("D"):
#        for cell in row:
#            if cell.value == local_id:
#                print(wb['история'].cell(row=cell.row, column=5).value)  # change column number for any cell value
    letter_number = letter_number + 1

    # Сохраняем проделанную работу в файл
    # wb.save('AIHUB.xlsx')

    # Открываем файл с помощью программы, указанной в реестре Windows для файлов этого типа
    # os.startfile('AIHUB.xlsx')
