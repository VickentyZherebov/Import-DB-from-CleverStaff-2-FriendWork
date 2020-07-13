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
    def __init__(self, number, lastname, patronymic, desiredposition, currentplace, birthdate,
                 sex, status, phone, email, skype, facebook, linkedin, typeofemployment, fieldofactivity,
                 workexperience, salary, currency, language, languagelevel, region, dateofadding, candidateid,
                 actiondate, actioncreator, action, commentdate, commentcreator, comment):
        self.number = number
        self.lastname = lastname
        self.patronymic = patronymic
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

a2 = wb.active['A2'].value
b2 = wb.active['B2'].value
print(a2)

FirstCanidate = Candidate(a2, b2, "test", "test", "test", "test", "test", "test", "test", "test", "test",
                          "test", "test", "test", "test", "test", "test", "test", "test", "test", "test", "test",
                          "test", "test", "test", "test", "test", "test", "test")
print(FirstCanidate.lastname)
        

# Сохраняем проделанную работу в файл
wb.save('AIHUB.xlsx')

# Открываем файл с помощью программы, указанной в реестре Windows для файлов этого типа
os.startfile('AIHUB.xlsx')