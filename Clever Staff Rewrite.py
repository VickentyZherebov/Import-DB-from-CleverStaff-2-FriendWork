from openpyxl import load_workbook

# загружаем эксель файл который надо пересобрать
from Candidate import Candidate


def load_candidates(excel_filename):
    wb = load_workbook(excel_filename)
    candidates_sheet = wb['кандидаты']

    # Узнаем количество заполненных строк на странице "кандидаты",
    # вычетаем строку с заголовком и получаем количество кандидатов
    number_of_candidates = candidates_sheet.max_row - 1
    print(f'Количество кандидатов должно быть меньше количества строк на единицу (заголовок) и равно - {number_of_candidates}')

    candidates = {}
    for row_number in range(2, number_of_candidates + 1):
        number = wb.active[f'A{row_number}'].value
        first_name = wb.active[f'B{row_number}'].value
        patro_nymic = wb.active[f'C{row_number}'].value
        last_name = wb.active[f'D{row_number}'].value
        desired_position = wb.active[f'E{row_number}'].value
        current_position = wb.active[f'F{row_number}'].value
        current_place = wb.active[f'G{row_number}'].value
        birth_date = wb.active[f'H{row_number}'].value
        sex = wb.active[f'I{row_number}'].value
        status = wb.active[f'J{row_number}'].value
        phone = wb.active[f'K{row_number}'].value
        email = wb.active[f'L{row_number}'].value
        skype = wb.active[f'M{row_number}'].value
        facebook = wb.active[f'N{row_number}'].value
        linkedin = wb.active[f'O{row_number}'].value
        type_of_employment = wb.active[f'P{row_number}'].value
        field_of_activity = wb.active[f'Q{row_number}'].value
        work_experience = wb.active[f'R{row_number}'].value
        salary = wb.active[f'S{row_number}'].value
        currency = wb.active[f'T{row_number}'].value
        language = wb.active[f'U{row_number}'].value
        language_level = wb.active[f'U{row_number}'].value
        region = wb.active[f'V{row_number}'].value
        date_of_adding = wb.active[f'Z{row_number}'].value
        local_id = wb.active[f'AB{row_number}'].value
        action_date = wb.active[f'W{row_number}'].value
        action_creator = wb.active[f'X{row_number}'].value
        action = wb.active[f'Y{row_number}'].value
        comment_date = wb.active[f'Z{row_number}'].value
        comment_creator = wb.active[f'A{row_number}'].value
        comment = wb.active[f'B{row_number}'].value
        candidates[local_id] = Candidate(
            number, first_name, patro_nymic, last_name, desired_position, current_position, current_place,
            birth_date, sex, status, phone, email, skype, facebook, linkedin, type_of_employment,
            field_of_activity, work_experience, salary, currency, language, language_level,
            region, date_of_adding, local_id, action_date, action_creator, action, comment_date,
            comment_creator, comment)

    return candidates


candidates = load_candidates('AIHUB.xlsx')
print(candidates)
