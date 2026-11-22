"""Раздел сайта «Оборудование: марки, модели, фото».

Источник данных — лист «Ведомость» в 03_Ведомость_электроприемников.xlsx (марки, модели, Pн, количество,
объекты генплана). Фото — scripts/data/photos.json: {id: {"img": URL, "page": URL}}; скачанные и
уменьшенные копии лежат в site/img/eq/<id>.jpg (шаг fetch — `python build_site_eq.py fetch`).

Запуск: python build_site_eq.py [fetch]  → вставляет HTML между <!-- EQ:START --> и <!-- EQ:END --> в site/index.html
"""
import html
import json
import subprocess
import sys
import urllib.parse
from collections import OrderedDict
from pathlib import Path

import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SITE = ROOT.parent / "site"
IMG_DIR = SITE / "img" / "eq"
PHOTOS = HERE / "data" / "photos.json"
XLSX = ROOT / "03_Ведомость_электроприемников.xlsx"

# № ЭП → id фото (одна модель на несколько ЭП — одна карточка)
PHOTO_OF = {
    1: "A1", 2: "A2", 3: "C17", 4: "A3", 6: "A4", 7: "A5",
    8: "C16", 9: "A6", 10: "A7", 11: "A8", 12: "A9", 13: "A10",
    14: "A11", 15: "A11", 16: "A12", 17: "C14", 18: "A13", 19: "A14", 20: "A15", 21: "A16", 22: "A17", 23: "A18",
    24: "A19", 25: "C15", 28: "A20", 29: "A21", 30: "B1", 31: "B2", 34: "B3", 47: "B3", 61: "B3", 35: "B4",
    36: "B5", 37: "B6", 39: "B7", 41: "B8", 42: "B9", 44: "B10", 45: "B11", 46: "B13", 48: "B14",
    50: "B15", 51: "B16", 52: "B18", 56: "B18", 53: "B17", 54: "B19", 55: "B20",
    58: "C2", 59: "C3", 60: "C4", 62: "C5", 63: "C6",
    64: "B22", 65: "C7", 66: "C8", 67: "C9", 68: "C10", 69: "C10", 70: "C11", 72: "C12", 73: "C13",
}
# Объединение строк ведомости в одну карточку (одинаковая модель)
GROUP_KEY = {47: 34, 61: 34, 15: 14, 69: 68}
# Карточки вне листа «Ведомость»: пожарные насосы (лист «Резерв_пожарные»), сама ДГУ (источник, не ЭП), дрон
EXTRA = [
    dict(after=56, ids=["Резерв"], obj="16", name="Насос пожаротушения ВПВ (1 раб. + 1 рез.)",
         maker="Grundfos", model="CR 45-2 A-F-A-E-HQQE (96122799)", p="7,5", qty="2", photo="B21",
         doc="https://www.solarics.de/cdn/shop/files/96122799_CR_452_AFAEHQQE.pdf"),
    dict(after=53, ids=["—"], obj="15", name="Дизель-генератор — резервный источник I и II категорий (не ЭП)",
         maker="Kohler SDMO", model="J88 (80/88 кВА, 400 В)", p="—", qty="1", photo="B17",
         doc="https://techcomm.rehlko.com/techcomm/pdf/g5642.pdf"),
    dict(after=58, ids=["—"], obj="20", name="Агродрон — заряжается от C10000 (сам дрон не ЭП)",
         maker="DJI", model="Agras T50", p="—", qty="1", photo="C1", doc="https://ag.dji.com/t50/specs"),
]
NO_BRAND = ("НЕИЗВЕСТНО", "не выбран", "требует уточнения", "—", "", None)


def fmt(x, nd=2):
    if x is None or x == "":
        return "—"
    if isinstance(x, (int, float)):
        s = f"{x:.{nd}f}".rstrip("0").rstrip(".")
        return s.replace(".", ",")
    return str(x)


def load_rows():
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    ws = wb["Ведомость"]
    hdr, rows = None, []
    for r in ws.iter_rows(values_only=True):
        if hdr is None:
            if r and any(isinstance(c, str) and "Производ" in c for c in r):
                hdr = list(r)
            continue
        if isinstance(r[0], int):
            d = dict(zip(hdr, r))
            rows.append(d)
    return rows


