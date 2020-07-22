from openpyxl import load_workbook

from LoadCandidates import load_candidates, load_history, load_comments

workbook = load_workbook('AIHUB.xlsx')
candidates = load_candidates(workbook)
load_history(workbook, candidates)
load_comments(workbook, candidates)

for local_id, candidate in list(candidates.items())[:20]:
    print(candidate)
