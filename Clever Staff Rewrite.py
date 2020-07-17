import re
from openpyxl import load_workbook
from LoadCandidates import load_candidates, load_history

workbook = load_workbook('AIHUB.xlsx')
candidates = load_candidates(workbook)
load_history(workbook, candidates)

# for local_id, candidate in list(candidates.items())[10:20]:
#     print(candidate)

for local_id, candidate in candidates.items():
    if candidate.phone_comment is not None:
        print(f'{local_id}: {candidate.phone_comment}')