def esc(s):
    return html.escape(str(s), quote=True)


def domain(url):
    try:
        return urllib.parse.urlparse(url).netloc.replace("www.", "")
    except Exception:
        return ""


def fetch(photos):
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    tmp = HERE / "__photo_tmp"
    tmp.mkdir(exist_ok=True)
    for pid, ph in photos.items():
        out = IMG_DIR / f"{pid}.jpg"
        if out.exists() or not ph.get("img"):
            continue
        raw = tmp / f"{pid}.bin"
        jar = tmp / "jar.txt"
        r = subprocess.run(["curl", "-sL", "-m", "40", "-c", str(jar), "-b", str(jar), "-A",
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36",
                            "-e", ph.get("page") or "", "-o", str(raw), "-w", "%{http_code} %{content_type}", ph["img"]],
                           capture_output=True, text=True)
        print(pid, r.stdout)
        if not r.stdout.startswith("200") or "image" not in r.stdout:
            continue
        # sips: конвертация в JPEG (webp поддерживается в macOS 11+), ширина ≤ 640 px, белый фон для PNG с альфой
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82", "-Z", "640",
                        str(raw), "--out", str(out)], capture_output=True)
        if not out.exists():
            print("  convert failed", pid)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()


def build(photos):
    rows = load_rows()
    by_no = {r["№ ЭП"]: r for r in rows}
    # карточки
    cards = OrderedDict()
    for r in rows:
        no = r["№ ЭП"]
        key = GROUP_KEY.get(no, no)
        maker, model = r["Производитель"], r["Модель"]
        has_brand = maker not in NO_BRAND and not str(maker).startswith(("требует", "НЕИЗВ", "не выбран"))
        if not has_brand:
            continue
        c = cards.setdefault(key, dict(ids=[], objs=[], name=r["Наименование"], maker=maker, model=model,
                                       p=fmt(r["Pн ед., кВт"], 3), qty=0, photo=PHOTO_OF.get(no),
                                       doc=(r.get("Ссылка на паспорт / каталог") or "").split(" ; ")[0]))
        c["ids"].append(str(no))
        ob = str(r["№ объекта"])
        if ob not in c["objs"]:
            c["objs"].append(ob)
        c["qty"] += r["Кол-во всего"] or 0
    ordered = []
    for key, c in cards.items():
        ordered.append(dict(c, obj=", ".join(c["objs"]), qty=fmt(c["qty"])))
        for e in EXTRA:
            if e["after"] == key:
                ordered.append(e)

    def card_html(c):
        ph = photos.get(c["photo"] or "", {})
        img_file = IMG_DIR / f"{c['photo']}.jpg"
        if c["photo"] and img_file.exists():
            src = f"img/eq/{c['photo']}.jpg"
            pic = f'<img src="{src}" alt="{esc(c["maker"])} {esc(c["model"])}" loading="lazy">'
            if ph.get("note"):
                pic += f'<p class="eq-pnote">{esc(ph["note"])}</p>'
            cred = f'<a href="{esc(ph.get("page") or ph.get("img"))}" target="_blank" rel="noopener">фото: {esc(domain(ph.get("page") or ph.get("img")))}</a>'
        else:
            pic = '<div class="eq-nophoto">фото не найдено</div>'
            cred = ""
        doc = f'<a href="{esc(c["doc"])}" target="_blank" rel="noopener">паспорт</a>' if c.get("doc") else ""
        links = " · ".join(x for x in (doc, cred) if x)
        obj = c["obj"]
        obj_lab = f"объект № {obj}" if obj[0].isdigit() and obj != "1–20" else ("все объекты" if obj == "1–20" else ("виноградник" if obj == "Поле" else "территория"))
        return (f'<article class="eq-card">{pic}<div class="eq-body">'
                f'<p class="eq-tag">ЭП № {esc(", ".join(c["ids"]))} · {esc(obj_lab)}</p>'
                f'<h3>{esc(c["maker"])} <span>{esc(c["model"])}</span></h3>'
                f'<p class="eq-name">{esc(c["name"])}</p>'
                f'<p class="eq-meta">Pн {esc(c["p"])} кВт × {esc(c["qty"])} шт.</p>'
                f'<p class="eq-links">{links}</p></div></article>')

    plant = [c for c in ordered if c["obj"] != "Поле"]
    field = [c for c in ordered if c["obj"] == "Поле"]
    n_brand = sum(1 for r in rows if r["Производитель"] not in NO_BRAND
                  and not str(r["Производитель"]).startswith(("требует", "НЕИЗВ", "не выбран")))
    n_photo = sum(1 for c in ordered if c["photo"] and (IMG_DIR / f"{c['photo']}.jpg").exists())

    # полная таблица
    trs = []
    cur_obj = None
    for r in rows:
        ob = str(r["№ объекта"])
        if ob != cur_obj:
            cur_obj = ob
            trs.append(f'<tr class="grp"><td colspan="7">{esc(ob)} — {esc(r["Объект генплана"])}</td></tr>')
        maker, model = r["Производитель"], r["Модель"]
        nob = maker in NO_BRAND or str(maker).startswith(("требует", "НЕИЗВ", "не выбран"))
        mk = f'<span class="badge unk">нет марки</span> <small>{esc(maker or "")}</small>' if nob else esc(maker)
        trs.append(f'<tr><td>{r["№ ЭП"]}</td><td>{esc(r["Наименование"])}</td><td>{mk}</td>'
                   f'<td>{esc(model if model not in (None, "—") else "—")}</td><td>{fmt(r["Pн ед., кВт"], 3)}</td>'
                   f'<td>{fmt(r["Кол-во всего"])} / {fmt(r["рабочих"])}</td><td>{fmt(r["Pн ед., кВт"] * r["рабочих"] if isinstance(r["Pн ед., кВт"], (int, float)) else None, 2)}</td></tr>')

    out = f"""<!-- EQ:START -->
<section id="equipment">
  <h2>Оборудование: марки, модели, фото</h2>
  <p>Марка и модель указаны у {n_brand} ЭП из {len(rows)}. Карточки ниже — по одной на модель, в порядке объектов генплана; данные — лист «Ведомость» файла 03. Фото взяты со страниц производителей или их дилеров (ссылка под каждым фото) и показывают модель или её серию, а не оборудование конкретного завода. Фото найдено для {n_photo} карточек.</p>
  <h3>Завод (объекты № 1–20)</h3>
  <div class="eq-grid">
    {''.join(card_html(c) for c in plant)}
  </div>
  <h3>Виноградник: орошение и автоматика (вне площадки)</h3>
  <div class="eq-grid">
    {''.join(card_html(c) for c in field)}
  </div>
  <details class="eq-all">
    <summary>Все {len(rows)} электроприёмников с марками и моделями</summary>
    <div class="table"><table>
      <thead><tr><th>№ ЭП</th><th>Наименование</th><th>Производитель</th><th>Модель</th><th>Pн ед., кВт</th><th>Кол-во всего / раб.</th><th>Pуст = Pн × раб., кВт</th></tr></thead>
      <tbody>{''.join(trs)}</tbody>
    </table></div>
  </details>
  <p class="muted">Без марки: шнек выжимки (по компоновке пресса), термоголовка капсулятора, конвейеры, приборы учёта алкоголя, очистные, серверная и SCADA, лабораторный набор, видеонаблюдение, LoRaWAN-узлы и автоматика насосной орошения. Их мощности — оценки, статус в ведомости указан.</p>
</section>
<!-- EQ:END -->"""
    idx = SITE / "index.html"
    s = idx.read_text(encoding="utf-8")
    if "<!-- EQ:START -->" in s:
        a = s.index("<!-- EQ:START -->")
        b = s.index("<!-- EQ:END -->") + len("<!-- EQ:END -->")
        s = s[:a] + out + s[b:]
    else:
        anchor = '<section id="shifts">'
        s = s.replace(anchor, out + "\n\n" + anchor, 1)
    idx.write_text(s, encoding="utf-8")
    print(f"cards {len(ordered)}, with photo {n_photo}, brands {n_brand}/{len(rows)}")


if __name__ == "__main__":
    photos = json.load(open(PHOTOS, encoding="utf-8")) if PHOTOS.exists() else {}
    if "fetch" in sys.argv:
        fetch(photos)
    build(photos)
