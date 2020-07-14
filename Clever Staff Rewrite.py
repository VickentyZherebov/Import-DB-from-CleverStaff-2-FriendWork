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
    a = wb.active[f'A{letternumber}'].value
    b = wb.active[f'B{letternumber}'].value
    c = wb.active[f'C{letternumber}'].value
    d = wb.active[f'D{letternumber}'].value
    e = wb.active[f'E{letternumber}'].value
    f = wb.active[f'F{letternumber}'].value
    g = wb.active[f'G{letternumber}'].value
    h = wb.active[f'H{letternumber}'].value
    i = wb.active[f'I{letternumber}'].value
    j = wb.active[f'J{letternumber}'].value
    k = wb.active[f'K{letternumber}'].value
    l = wb.active[f'L{letternumber}'].value
    m = wb.active[f'M{letternumber}'].value
    n = wb.active[f'N{letternumber}'].value
    o = wb.active[f'O{letternumber}'].value
    p = wb.active[f'P{letternumber}'].value
    q = wb.active[f'Q{letternumber}'].value
    r = wb.active[f'R{letternumber}'].value
    s = wb.active[f'S{letternumber}'].value
    t = wb.active[f'T{letternumber}'].value
    u = wb.active[f'U{letternumber}'].value
    v = wb.active[f'V{letternumber}'].value
    w = wb.active[f'W{letternumber}'].value
    x = wb.active[f'X{letternumber}'].value
    y = wb.active[f'Y{letternumber}'].value
    z = wb.active[f'Z{letternumber}'].value

    FirstCanidate = Candidate(a, b, c, d, e, f, g, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w,
                              x, y, z, "test", "test", "test", "test", "test")
    print(FirstCanidate.number)
    print(FirstCanidate.firstname)
    print(FirstCanidate.patronymic)
    print(FirstCanidate.lastname)
    print(FirstCanidate.desiredposition)
    print(FirstCanidate.currentplace)
    print(FirstCanidate.birthdate)
    print(FirstCanidate.sex)
    print(FirstCanidate.status)
    print(FirstCanidate.phone)
    print(FirstCanidate.email)
    print(FirstCanidate.skype)
    print(FirstCanidate.facebook)
    print(FirstCanidate.linkedin)
    print(FirstCanidate.typeofemployment)
    print(FirstCanidate.fieldofactivity)
    print(FirstCanidate.workexperience)
    print(FirstCanidate.salary)
    print(FirstCanidate.currency)
    print(FirstCanidate.language)
    print("____________________________________________")
    letternumber = letternumber + 1

    # Сохраняем проделанную работу в файл
    # wb.save('AIHUB.xlsx')

    # Открываем файл с помощью программы, указанной в реестре Windows для файлов этого типа
    # os.startfile('AIHUB.xlsx')
