import sys,openpyxl
wb=openpyxl.load_workbook(sys.argv[1],data_only=True)
for ws in wb:
  print('##',ws.title,ws.max_row,ws.max_column)
  for r in ws.iter_rows(values_only=True):
    if any(c is not None for c in r): print(' | '.join('' if c is None else str(c) for c in r))
