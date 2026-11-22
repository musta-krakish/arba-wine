"""Пересчёт формул xlsx (библиотека formulas) и печать листа: python evalx.py файл.xlsx ЛИСТ"""
import sys, re, formulas
fn, sheet = sys.argv[1], sys.argv[2].upper()
sol = formulas.ExcelModel().loads(fn).finish().calculate()
out = {}
for k, v in sol.items():
    m = re.match(r"'\[(.+)\](.+)'!([A-Z]+)(\d+)$", k)
    if not m or m.group(2).upper() != sheet:
        continue
    try:
        val = v.value[0][0]
    except Exception:
        val = v
    out[(int(m.group(4)), m.group(3))] = val
for r in sorted(set(r for r, _ in out)):
    cells = sorted(((c, out[(r, c)]) for rr, c in out if rr == r), key=lambda x: (len(x[0]), x[0]))
    print(r, " | ".join(f"{c}={round(v, 3) if isinstance(v, (int, float)) else v}" for c, v in cells))
