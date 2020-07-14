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

# Делаем активным лист с номером 0 и выводим его название
wb.active = 0
print(f'3. Делаем активным лист с номером 0 и выводим его название - "{wb.active.title}"')

# Узнаем количество заполненных строк на странице "кандидаты",
# вычетаем строку с заголовком и получаем количество кандидатов
maxcolumn = wb['кандидаты'].max_row
print(f'4. Количество строк на странице "кандидаты" равно - {maxcolumn}')
NumberOfCandidates = maxcolumn - 1
print(f'5. Количество кандидатов должно быть меньше количества строк на единицу (заголовок) и равно - {NumberOfCandidates}')


# Создаем класс CandidateClass
class Candidate:
    def __init__(self, number, firstname, patronymic, lastname, desiredposition, currentplace, birthdate,
                 sex, status, phone, email, skype, facebook, linkedin, typeofemployment, fieldofactivity,
                 workexperience, salary, currency, language, languagelevel, region, dateofadding, candidateid,
                 actiondate, actioncreator, action, commentdate, commentcreator, comment):
        self.number = number
        self.firstname = firstname
        self.patronymic = patronymic
        self.lastname = lastname
        self.desiredposition = desiredposition
        self.currentplace = currentplace
        self.birthdate = birthdate
        self.sex = sex
        self.status = status
        self.phone = phone
        self.email = email
        self.skype = skype
        self.facebook = facebook
        self.linkedin = linkedin
        self.typeofemployment = typeofemployment
        self.fieldofactivity = fieldofactivity
        self.workexperience = workexperience
        self.salary = salary
        self.currency = currency
        self.language = language
        self.languagelevel = languagelevel
        self.region = region
        self.dateofadding = dateofadding
        self.candidateid = candidateid
        self.actiondate = actiondate
        self.actioncreator = actioncreator
        self.action = action
        self.commentdate = commentdate
        self.commentcreator = commentcreator
        self.comment = comment

letternumber = 2
print('_________________________________________________')
maxcolumn = 6
while letternumber < maxcolumn:
    print(f'6. Cтартовое значение = {letternumber}')
    a2 = wb.active[f'A{letternumber}'].value
    b2 = wb.active[f'B{letternumber}'].value
    c2 = wb.active[f'C{letternumber}'].value
    d2 = wb.active[f'D{letternumber}'].value

    FirstCanidate = Candidate(a2, b2, c2, d2, "test", "test", "test", "test", "test", "test", "test",
                              "test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                              "test", "test", "test", "test", "test", "test", "test", "test")
    print(FirstCanidate.number)
    print(FirstCanidate.firstname)
    print(FirstCanidate.patronymic)
    print(FirstCanidate.lastname)
    print("____________________________________________")
    letternumber = letternumber + 1

    # Сохраняем проделанную работу в файл
    # wb.save('AIHUB.xlsx')

    # Открываем файл с помощью программы, указанной в реестре Windows для файлов этого типа
    # os.startfile('AIHUB.xlsx')
