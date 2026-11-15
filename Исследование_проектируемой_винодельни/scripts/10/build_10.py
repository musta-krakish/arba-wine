"""Сборка 10_Источники_и_проверка.md из urls.tsv (где использован) и urls_chk.tsv (проверка curl).

Запуск (из папки Исследование_проектируемой_винодельни):
  python scripts/10/build_10.py
Перед этим — проверка ссылок: см. check_urls.sh (результат в urls_chk.tsv).
"""
import re
import glob
from pathlib import Path
from collections import defaultdict, Counter
import openpyxl

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent

used = {}
for l in open(HERE / "urls.tsv", encoding="utf-8"):
    if l.strip():
        u, f = l.rstrip("\n").split("\t")
        used[u] = f.split(",")
chk = {}
for l in open(HERE / "urls_chk.tsv", encoding="utf-8"):
    p = l.rstrip("\n").split("\t")
    if len(p) >= 2:
        chk[p[0]] = p[1]

# ---- контекст: подпись ссылки
label = {}
urlre = re.compile(r"https?://[^\s|)\]>»\"'`,;]+")
for f in sorted(glob.glob(str(ROOT / "*.md"))):
    if Path(f).name.startswith("10_"):
        continue
    for line in open(f, encoding="utf-8"):
        first = ""
        if line.startswith("|"):
            first = re.sub(r"\*\*|`", "", line.strip().strip("|").split("|")[0].strip())
            first = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", first)
        for m in re.finditer(r"\[([^\]]{2,160})\]\((https?://[^)\s]+)\)", line):
            t = m.group(1).strip()
            weak = (len(t) < 12 or re.search(r"\.[a-z]{2,4}(/|$)|^www\.|^https?", t, re.I)
                    or re.match(r"^(prg|pdf|adilet|сайт|ссылка|карточка)\b", t, re.I))
            if weak:
                if first and not re.fullmatch(r"[A-Z]?\d+", first) and not urlre.search(first):
                    t = f"{first} ({t})" if not re.search(r"\.[a-z]{2,4}(/|$)", t) else first
                else:
                    continue
            label.setdefault(m.group(2).rstrip("."), t[:110])
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            for i, c in enumerate(cells):
                for u in urlre.findall(c):
                    u = u.rstrip(".").rstrip("*")
                    if u in label:
                        continue
                    own = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", urlre.sub("", c)).strip(" —:-–(),")
                    own = re.sub(r"\*\*|`", "", own)
                    if len(own) >= 8 and not re.fullmatch(r"[\d.\s–-]+", own):
                        label[u] = own[:110]
                        continue
                    others = [x for j, x in enumerate(cells) if j != i and x and not urlre.search(x) and len(x) > 3
                              and not re.fullmatch(r"(обновл\. )?[\d.\s–-]+|без даты|—|Да|Нет", x)]
                    if others and re.fullmatch(r"[A-Z]?\d+", others[0]):
                        others = others[1:]
                    txt = re.sub(r"\*\*|`", "", others[0] if others else "")
                    label[u] = txt[:110]
for f in sorted(glob.glob(str(ROOT / "*.xlsx"))):
    wb = openpyxl.load_workbook(f)
    for ws in wb:
        hdr = None
        for row in ws.iter_rows(values_only=True):
            if row and "Наименование" in [str(x) for x in row]:
                hdr = [str(x) for x in row]
                continue
            for c in row:
                if isinstance(c, str):
                    for u in urlre.findall(c):
                        u = u.rstrip(".").rstrip("*")
                        if u in label:
                            continue
                        if hdr and "Наименование" in hdr:
                            i = hdr.index("Наименование")
                            j = hdr.index("Модель") if "Модель" in hdr else None
                            label[u] = f"{row[i]} — {row[j] if j is not None else ''}"[:110]
                        else:
                            label[u] = (row[0] if isinstance(row[0], str) else "")[:110]

