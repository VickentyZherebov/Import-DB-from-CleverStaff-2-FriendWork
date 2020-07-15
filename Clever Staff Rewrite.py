from openpyxl import load_workbook, Workbook

# загружаем эксель файл который надо пересобрать
from Candidate import Candidate


def load_candidates(workbook: Workbook):
    candidates_sheet = workbook['кандидаты']

    # Узнаем количество заполненных строк на странице "кандидаты",
    # вычетаем строку с заголовком и получаем количество кандидатов
    number_of_candidates = candidates_sheet.max_row - 1
    print(f'Количество кандидатов {number_of_candidates}')

    candidates = {}
    for row_number in range(2, number_of_candidates + 1):
        number = candidates_sheet[f'A{row_number}'].value
        first_name = candidates_sheet[f'B{row_number}'].value
        patronymic = candidates_sheet[f'C{row_number}'].value
        last_name = candidates_sheet[f'D{row_number}'].value
        desired_position = candidates_sheet[f'E{row_number}'].value
        current_position = candidates_sheet[f'F{row_number}'].value
        current_place = candidates_sheet[f'G{row_number}'].value
        birth_date = candidates_sheet[f'H{row_number}'].value
        sex = candidates_sheet[f'I{row_number}'].value
        status = candidates_sheet[f'J{row_number}'].value
        phone = candidates_sheet[f'K{row_number}'].value
        email = candidates_sheet[f'L{row_number}'].value
        skype = candidates_sheet[f'M{row_number}'].value
        facebook = candidates_sheet[f'N{row_number}'].value
        linkedin = candidates_sheet[f'O{row_number}'].value
        type_of_employment = candidates_sheet[f'P{row_number}'].value
        field_of_activity = candidates_sheet[f'Q{row_number}'].value
        work_experience = candidates_sheet[f'R{row_number}'].value
        salary = candidates_sheet[f'S{row_number}'].value
        currency = candidates_sheet[f'T{row_number}'].value
        language = candidates_sheet[f'U{row_number}'].value
        region = candidates_sheet[f'V{row_number}'].value
        date_of_adding = candidates_sheet[f'Z{row_number}'].value
        local_id = candidates_sheet[f'AB{row_number}'].value
        candidates[local_id] = Candidate(
            number, first_name, patronymic, last_name, desired_position, current_position, current_place,
            birth_date, sex, status, phone, email, skype, facebook, linkedin, type_of_employment,
            field_of_activity, work_experience, salary, currency, language,
            region, date_of_adding, local_id)

    return candidates


workbook = load_workbook('AIHUB.xlsx')
candidates = load_candidates(workbook)

