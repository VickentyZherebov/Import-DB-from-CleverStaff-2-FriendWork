from typing import Dict

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from Candidate import Candidate


def export_candidates(workbook: Workbook, candidates: Dict[str, Candidate]):
    worksheet: Worksheet = workbook.create_sheet("результат")

    out_row = 1
    for local_id, candidate in candidates.items():
        worksheet[f'A{out_row}'] = candidate.first_name
        out_row = out_row + 1