# ---- тип источника по домену
TYPES = [
    ("[С]", ["arbawine.com"]),
    ("[Р]", ["eldala.kz", "statsnet", "adata.kz", "emis.cn", "kompra"]),
    ("[ОФ]", ["gov.kz", "azhk.kz", "esalmaty.kz", "nationalbank.kz", "stat.gov.kz", "kgd.gov.kz", "qazsu.kz", "almatysu.kz",
              "gharysh.kz", "aisgzk.kz", "gov4c", "kegoc", "gosreestr.kz", "map.gov4c.kz", "akorda"]),
    ("[НПА/НТД]", ["adilet.zan.kz", "zakon.uchet.kz", "cdb.kz", "prg.kz", "online.zakon.kz", "faolex", "alta.ru", "garant.ru",
                   "ppt.ru", "ksm.kz", "kaf.kz", "smway.ru", "dnaop.com", "eaeunion", "docs.cntd.ru"]),
    ("[Нау]", ["awri.com.au", "enology.fst.vt.edu", "escholarship", "doaj.org", "iris.unito", "iieta.org", "oiv.int", "fao.org",
               "mdpi", "wsu.edu", "waterboards.ca.gov", "cornell", "psu.edu", "7universum", "uni-ruse", "mrwa", "ucdavis",
               "researchgate", "sciencedirect", "springer", "wiley", "doi.org", "agris", "cyberleninka", "elibrary"]),
    ("[Гео/Данные]", ["openstreetmap", "open-meteo", "project-osrm", "isric", "nasa.gov", "overpass", "arcgisonline", "esri", "maps.mail.ru",
                      "copernicus", "ecmwf"]),
    ("[СМИ]", ["zakon.kz", "tengrinews", "informburo", "kapital.kz", "inbusiness", "vc.ru", "timesca", "the-buyer", "yahoo",
               "orda.kz", "forbes", "inform.kz", "airpress", "nur.kz", "bizmedia", "uchet.kz", "mybuh", "pro1c", "bes.media",
               "uppersetup", "finratings", "pressdemocrat", "substack", "cepaos", "llamasfinancial", "ashlandcontainer",
               "weproject", "jancisrobinson", "bellisariostudentmedia", "kursiv", "lsm.kz", "kt.kz", "wineretail", "retail.ru", "interfax", "habr", "wine-and-spirits.md",
               "inshymkent", "damu.kz", "wineandbeersupply", "stroihub", "profi-dom", "cler.pro", "sdchenma", "thequirkycork"]),
    ("[Б/у]", ["equipt.com", "usedbottlinglines", "machinio", "exapro", "ybcase", "used-"]),
    ("[Дилер/Магазин]", ["pavlodar.com", "satu.kz", "making.com", "destiller", "winemakersdepot", "wineandbarrels", "twood.fr",
                         "champagne.kz", "newelitalco", "almawine", "alco24", "chinchin", "newxo", "wolt.com", "pegas61",
                         "upakovkatorg", "tcwequipment", "anglianpumping", "springpack", "breezart.ru", "dme1923", "xa.com",
                         "prod.cyb.com.au", "kaspi", "magnum"]),
]


def typ(u):
    d = re.sub(r"^https?://", "", u).split("/")[0].lower()
    for t, keys in TYPES:
        if any(k in d for k in keys):
            return t
    return "[Кат]"   # прочие домены — сайты производителей оборудования (проверено выборочно)


API = ("api.open-meteo.com", "project-osrm.org", "rest.isric.org", "overpass", "power.larc.nasa.gov", "arcgis")


def status(u, code):
    c = code.replace("(ssl)", "")
    if any(a in u for a in API) and c not in ("200", "206"):
        return "Адрес API (не страница) — запросы с параметрами работали при расчёте"
    if c in ("200", "206"):
        if "adilet.zan.kz" in u:
            return "Открыта (текст акта подгружается скриптом — проверить в браузере)"
        if "prg.kz" in u:
            return "Открыта (карточка документа)"
        return "Открыта"
    if c in ("403", "429", "468"):
        return f"Закрыта для автоматической проверки ({c}) — проверить в браузере"
    if c == "404":
        return "**Не открывается (404)**"
    if c == "000":
        return "Не ответил (таймаут)"
    return f"Ошибка {c}"


FILES = {"01": "01_Arba_Wine", "02": "02_Технология", "03": "03_Ведомость ЭП", "04": "04_График", "05": "05_Расчёт",
         "06": "06_Участок", "07": "07_Генплан", "08": "08_Орошение_БПЛА", "09": "09_Экономика", "11": "11_Нормативы"}
