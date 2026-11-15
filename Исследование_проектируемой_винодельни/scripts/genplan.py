"""Предварительная схема генплана 100 × 75 м (учебная, не официальный генплан).

Список объектов OBJ используется и для рисунка, и для подсчёта площадей
(build_genplan_table печатает таблицу для 07_Генплан).
Запуск: python genplan.py → ../img/genplan_shema.png
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent.parent / "img" / "genplan_shema.png"
OUT.parent.mkdir(exist_ok=True)

W, H = 100, 75

# № , название, x0, y0, ширина(x), высота(y), этажей, входит в площадь застройки, цвет
OBJ = [
    # Главный производственный корпус 60 × 30 м (x 20–80, y 25–55)
    (1, "Приёмно-\nпрессовое\nотделение", 20, 25, 12, 18, 1, True, "#f4cccc"),
    (2, "Мойка тары,\nCIP,\nкомпрессорная,\nазот", 20, 43, 12, 12, 1, True, "#d9d2e9"),
    (3, "Бродильно-хранильное\nотделение\n(ёмкости ≈255 м³)", 32, 25, 24, 18, 1, True, "#cfe2f3"),
    (4, "Бочковый погреб\n(≈180 бочек)", 32, 43, 18, 12, 1, True, "#fce5cd"),
    (5, "Лаборатория, ГРЩ,\nтепловой пункт", 50, 43, 6, 12, 1, True, "#d9ead3"),
    (6, "Цех розлива", 56, 25, 12, 15, 1, True, "#fff2cc"),
    (7, "Склад\nстеклотары\nи сухих\nматериалов", 56, 40, 12, 15, 1, True, "#eeeeee"),
    (8, "Склад готовой\nпродукции", 68, 25, 12, 22, 1, True, "#ead1dc"),
    (9, "Экспедиция,\nрампа", 68, 47, 12, 8, 1, True, "#ead1dc"),
    # Отдельные объекты
    (10, "Навес приёмки\nвинограда,\nвесы", 8, 31, 12, 15, 1, True, "#f4cccc"),
    (11, "АБК (2 эт.),\nдегустационный зал", 22, 3, 16, 8, 2, True, "#d9ead3"),
    (12, "КПП", 41, 0.5, 4, 3, 1, True, "#cccccc"),
    (13, "Чиллеры\n(площадка)", 36, 55.5, 10, 3.5, 1, True, "#cfe2f3"),
    (14, "2КТП 10/0,4 кВ", 85, 3, 6, 4, 1, True, "#ffd966"),
    (15, "ДГУ", 85, 8.5, 6, 3, 1, True, "#ffd966"),
    (16, "Насосная станция\n(хоз. и пожарная)", 81, 62, 6, 5, 1, True, "#9fc5e8"),
    (17, "Пожарные\nрезервуары\n2×100 м³", 88, 66, 10, 7, 1, True, "#9fc5e8"),
    (18, "Локальные\nочистные\nсооружения", 2, 64, 14, 9, 1, True, "#b6d7a8"),
    (19, "Площадка выжимок\nи отходов", 2, 48, 6, 10, 1, True, "#b6d7a8"),
    (20, "Бокс БПЛА\nи АКБ", 2, 3, 6, 6, 1, True, "#cccccc"),
]
# Не входят в площадь застройки (дороги, стоянки) — только для рисунка
ROADS = [
    ("Проезд (юг)", 2, 14, 92, 6),
    ("Проезд (север)", 2, 60, 78, 6),
    ("Проезд (запад)", 2, 14, 6, 52) ,
    ("Проезд (восток)", 88, 14, 6, 52),
    ("Въезд", 45, 0, 7, 14),
]
PARK = ("Стоянка (12 м/м)", 52, 3, 30, 8)


def clean(name):
    return name.replace("-\n", "-").replace("\n", " ")


def area_table():
    rows = []
    for n, name, x, y, w, h, fl, inc, _ in OBJ:
        rows.append((n, clean(name), w, h, w * h, fl, w * h * fl, inc))
    return rows


def draw():
    fig, ax = plt.subplots(figsize=(15, 9.2))
    ax.add_patch(Rectangle((0, 0), W, H, fill=False, lw=2.5, ec="black"))
    for name, x, y, w, h in ROADS:
        ax.add_patch(Rectangle((x, y), w, h, fc="#e0e0e0", ec="none", zorder=1))
    x, y, w, h = PARK[1:]
    ax.add_patch(Rectangle((x, y), w, h, fc="#efefef", ec="#999", ls="--", zorder=1))
    ax.text(x + w / 2, y + h / 2, PARK[0], ha="center", va="center", fontsize=8)
    ax.add_patch(Rectangle((20, 25), 60, 30, fill=False, lw=2.2, ec="#1f4e78", zorder=3))
    for n, name, x, y, w, h, fl, inc, col in OBJ:
        ax.add_patch(Rectangle((x, y), w, h, fc=col, ec="#333", lw=0.8, zorder=2))
        short = w < 10 or h < 6
        lab = f"{n}" if short else f"{n}. {name}"
        ax.text(x + w / 2, y + h / 2, lab, ha="center", va="center", fontsize=11 if short else 8,
                weight="bold" if short else "normal", zorder=4)
    ax.text(50, 22.3, "Главный производственный корпус 60 × 30 м", ha="center", fontsize=9, color="#1f4e78", weight="bold")
    ax.annotate("Въезд с автодороги", xy=(48.5, 0), xytext=(48.5, -5), ha="center", fontsize=9,
                arrowprops=dict(arrowstyle="->"))
    ax.text(W + 1, H, "С\n↑", fontsize=14, va="top")
    ax.set_xlim(-3, W + 42)
    ax.set_ylim(-8, H + 3)
    ax.set_aspect("equal")
    ax.set_xticks(range(0, 101, 10))
    ax.set_yticks(range(0, 76, 5))
    ax.grid(alpha=0.25)
    ax.set_xlabel("м")
    ax.set_ylabel("м")
    ax.set_title("Предварительная схема генплана нового винзавода на участке 100 × 75 м (0,75 га)\n"
                 "Учебная схема для дипломного проектирования — не официальный генплан и не план Arba Wine",
                 fontsize=11)
    leg = "\n".join(f"{n}. {name.replace(chr(10), ' ')}" for n, name, x, y, w, h, *_ in OBJ if w < 10 or h < 6)
    ax.text(W + 3, 45, leg, fontsize=8, va="top", ha="left",
            bbox=dict(fc="white", ec="#999"))
    fig.tight_layout()
    fig.savefig(OUT, dpi=150)
    print("saved", OUT)


if __name__ == "__main__":
    draw()
    tot = 0
    for r in area_table():
        print(r)
        tot += r[4] if r[7] else 0
    print("Площадь застройки:", tot, "м²; плотность", round(tot / 7500 * 100, 1), "%")
