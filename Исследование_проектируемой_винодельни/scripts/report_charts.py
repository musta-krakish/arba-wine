"""Графики для 00_Краткий_отчет: значения считаются из формул 04 библиотекой formulas."""
import re
from pathlib import Path
import formulas
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
xl = formulas.ExcelModel().loads(str(ROOT / "04_График_работы_и_нагрузок.xlsx")).finish()
sol = xl.calculate()
V = {}
for k, v in sol.items():
    m = re.match(r"'\[(.+)\](.+)'!([A-Z]+)(\d+)$", k)
    if m:
        try:
            V[(m.group(2).upper(), m.group(3), int(m.group(4)))] = v.value[0][0]
        except Exception:
            pass

cols = [c for c in "DEFGHIJKLMNOPQRSTUVWXYZ"] + ["AA"]


def row_by_label(sheet, label):
    for (s, c, r), v in V.items():
        if s == sheet.upper() and c == "A" and v == label:
            return r


days = {"СУТКИ_ПИК_ПЕРЕРАБОТКИ": "Пиковые сутки переработки (сентябрь)", "СУТКИ_РОЗЛИВ": "Сутки розлива (апрель)",
        "СУТКИ_ЗИМА": "Зимние сутки (январь)", "СУТКИ_ЛЕТО": "Летние сутки с орошением (июль)"}
fig, ax = plt.subplots(figsize=(10, 4.6))
out = {}
for sh, nm in days.items():
    r = row_by_label(sh, "ВСЕГО, кВт")
    y = [float(V[(sh, c, r)]) for c in cols]
    out[sh] = y
    ax.step(range(25), y + [y[-1]], where="post", label=nm, lw=2 if "ПИК" in sh else 1.4)
ax.set_xlim(0, 24)
ax.set_xticks(range(0, 25, 2))
ax.set_xlabel("Час суток")
ax.set_ylabel("P, кВт")
ax.grid(alpha=0.3)
ax.legend(fontsize=8, loc="upper left")
ax.set_title("Суточные графики нагрузки (проектные, РАСЧЁТНОЕ; 04_График)")
fig.tight_layout()
fig.savefig(ROOT / "img" / "graf_sutki.png", dpi=160)

r0 = row_by_label("ГОД", "Янв")
mon = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]
pl = [float(V[("ГОД", "H", r0 + i)]) for i in range(12)]
irr = [float(V[("ГОД", "K", r0 + i)]) for i in range(12)]
dr = [float(V[("ГОД", "N", r0 + i)]) for i in range(12)]
fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(mon, pl, label="Завод")
ax.bar(mon, irr, bottom=pl, label="Орошение (RDI)")
ax.bar(mon, dr, bottom=[a + b for a, b in zip(pl, irr)], label="БПЛА")
ax.set_ylabel("МВт·ч")
ax.set_title("Помесячное электропотребление (РАСЧЁТНОЕ; 04_График, лист «Год»)")
ax.legend(fontsize=8)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig(ROOT / "img" / "graf_god.png", dpi=160)
for sh, y in out.items():
    print(sh, round(max(y), 1), round(sum(y), 0))
print("year plant", round(sum(pl), 1), "irr", round(sum(irr), 1), "drone", round(sum(dr), 2))