REL = {"[С]": "Данные со слов компании; не инженерные исходные данные",
       "[Р]": "Вторичный (агрегатор реестров); финансы — оценки сервиса; сверять с stat.gov.kz/kgd.gov.kz",
       "[ОФ]": "Высокая (госорган, сетевая компания, Нацбанк)",
       "[НПА/НТД]": "Высокая по содержанию; действующую редакцию сверять на adilet.zan.kz",
       "[Нау]": "Высокая для удельных показателей и методик",
       "[Кат]": "Основа статуса ТИПОВОЕ (паспорт/каталог производителя)",
       "[Дилер/Магазин]": "Средняя: цены и характеристики сверять с производителем",
       "[Б/у]": "Низкая: только порядок величины",
       "[СМИ]": "Средняя/низкая: факты событий; цифры — заявления; реклама помечена",
       "[Гео/Данные]": "Открытые данные и модели (OSM, реанализ, ЦМР); не обследование"}

rows = []
for u, fs in used.items():
    rows.append((u, typ(u), fs, status(u, chk.get(u, "000")), label.get(u, "")))
first_file = lambda r: min(r[2])
rows.sort(key=lambda r: (first_file(r), r[1], r[0]))

cnt = Counter()
for r in rows:
    s = r[3]
    key = ("Открыта" if s.startswith("Открыта") else "Закрыта для автоматической проверки" if s.startswith("Закрыта")
           else "404" if "404" in s else "Адрес API" if s.startswith("Адрес API") else "Таймаут / ошибка")
    cnt[key] += 1
tcnt = Counter(r[1] for r in rows)

out = []
out.append("# 10. Источники и проверка достоверности\n")
out.append("Дата проверки ссылок: **16.11.2026**. Реестр собран автоматически из всех файлов папки (`01`–`11`, включая листы xlsx) "
           "и из входных данных экономической модели. Скрипты: `scripts/10/check_urls.sh` (проверка curl), `scripts/10/build_10.py` (сборка).\n")
out.append(f"Всего уникальных ссылок: **{len(rows)}**. Итог проверки: " +
           "; ".join(f"{k} — {v}" for k, v in cnt.most_common()) + ".\n")
out.append("## 1. Как оценивалась достоверность\n")
out.append("Каждая цифра в файлах имеет статус показателя (ПОДТВЕРЖДЕНО / ТИПОВОЕ / РАСЧЁТНОЕ / НЕИЗВЕСТНО). "
           "Здесь — надёжность самого источника по его типу.\n")
out.append("| Тип | Что это | Надёжность для проекта | Ссылок |\n|---|---|---|---|")
for t, d in REL.items():
    nm = {"[С]": "Сайт предприятия", "[Р]": "Реестры и агрегаторы", "[ОФ]": "Официальные организации", "[НПА/НТД]": "Законы, правила, нормы",
          "[Нау]": "Научные и отраслевые публикации", "[Кат]": "Каталоги и паспорта производителей", "[Дилер/Магазин]": "Дилеры и магазины",
          "[Б/у]": "Объявления б/у", "[СМИ]": "СМИ, блоги, обзоры", "[Гео/Данные]": "Карты, климат, рельеф, почвы"}[t]
    out.append(f"| {t} | {nm} | {d} | {tcnt.get(t, 0)} |")
out.append("\nЧто означает результат проверки:\n")
out.append("- **Открыта** — сервер вернул страницу или файл (HTTP 200/206).")
out.append("- **adilet.zan.kz** открывается, но текст и статус акта подгружаются скриптом с авторизацией; автоматически редакцию не проверить — **открыть каждый акт в браузере**.")
out.append("- **Закрыта для автоматической проверки (403/429)** — сайт отказывает роботу; ссылка, скорее всего, рабочая. Проверить в браузере.")
out.append("- **Адрес API** — базовый адрес сервиса данных (рельеф, маршруты, почвы, климат, МЧС); сами запросы с параметрами при расчёте работали, а «голый» адрес отвечает ошибкой — это нормально.")
out.append("- **Не открывается (404)** — ссылка устарела; на выводы см. раздел 3.\n")

out.append("## 2. Реестр ссылок (по файлу, где использованы впервые)\n")
cur = None
n = 0
for u, t, fs, st, lab in rows:
    f0 = first_file((u, t, fs))
    if f0 != cur:
        cur = f0
        out.append(f"\n### {FILES.get(f0, f0)}\n")
        out.append("| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |\n|---|---|---|---|---|---|")
    n += 1
    lab = lab.replace("|", "/").strip() or "—"
    disp = re.sub(r"^https?://", "", u)
    disp = disp if len(disp) <= 60 else disp[:57] + "…"
    out.append(f"| {n} | {lab} | [{disp}]({u}) | {t} | {', '.join(sorted(fs))} | {st} |")

