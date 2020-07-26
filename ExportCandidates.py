from typing import Dict

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from Candidate import Candidate


def export_candidates(workbook: Workbook, candidates: Dict[str, Candidate]):
    worksheet: Worksheet = workbook.create_sheet("результат")
    worksheet['A1'] = "Вакансия"
    worksheet['B1'] = "Ответственный за вакансию"
    worksheet['C1'] = "Создатель вакансии"
    worksheet['D1'] = "Дата создания вакансии"
    worksheet['E1'] = "Заказчик"
    worksheet['F1'] = "Источник"
    worksheet['G1'] = "Ссылка на резюме"
    worksheet['H1'] = "Способ занесения"
    worksheet['I1'] = "Дата создания кандидата"
    worksheet['J1'] = "Создатель кандидата"
    worksheet['K1'] = "Ответственный за кандидата"
    worksheet['L1'] = "Фамилия"
    worksheet['M1'] = "Имя"
    worksheet['N1'] = "Отчество"
    worksheet['O1'] = "Регион"
    worksheet['P1'] = "Возраст"
    worksheet['Q1'] = "Дата Рождения"
    worksheet['R1'] = "Email"
    worksheet['S1'] = "Skype"
    worksheet['T1'] = "Контакты"
    worksheet['U1'] = "Телефон"
    worksheet['V1'] = "Зарплата"
    worksheet['W1'] = "История"
    worksheet['X1'] = "Комментарий - Email"
    worksheet['Y1'] = "Комментарий - Phone"
    out_row = 2
    for local_id, candidate in candidates.items():
        worksheet[f'A{out_row}'] = "Название вакансии"  # сюды пиши название вакансии - например "импорт"
        worksheet[f'B{out_row}'] = "Ответственный за вакансию"  # сюды имя ответственного за вакансию
        worksheet[f'C{out_row}'] = "Создатель вакансии"  # сюды имя ответственного за вакансию
        worksheet[f'D{out_row}'] = "Дата создания вакансии"  # сюды дату создания вакансии в формате 15.06.2014
        worksheet[f'E{out_row}'] = "Заказчик"  # сюды заказчика
        worksheet[f'F{out_row}'] = candidate.linkedin_is_link
        worksheet[f'G{out_row}'] = candidate.linkedin
        worksheet[f'H{out_row}'] = candidate.status
        worksheet[f'I{out_row}'] = candidate.date_of_adding
        worksheet[f'J{out_row}'] = "Создатель кандидата"  # сюды создателя кандидата
        worksheet[f'K{out_row}'] = "Ответственный за кандидата"  # сюды создателя кандидата
        worksheet[f'L{out_row}'] = candidate.last_name
        worksheet[f'M{out_row}'] = candidate.first_name
        worksheet[f'N{out_row}'] = candidate.patronymic
        worksheet[f'O{out_row}'] = candidate.region
        worksheet[f'P{out_row}'] = None  # ничего не пиши
        worksheet[f'Q{out_row}'] = candidate.birth_date
        worksheet[f'R{out_row}'] = candidate.email
        worksheet[f'S{out_row}'] = candidate.skype
        worksheet[f'T{out_row}'] = None
        worksheet[f'U{out_row}'] = candidate.phone
        worksheet[f'V{out_row}'] = candidate.salary
        worksheet[f'X{out_row}'] = candidate.email_comment
        worksheet[f'Y{out_row}'] = candidate.phone_comment
        # worksheet[f'W{out_row}'] = candidate.comments(list=['all_text'])
        # worksheet[f'W{out_row}'] = candidate.comments(list) <--- Как выгрузить смерженные столбцы комментариев
        # WHEN-WHO-TEXT? Как создать количество столбцов равно максимальному количеству комментариев среди всех
        # кандидатов? Я бы попробовал посмотреть максимальное количество пустых строк между двумя заполненными. Например
        # через увеличение значения переменной

        out_row = out_row + 1