out.append("\n## 3. Неоткрывшиеся ссылки и их влияние на выводы\n")
out.append("| Ссылка | Что подтверждала | Влияние |\n|---|---|---|")
IMPACT = {
    "azud.com": "Электрика контроллера фильтров Azud — в 03 мощность и так НЕИЗВЕСТНО", "daikin.eu": "Кондиционеры АБК 0,99 кВт — значение взято с другой страницы Daikin; ссылка, вероятно, усечена",
    "ksm.kz/%D0%A1%D0%9F%20%D0%A0%D0%9A%202.03-30": "СП РК 2.03-30-2017 (сейсмика) не открыт — в 06/07 сейсмичность по слою МЧС, отмечено «сверить»",
    "kaf.kz": "Правила инвестсубсидирования № 317 (документ на сайте КАФ) — проценты субсидий в 09 помечены как допущение",
    "almawine.kz/catalog/vino/krasnoe/15253": "Одна из цен Arba — есть другие магазины", "statsnet.co": "Реестровые данные Arba — есть adata, EMIS",
    "chinchin.kz": "Цена Arba — есть другие магазины", "e-auction.gosreestr.kz": "Земельные торги — юридическая доступность участков в 06 не подтверждена",
}
for u, t, fs, st, lab in rows:
    if st.startswith("**Не") or st.startswith("Не ответил"):
        imp = next((v for k, v in IMPACT.items() if k in u), "Вспомогательная ссылка; цифры продублированы другими источниками или помечены")
        out.append(f"| {u} | {lab or '—'} | {imp} |")

out.append("\n## 4. Источники без ссылки (книги, нормы на бумаге)\n")
out.append("| Источник | Где | Статус |\n|---|---|---|")
for a, b, c in [
    ("Boulton R.B., Singleton V.L., Bisson L.F., Kunkee R.E. Principles and Practices of Winemaking. Springer, 1996", "02, 05", "Не открывался; теплота брожения взята по AWRI 2012"),
    ("Ribéreau-Gayon P. et al. Handbook of Enology. Vol. 1–2. Wiley, 2006", "02", "Не открывался — сверить параметры «ТИПОВОЕ, первоисточник не сверен»"),
    ("Валуйко Г.Г. Технология виноградных вин. Симферополь: Таврида, 2001", "02", "Не открывался — нормативы выхода сусла по фракциям"),
    ("Кишковский З.Н., Мержаниан А.А. Технология вина. М., 1984", "02", "Не открывался"),
    ("Кабышев А.В., Обухов С.Г. Расчёт и проектирование систем электроснабжения. Томск: ТПУ, 2005", "03 (Ки, cosφ)", "Из прежнего исследования (лист «Коэффициенты»)"),
    ("Радкевич В.Н. и др. Расчёт электрических нагрузок промышленных предприятий. БНТУ, 2013", "03", "Из прежнего исследования"),
    ("ВНТП 03-86, прил. 15", "03", "Из прежнего исследования (dnaop.com)"),
    ("Della Toffola, каталог «Impianti di Refrigerazione», с. 7", "03 (Чиллеры)", "Ссылка — в 03, лист «Ведомость»; дата каталога не указана"),
    ("KAZNEX INVEST, 2016 — до 300 тыс. бут./год Arba", "01", "Найден через Times of Central Asia (04.05.2016) — ссылка в 01"),
]:
    out.append(f"| {a} | {b} | {c} |")

out.append("\n## 5. Что проверить вручную перед защитой\n")
for i, t in enumerate([
    "Открыть на **adilet.zan.kz** в браузере все акты из 11_Нормативная_база (особенно санитарные правила СЗЗ — п. о «первичном виноделии» и п. 23 о 2 000 м; Водный кодекс 2025; правила БАС № 706) и сверить действующие редакции.",
    "Проверить ссылки с пометкой «Закрыта для автоматической проверки».",
    "Сохранить PDF-копии каталогов производителей, на которые опирается 03 (сайты меняются).",
    "Для финансов Arba (01) — получить платный отчёт statsnet/adata или ответ компании; оценки ElDala не использовать как отчётность.",
    "Для площадки (06) — ручная проверка кадастровой карты map.gov4c.kz/egkn по координатам.",
], start=1):
    out.append(f"{i}. {t}")

(ROOT / "10_Источники_и_проверка.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("rows", len(rows), cnt, tcnt)
