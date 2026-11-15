"""Сборка 08_Источники.md.

Вход:
  urls_chk.tsv — результат проверки ссылок (url, http-код, конечный url), см. check_urls.sh;
  ctx.txt      — контекст ссылок из 03_Электроприемники.xlsx (файл, url, текст ячейки || строка).
Ручные описания источников из 01, 02, 04, 05 — в списках ниже.
Запуск: python3 build_registry.py <папка с urls_chk.tsv и ctx.txt> > ../../08_Источники.md
"""
import sys, os, re
from urllib.parse import urlparse

D = sys.argv[1]
chk = {}
for l in open(os.path.join(D, "urls_chk.tsv"), encoding="utf-8"):
    u, code, *_ = l.rstrip("\n").split("\t")
    chk[u] = code

CHECK_DATE = "01.11.2026"

def status(u, override=None):
    if override:
        return override
    c = chk.get(u)
    if c is None:
        return "не проверялась"
    if c in ("200", "206"):
        return "Открыта"
    if "zakon.uchet.kz" in u and c == "000":
        return "Таймаут (сайт не отвечал при итоговой проверке)"
    if c == "000":
        return "Не открывается (таймаут)"
    if c in ("403", "468"):
        return f"Закрыта для робота ({c}); проверить в браузере"
    if c.startswith("404"):
        return "**Не открывается (404)**"
    return c

def link(u, text=None):
    t = text or urlparse(u).netloc.replace("www.", "")
    return f"[{t}]({u})"

counter = [0]
final = {}
def table(rows):
    out = ["| № | Источник | Тип | Дата | Что подтверждает | Где использован | Проверка |",
           "|---|---|---|---|---|---|---|"]
    for r in rows:
        u, title, typ, date, what, where = r[:6]
        ov = r[6] if len(r) > 6 else None
        counter[0] += 1
        src = f"{title} — {link(u)}" if u else title
        st = status(u, ov) if u else "—"
        if u:
            final[u] = st
        out.append(f"| {counter[0]} | {src} | {typ} | {date} | {what} | {where} | {st} |")
    return "\n".join(out)

used = set()
def mark(rows):
    for r in rows:
        if r[0]:
            used.add(r[0])
    return rows

# ---------------------------------------------------------------- 1. Сайты предприятий
S1 = mark([
 ("https://arbawine.com/ru/контакты", "Arba Wine — Контакты", "[С]", "—", "Телефоны, e-mail, адреса винотек", "01"),
 ("https://arbawine.com/ru/технология-винификации", "Arba Wine — Технология винификации", "[С]", "—", "Прессы Bucher Vaslin, танки Gortani, чиллеры", "01, 03 А"),
 ("https://arbawine.com/ru/технология-розлива", "Arba Wine — Технология розлива", "[С]", "—", "Линия розлива: Alfatek, OMAR, R&G, C&G; насос, фильтр", "01, 03 А"),
 ("https://arbawine.com/ru/винный-погреб", "Arba Wine — Винный погреб", "[С]", "—", "Бочковый и бутылочный (61,4 м²) погреба, климат-контроль", "01, 02, 03 А"),
 ("https://arbawine.com/ru/география", "Arba Wine — География", "[С]", "—", "Каракемер, высота ≈1000 м", "01"),
 ("https://arbawine.com/ru/сбор-урожая", "Arba Wine — Сбор урожая", "[С]", "—", "Сезон 20.08 — середина октября, круглосуточная работа", "01, 03 А"),
 ("https://gold-product.com/kontakty-2/", "Голд Продукт — Контакты", "[С]", "© 2021", "Контакты ПК «Тургень» и офиса", "01"),
 ("https://gold-product.com/proizvodstvo-8/", "Голд Продукт — Производство", "[С]", "© 2021", "7 000 т/год, розлив 4 000 бут./ч, хранение", "01, 02, 03 А"),
 ("https://gold-product.com/o-kompanii-1/", "Голд Продукт — О компании", "[С]", "© 2021", "Структура, виноградники", "01"),
 ("https://gold-product.com/rukovodstvo-7/", "Голд Продукт — Руководство", "[С]", "© 2021", "Генеральный директор", "01"),
 ("https://turgenwines.com/", "Turgen Wines (текст извлечён из JS-файла сайта)", "[С]", "31.10.2026", "Линия до 18 000 т/сезон, розлив 6 000 бут./ч, площади подвалов и складов", "01, 02"),
 ("https://issykwine.kz/kontakty/", "Винзавод «ISSYK» — Контакты", "[С]", "—", "Телефоны, e-mail, офис", "01"),
 ("https://issykwine.kz/o-kompanii/", "Винзавод «ISSYK» — О компании", "[С]", "© 2023", "История, «европейское оборудование»", "01"),
 ("https://issykwine.kz/assortiment/", "Винзавод «ISSYK» — Ассортимент", "[С]", "—", "Виноградных вин в ассортименте нет", "01"),
 ("https://silkalleykz.com/en/contacts/", "Silk Alley — Contacts", "[С]", "—", "Адрес, телефоны, e-mail", "01"),
 ("https://silkalleykz.com/contacts/", "Silk Alley — Контакты", "[С]", "изм. 10.08.2026", "Ошибочный маркер на карте; описание территории", "02"),
 ("https://winnac.kz/contact/", "Winnac Elite — Контакты", "[С]", "—", "Адрес, телефоны", "01"),
])

# ---------------------------------------------------------------- 2. Реестры
S2 = mark([
 ("https://pk.adata.kz/company/990540004450", "adata.kz — ТОО «ARBA WINE»", "[Р]", "—", "БИН, юр. адрес, руководитель, ОКЭД", "01"),
 ("https://www.emis.cn/php/company-profile/KZ/Arba_Wine_TOO__Arba_Wine_ТОО__en_8588346.html", "EMIS — Arba Wine TOO", "[Р]", "—", "Профиль компании", "01"),
 ("https://ba.prg.kz/194081100-turgen/980740001015-ao-gold-produkt/", "prg.kz — АО «Голд Продукт»", "[Р]", "данные 2026", "БИН, ОКЭД, юр. адрес, налоги", "01"),
 ("https://kompra.kz/organization/930440000824", "kompra.kz — АО «Винзавод «Иссык»»", "[Р]", "30.10.2026", "Реквизиты, ликвидация филиала", "01"),
 ("https://ba.prg.kz/194041100-bolek/930440000824-ao-vinzavod-issyk/", "prg.kz — АО «Винзавод «Иссык»»", "[Р]", "2026", "БИН, адрес, ОКЭД", "01"),
 ("https://pk.adata.kz/counterparty/main/company/191140012879/basic-info", "adata.kz — ТОО «Винный завод «Silk Alley»", "[Р]", "—", "БИН, адрес, ОКЭД, численность", "01"),
 ("https://pk.adata.kz/counterparty/main/company/941140000417/basic-info", "adata.kz — АО «Бахус»", "[Р]", "—", "БИН, адрес, ОКЭД", "01"),
 ("https://pk.uchet.kz/search/bin/970740001915", "uchet.kz — ТОО «Винзавод «Дионис»", "[Р]", "—", "БИН, адрес, ОКЭД", "01"),
 ("https://eldala.kz/dannye/kompanii/5183-arba-wine", "ElDala — Arba Wine", "[Р]", "2026", "Состав производства", "02"),
])

# ---------------------------------------------------------------- 3. СМИ
S3 = mark([
 ("https://www.zakon.kz/sobytiia/6377519-Arba-Wine-kak-vozrozhdenie-vinogradnikov-prinosit-polzu-selu.html", "zakon.kz — «Arba Wine: как возрождение виноградников приносит пользу селу»", "[СМИ]", "29.11.2022", "Виноградники 170 + 49 га", "01, 06"),
 ("https://vc.ru/id1342027/536203-vinodelnya-arba-wine", "vc.ru — «Винодельня Arba Wine»", "[СМИ]", "10.11.2022", "Выпуск 80–100 тыс. бут.; планировка гостевой зоны", "01, 02"),
 ("https://informburo.kz/stati/est-istina-v-vine-karakemera.html", "informburo.kz — «Есть истина в вине Каракемера»", "[СМИ]", "22.09.2016", "Сортировка, прессы, история", "01, 03 А"),
 ("https://www.weproject.media/articles/detail/prazdnik-urozhaya-glavnoe-sobytie-goda-dlya-vinodelni-arba-wine/", "weproject.media — праздник урожая Arba Wine", "[СМИ]", "07.08.2026", "Завод действует в 2026 г.", "01"),
 ("https://daz.asia/ru/otsenka-potrebitelya-vsegda-otlichno/", "daz.asia — «Оценка потребителя — всегда «отлично»»", "[СМИ]", "26.01.2012", "Голд Продукт: 10 000 т винограда, итальянское оборудование", "01, 03 А"),
 ("https://winenomad.kz/turgen-wines.html", "winenomad.kz — Turgen Wines", "[Блог]", "06.11.2025", "Винодельня действует", "01"),
 ("https://siberia2022.retaildays.ru/images/2022/presentations/2810_1400_wine_kondrashov.pdf", "Презентация Gold Product, Retail Days 2022", "[С]", "2022", "Мощности Тургень/Шелек (только сниппет поиска)", "01",
  "Не открывается (таймаут); не открывалась и при сборе 31.10 — данные только из сниппета"),
 ("https://www.euromonitor.com/cider-perry-in-kazakhstan/report", "Euromonitor — Cider/Perry in Kazakhstan", "[СМИ]", "08.2026", "«Иссык» — лидер рынка сидра (53 %)", "01"),
 ("https://en.tengrinews.kz/news/22736/", "Tengrinews — High quality wines to be produced in south Kazakhstan", "[СМИ]", "22.09.2013", "Silk Alley: 3 000 т, ёмкости", "01"),
 ("https://forbes.kz/articles/shelkovaya_alleya_1559896226", "Forbes.kz — «Шёлковая аллея»", "[СМИ]", "20.06.2019", "Silk Alley: мощность, 172 ёмкости, оборудование", "01, 03 А"),
 ("https://yujanka.kz/yuzhnyj-kazahstan-vinodelie-vozrozhdaetsya/", "yujanka.kz — «Южный Казахстан: виноделие возрождается»", "[СМИ]", "09.01.2019", "Silk Alley: персонал, выпуск", "01"),
 ("https://www.zakon.kz/redaktsiia-zakonkz/4944850-zhanseit-tuymebaev-oznakomilsya-s.html", "zakon.kz — Туймебаев ознакомился с Caspian Food", "[СМИ]", "06.11.2018", "Silk Alley: выпуск 2018", "01"),
 ("https://podrobno.uz/cat/politic/mirziyeev-i-nazarbaev-posetili-vinodelcheskoe-proizvodstvo-v-kazakhstane-/", "Podrobno.uz — визит на винодельческое производство", "[СМИ]", "30.04.2017", "Silk Alley: Сарыагашский район", "02"),
 ("https://mirror.akorda.kz/en/events/astana_kazakhstan/visits_to_objects/visit-to-caspian-food-llp", "Akorda — Visit to Caspian Food LLP", "[ОФ]", "29.04.2017", "Silk Alley = Caspian Food", "02"),
 ("https://informburo.kz/stati/v-zale-9-tysyach-butylok-remyuer-ezhednevno-perevorachivaet-vse-.html", "informburo.kz — цех игристого «Бахус»", "[Рек]", "01.11.2018", "Бахус: бочки, ёмкости, шампанизация", "01, 03 А"),
 ("https://forbes.kz/articles/uroki_armenii", "Forbes.kz — «Уроки Армении»", "[СМИ]", "27.03.2017", "Winnac Elite: профиль", "01"),
 ("https://forbes.kz/news/newsid_228351", "Forbes.kz — возрождение виноделия в Жамбылской обл.", "[СМИ]", "28.06.2020", "Винзавод Южный", "01"),
 ("https://orda.kz/ot-lozy-do-butylki-pochemu-kazahstanskomu-vinu-trudno-konkurirovat-s-importom-416592/", "Orda.kz — «От лозы до бутылки» (данные МСХ и Минфина РК)", "[СМИ]", "08.07.2026", "Площадь виноградников и урожай РК 2025 (для оценки урожайности)", "01, 06"),
 ("https://marketing.rbc.ru/research/45276/", "РБК Маркетинг — Анализ рынка вина в Казахстане 2025 (TEBIZ)", "[СМИ]", "10.03.2025", "Отраслевой контекст", "01"),
 ("https://tengrinews.kz/home-news/hotim-normalnoy-jizni-jiteli-almatinskoy-oblasti-jaluyutsya-605065/", "Tengrinews — «Хотим нормальной жизни»: перебои напряжения в Алматинской обл.", "[СМИ]", "09.08.2026", "Провалы напряжения в Тургене, Каракемире; ВЛ-110 № 106И/107И", "04"),
])

# ---------------------------------------------------------------- 4. Карты, геоданные, объявления
S4 = mark([
 ("https://2gis.kz/almaty/firm/70000001114727190", "2ГИС — Arba Wine, Завод", "[Гео]", "31.10.2026", "Адрес Орымбетова 63а, координаты 43.4273, 77.6217", "01, 02",
  "Открывалась 31.10.2026; при итоговой проверке робот получил заглушку 2ГИС"),
 ("https://www.wine-searcher.com/merchant/67026-arba-wine", "Wine-searcher — Arba Wine", "[Гео]", "—", "Координаты завода (сниппет)", "02",
  "Закрыта для робота (403) и 31.10; координаты из сниппета"),
 ("https://krisha.kz/a/show/662895755", "krisha.kz — завод первичного виноделия, Шелек (объявление о продаже)", "[Объявл]", "26.10.2020 / 29.10.2026", "Шелекский завод: 6,78 га, 9 752 м², 5,5 млн л; продаётся", "01, 02",
  "Открывалась 31.10.2026; при итоговой проверке закрыта для робота (468)"),
 ("https://krisha-photos.kcdn.online/webp/5f/5fc52e60-04e1-4b63-b2fd-1cfb04779518/15-full.jpg", "krisha.kz — фото завода с дрона", "[Объявл]", "—", "Вид территории сверху", "02"),
 ("http://www.energoprojekt.rs/winery-and-leasure-area-juko-villa-saryagash-kazakhstan/?lang=en", "Energoprojekt Holding — Winery and leisure area JUKO Villa, Saryagash", "[ОФ подрядчика]", "статус 2012, фото 10.2018", "Silk Alley: 12 000 м², 3,5 млн л/год, фото корпуса", "02"),
 ("http://www.energoprojekt.rs/wp-content/uploads//2018/10/corporate-overview_2018.pdf", "Energoprojekt Corporate Overview 2018 (PDF)", "[ОФ подрядчика]", "2018", "Проект JUKO Villa в портфеле", "02"),
 ("https://energovg.rs/en/projects/winery-and-leisure-area-juko-villa/", "Energoprojekt Visokogradnja — Winery and Leisure Area JUKO Villa", "[ОФ подрядчика]", "—", "Цифры «9 130 м², дистиллерия 700 м²» — только сниппет, не подтверждены", "02",
  "**Не открывается (404)**; 31.10 — ошибка сертификата"),
 ("https://www.gov.kz/uploads/2025/12/8/44ec5193582e3d020be8dd86b8793396_original.3942557.pdf", "Корректировка генплана г. Алматы, т. 2 (НИИ «Алматыгенплан»)", "[ОФ]", "2025", "Упоминание АО «Голд Продукт» (генплана завода нет)", "02"),
 ("https://www.openstreetmap.org/", "OpenStreetMap — Overpass API (зеркало maps.mail.ru), OSM API v0.6, Nominatim", "[Гео]", "данные на 31.10.2026", "Контуры корпусов, подстанции, ЛЭП (© участники OSM, ODbL)", "02, 04"),
 ("https://ecoportal.kz/Rubric/PublicService", "ecoportal.kz — реестр государственных услуг (заявления, ОВОС)", "[ОФ]", "31.10.2026", "Поиск по БИН и сёлам — совпадений нет", "02"),
 (None, "Esri World Imagery (тайловый сервис ArcGIS Online; © Esri, Maxar, Earthstar Geographics)", "[Гео]", "дата съёмки неизвестна", "Спутниковые снимки в 02/img", "02"),
])

# ---------------------------------------------------------------- 5. Сети, тарифы
S5 = mark([
 ("https://www.azhk.kz/ru/company/region/esikskii", "АО «АЖК» — Есикский РЭС", "[ОФ]", "—", "Адрес, телефоны, число абонентов", "04, 07"),
 ("https://www.azhk.kz/ru/company/region/shelekskii", "АО «АЖК» — Шелекский РЭС", "[ОФ]", "—", "Адрес, телефоны", "04"),
 ("https://www.azhk.kz/images/261005-x-1.xlsx", "АЖК — Информация о резерве и свободных мощностях ПС, 3 кв. 2026 (xlsx)", "[ОФ]", "замеры 17.12.2025, на 01.10.2026", "Загрузка и свободная мощность ПС 34И, 53И, 68И и др.", "04, 06"),
 ("https://www.azhk.kz/images/252131633-6.xlsx", "АЖК — то же, 4 кв. 2025 (xlsx)", "[ОФ]", "замеры 18.12.2024", "Динамика загрузки ПС", "04"),
 ("https://www.azhk.kz/images/aaa/tech-nine/9.pdf", "АЖК — перечень ПС с типами трансформаторов (pdf)", "[ОФ]", "2017", "Число и мощность трансформаторов ПС", "04"),
 ("https://www.azhk.kz/images/260901-x-1.xlsx", "АЖК — исполнение инвестпрограммы 2026 (xlsx)", "[ОФ]", "2 кв. 2026", "ПСД реконструкции ПС-68И «Шелек», 130 млн тг, освоено 0", "04"),
 ("https://www.azhk.kz/media-center//ru/199-novosti/2026/5287-rassmotreny-zhaloby-na-snizhenie-elektricheskogo-napryazheniya-v-enbekshikazakhskom-rajone", "АЖК — «Рассмотрены жалобы на снижение напряжения в Енбекшиказахском районе»", "[ОФ]", "27.08.2026", "Причина провалов, меры (БСК 110 кВ)", "04"),
 ("https://www.azhk.kz/ru/tarify", "АЖК — Тарифы", "[ОФ]", "с 01.04.2026", "Передача 15,42 тг/кВт·ч без НДС", "04"),
 ("https://www.esalmaty.kz/images/docs/2025/2609112312-x-1.pdf", "Филиал АЖК «Энергосбыт» — тарифы с 12.09.2026 (pdf)", "[ОФ]", "12.09.2026", "Группа 2: 50,03 / 43,13 тг/кВт·ч", "04"),
 ("https://esalmaty.kz/ru/i4160", "esalmaty.kz — тарифы с 05.06.2026", "[ОФ]", "05.06.2026", "Предыдущий тариф 46,25 / 39,87", "04"),
 ("https://energopotok.kz/wp-content/uploads/2026/09/свободная-мощность-2026-1.pdf", "ТОО «Оңтүстік Жарық Транзит» — свободная мощность ПС 2026 (скан)", "[ОФ]", "04.02.2026", "ПС «Карла Маркса» 35/10 кВ и др. (Сарыагашский р-н)", "04, 06"),
 ("https://energopotok.kz/?p=4326", "ОЖТ — объявление о тарифе на передачу", "[ОФ]", "с 01.11.2026", "12,28 тг/кВт·ч без НДС", "04"),
 ("https://energopotok.kz/?p=4012", "ОЖТ — тарифы Шымкента и Туркестанской обл.", "[ОФ]", "01.08.2025", "Группа 2: 44,75 тг/кВт·ч", "04"),
 ("https://www.gov.kz/memleket/entities/ontustik/press/news/details/674915?lang=ru", "gov.kz — ввод ПС 220/110/10 кВ «Кызыласкер»", "[ОФ]", "21.12.2023", "Питание Сарыагашского района", "04"),
])

# ---------------------------------------------------------------- 6. НПА
def npa(id_, title, what, where):
    u = f"https://zakon.uchet.kz/rus/docs/{id_}"
    used.add(u)
    used.add(f"https://adilet.zan.kz/rus/docs/{id_}")
    t = f"{title}; официально — [adilet.zan.kz](https://adilet.zan.kz/rus/docs/{id_})"
    return (u, t, "[НПА]", "см. `05`", what, where)

S6 = [
 npa("V1500010851", "ПУЭ РК — приказ МЭ РК № 230 от 20.03.2015", "Устройство электроустановок", "03, 04, 05"),
 npa("V1500010949", "ПТЭЭП РК — приказ МЭ РК № 246 от 30.03.2015", "Перегрузка трансформаторов, эксплуатация", "04, 05"),
 npa("V1500010889", "ПТБ потребителей РК — приказ МЭ РК № 222 от 19.03.2015", "Электробезопасность", "05"),
 npa("V1500010403", "Правила пользования электрической энергией — приказ МЭ РК № 143 от 25.02.2015", "ТУ (п. 17), учёт (п. 38)", "04, 05, 07"),
 npa("V1500011108", "Нормативные значения коэффициента мощности — приказ МИР РК № 393 от 31.03.2015", "cosφ ≥ 0,93 на 0,4 кВ", "04, 05"),
 npa("V1400010899", "Электросетевые правила — приказ МЭ РК № 210 от 18.12.2014", "Справочно", "05"),
 npa("V1500010957", "Правила функционирования АСКУЭ — приказ МЭ РК № 248 от 30.03.2015", "Справочно", "05"),
 npa("V2100024045", "ТР «Общие требования к пожарной безопасности» — приказ МЧС РК № 405 от 17.08.2021", "Пожарная безопасность", "05"),
 npa("V2100025366", "Санитарные требования к объектам производства алкогольной продукции — приказ МЗ РК № ҚР ДСМ-123 от 23.11.2021", "Санитарные требования (пункты не сверены)", "05"),
 npa("V2100022673", "Санитарные требования к объектам производства пищевой продукции — приказ МЗ РК № ҚР ДСМ-36 от 28.04.2021", "Светильники с защитой от боя стекла", "05"),
 npa("Z040000588_", "Закон РК «Об электроэнергетике» от 09.07.2004 № 588", "Базовый закон", "05"),
 npa("Z1200000541", "Закон РК «Об энергосбережении и повышении энергоэффективности» от 13.01.2012 № 541", "Энергоэффективность", "05"),
 npa("K2600000253", "Строительный кодекс РК 2026", "Система строительных норм", "05"),
]
S6 += mark([
 ("https://prg.kz/m/amp/document/32102729", "prg.kz — карточка ПУЭ РК (статус и изменения)", "[НПА]", "—", "Изменения № 340 (2022), № 22-н/қ (2025)", "05"),
 ("https://www.zakon.kz/pravo/6536834", "zakon.kz — «Правила пользования электроэнергией изменили в Казахстане»", "[СМИ]", "30.10.2026", "Приказ № 383-н/қ, вступает с 08.11.2026", "05"),
 ("https://zakon.uchet.kz", "zakon.uchet.kz — рабочие копии НПА (главная)", "[НПА]", "—", "Полные тексты актов", "05"),
])

# ---------------------------------------------------------------- 7. Нормы и стандарты
def prg(doc, title, where="05"):
    u = f"https://prg.kz/document/?doc_id={doc}"
    used.add(u)
    return (u, title, "[НТД]", "см. `05`", "Статус и редакция", where)

S7 = [
 ("https://new-shop.ksm.kz/media/egfntd/ntdgo/4_04_08_2023.pdf", "СН РК 4.04-08-2023 «Проектирование электроснабжения промышленных предприятий» (PDF ЕГФНТД)", "[НТД]", "06.11.2023", "Выбор трансформаторов, категории", "04, 05"),
 prg(38667733, "СН РК 4.04-08-2023 — карточка prg.kz"),
 ("https://new-shop.ksm.kz/media/egfntd/ntdgo/SP_RK_4.04-108-2014.pdf", "СП РК 4.04-108-2014 «Проектирование электроснабжения промышленных предприятий» (PDF ЕГФНТД)", "[НТД]", "01.07.2015", "Методика нагрузок, Kз, Tм", "04, 05"),
 prg(35776703, "СП РК 4.04-108-2014 — карточка prg.kz"),
 ("https://new-shop.ksm.kz/media/egfntd/ntdgo/SP_RK_4.04-105-2014.pdf", "СП РК 4.04-105-2014 «Проектирование сельских электрических сетей» (PDF ЕГФНТД)", "[НТД]", "01.07.2015", "Сельские сети 10 кВ, категории", "04, 05"),
 prg(38338891, "СП РК 4.04-105-2014 — карточка prg.kz"),
 prg(37401178, "СП РК 4.04-109-2013 «Правила проектирования силового и осветительного оборудования промышленных предприятий»"),
 prg(30002371, "РДС РК 4.04-185-2003 «Нормы технологического проектирования сельских электрических сетей РК»"),
 prg(38520762, "СН РК 4.04-07-2023 «Электротехнические устройства»"),
 prg(39059542, "СП РК 4.04-107-2013 «Электротехнические устройства»"),
 prg(34120625, "СП РК 4.04-106-2013 «Электрооборудование жилых и общественных зданий»"),
 prg(38304152, "СП РК 2.04-104-2012 «Естественное и искусственное освещение»", "03 (сверить), 05"),
 prg(38588660, "СН РК 2.04-01-2011 «Естественное и искусственное освещение»"),
 prg(31753585, "СП РК 2.04-103-2013 «Устройство молниезащиты зданий и сооружений»"),
 prg(36515945, "СП РК 4.02-101-2012 «Отопление, вентиляция и кондиционирование воздуха»", "04, 05"),
 prg(35664024, "СН РК 4.02-01-2011 «Отопление, вентиляция и кондиционирование воздуха»"),
 prg(39287975, "СН РК 4.01-01-2011 «Внутренний водопровод и канализация зданий и сооружений»", "04, 05"),
 prg(37065985, "СН РК 2.02-02-2023 «Пожарная автоматика зданий и сооружений»"),
 prg(38466567, "СП РК 2.02-102-2022 «Пожарная автоматика зданий и сооружений»"),
 prg(34065963, "СН РК 2.02-01-2023 «Пожарная безопасность зданий и сооружений»"),
 prg(33195180, "СП РК 2.02-101-2022 «Пожарная безопасность зданий и сооружений»"),
 prg(31713776, "СН РК 3.02-31-2023 «Здания и сооружения для хранения и переработки сельскохозяйственной продукции»"),
 prg(34566000, "СП РК 3.02-131-2012 «Здания и сооружения для хранения и переработки сельскохозяйственной продукции»"),
 prg(30039496, "ГОСТ 14209-97 — карточка «утратил силу»"),
 ("https://online.zakon.kz/Document/?doc_id=30000028", "РД 34.21.122-87 (молниезащита) — карточка «утратил силу»", "[НТД]", "—", "Не применять", "05"),
 ("https://online.zakon.kz/Document/?doc_id=30005452", "СО 153-34.21.122-2003 (молниезащита) — «не действует в РК»", "[НТД]", "—", "Не применять", "05"),
 ("https://new-shop.ksm.kz/egfntd/ntdgo/kds/", "ЕГФНТД — перечень строительных норм КДСиЖКХ", "[НТД]", "—", "Поиск СН/СП РК", "05"),
 ("https://new-shop.ksm.kz/catalog/search/", "Каталог КазСтандарта — 25 ГОСТ и СТ РК из `05`, разд. 5 (номера карточек указаны там)", "[НТД]", "—", "Статус ГОСТ/СТ РК в Казахстане", "05"),
 ("https://prg.kz", "prg.kz (Параграф) — карточки документов", "[НТД]", "—", "Статусы и даты изменений", "05"),
]
mark(S7)

# ---------------------------------------------------------------- 8. Методики и аналоги
S8 = mark([
 ("https://meganorm.ru/Data1/9/9624/index.htm", "РТМ 36.18.32.4-92 «Указания по расчёту электрических нагрузок»", "[Мет]", "1992", "Методика расчёта нагрузок, табл. 1–2 Кр", "03, 04, 05"),
 ("https://meganorm.ru/Data1/9/9947/index.htm", "ВНТП 25-85 «Нормы технологического проектирования винодельческих заводов»", "[Мет]", "1985", "Режимы работы, удельный расход энергии; статус в РК неизвестен", "04, 05"),
 ("https://files.stroyinf.ru/Data2/1/4294840/4294840547.htm", "ГОСТ 10032-80 (текст)", "[НТД]", "1980", "Автоматизация ДГУ", "04"),
 ("https://meganorm.ru/Data/601/60117.pdf", "ГОСТ 33115-2014 (текст)", "[НТД]", "2014", "Допустимый наброс нагрузки на ДГУ", "04"),
 ("https://smway.ru/wp-content/uploads/2022/05/SP-60.13330.2020.pdf", "СП 60.13330.2020 (РФ, аналог)", "[НТД РФ]", "2020", "Категория аварийной вентиляции — заменено ссылкой на СП РК 4.02-101-2012", "03, 04"),
 ("https://meganorm.ru/Data2/1/4293853/4293853695.htm", "ОСН-АПК 2.10.24.001-04 (РФ) — нормы освещения с/х предприятий", "[НТД РФ]", "2004", "Нормы освещённости (сверить с СП РК 2.04-104-2012)", "03 «Освещение»"),
 (None, "СП 52.13330.2016 (РФ) «Естественное и искусственное освещение» — ссылка в файлах не приводится", "[НТД РФ]", "2016", "Нормы освещённости и удельной мощности (сверить с СП РК)", "03 «Освещение», «Расчёт_В»"),
 ("https://dnaop.com/html/29670_14.html", "ВНТП 03-86, прил. 15", "[Мет]", "1986", "Ки, cosφ холодильных компрессоров", "03 «Коэффициенты»"),
 ("https://edu.ggpek.by/mod/resource/view.php?id=3610", "Методичка «Практическая работа № 1», табл. 1.3 (ГГПЭК)", "[Мет]", "—", "Ки, cosφ вентиляторов", "03 «Коэффициенты»"),
 ("https://jasulib.org.kg/wp-content/uploads/2023/03/Кабышев-А.В.-Расч.-проект.-электросн..pdf", "Кабышев А.В., Обухов С.Г. Расчёт и проектирование систем электроснабжения. Томск: ТПУ, 2005", "[Мет]", "2005", "Ки, cosφ насосов, компрессоров", "03 «Коэффициенты»"),
 ("https://kubsau.ru/upload/iblock/9c8/9c84fdd278d8a5fe88fff572e33f466a.pdf", "Сазыкин В.Г., Кудряков А.Г. Расчёт электрических нагрузок в системах электроснабжения АПК. КубГАУ, 2017", "[Мет]", "2017", "Коэффициенты для производственных цехов АПК", "03 «Коэффициенты»"),
 ("https://vinograd.info/knigi/spravochnik-po-vinodeliyu/vinodelcheskoe-oborudovanie.html", "Тихонов В.П., Виноградов В.А. «Справочник по виноделию», гл. 9", "[Мет]", "—", "Типовое винодельческое оборудование", "03 Б"),
])

# ---------------------------------------------------------------- 9. Отраслевые исследования
S9 = mark([
 ("https://www.mdpi.com/1996-1073/10/2/222", "Gómez-Lorente D. et al. Energies 10(2):222", "[Нау]", "2017", "Удельное потребление малых заводов 16,3 кВт·ч/гл, сезонность", "04, 06"),
 ("https://dspace.uevora.pt/rdpc/bitstream/10174/21284/1/Vela_et_al_ctv20173201p62.pdf", "Vela R. et al. Ciência Téc. Vitiv. 32(1):62–71", "[Нау]", "2017", "Структура потребления: холод 46,9 %", "04"),
 ("https://rdpc.uevora.pt/handle/10174/29852", "Perdigones A. et al. Ciência Téc. Vitiv. 36(1):45–54", "[Нау]", "2021", "Pуст эталонного завода, суточный график", "04"),
 ("https://www.wineaustralia.com/getmedia/5996a3e5-3cbd-40d8-bbb9-8d632f443652/AWR-2201-LCA-Final-Report.pdf", "Hirlam K. LCA of the Australian wine industry (AWRI / Wine Australia, AWR 2201)", "[Нау]", "2023", "30,6 кВт·ч/гл для малых заводов", "04"),
 ("https://www.awri.com.au/wp-content/uploads/WineryA-CaseStudyReport.pdf", "AWRI. Improving winery refrigeration efficiency — Winery A", "[Нау]", "—", "≈188 МВт·ч/год на ≈500 т; потребление вне сезона", "04"),
 ("https://doi.org/10.1016/j.esd.2014.08.002", "Smyth M., Nesbitt A. Energy and English wine production: A review of energy use and benchmarking. Energy Sust. Dev. 23:85–91", "[Нау]", "2014", "0,557 кВт·ч/л (открыта только аннотация)", "04"),
 ("https://iieta.org/download/file/fid/109159", "Malavasi M. et al. Int. J. Heat & Technology 41(4)", "[Нау]", "2023", "Тепловыделение брожения ≈1 Вт/л", "03 «Расчёт_В»"),
 ("https://conf.uni-ruse.bg/bg/docs/cp10/9.2/9.2-12.pdf", "Митев П. Научни трудове Русенски ун-т, т. 49, с. 65–68", "[Нау]", "2010", "Теплофизика сусла, CO₂, холод", "03 «Расчёт_В», Б"),
 ("https://doaj.org/article/9ac0884d5c2541bcb5437ee81e61e72c", "J. Agric. Eng. 2023 — термостатирование ёмкостей", "[Нау]", "2023", "7,0–10,3 Вт·ч/дм³ (только сниппет)", "03 «Коэффициенты»"),
])

# ---------------------------------------------------------------- 10. Электрооборудование (04, 03 ABB)
S10 = mark([
 ("https://s.electrical.ru/files/products/c8/c89894df1ea1bf8ddf2c701e63667ab7_601ba97cafdd5.pdf", "Каталог трансформаторов ТМГ11", "[Кат]", "—", "ТМГ11-160/10/0,4: потери, Uк", "04"),
 ("https://kes.kz/katalog/transformatornye-podstantsii/komplektnye-transformatornye-podstantsii-naruzhnoy-ustanovki-ktpn", "KazElectroSnab — КТПН", "[Кат]", "—", "КТП 25–4000 кВА казахстанского производства", "04"),
 ("https://ukkz.nt-rt.ru/images/showcase/catalog3.pdf", "Усть-Каменогорский конденсаторный завод — каталог УКМ", "[Кат]", "—", "УКМ63-0,4-50-12,5", "04"),
 ("https://yorpower.com/wp-content/uploads/2025/07/C55D5E.pdf", "Cummins C55 D5e — datasheet", "[Кат]", "2025", "ДГУ 40 кВт PRP / 44 кВт ESP", "04"),
 ("https://ekt.kz/upload/iblock/b1f/Katalog_kabel_provod.pdf", "«ЭлкомКабель» — каталог кабелей", "[Кат]", "—", "Марки и параметры кабелей", "04"),
 ("https://cdn.shopify.com/s/files/1/0762/8819/6927/files/abb_low__voltage_process.pdf", "ABB «Low voltage Process performance motors 400 V 50 Hz», 9AKK105944 EN 12-2022 (копия)", "[Кат]", "12.2022", "КПД, cosφ двигателей IE3", "03 «Двигатели_ABB»"),
])

# ---------------------------------------------------------------- 11. Технологическое оборудование (03) — автоматически
TYPE_RULES = [
 (("machineseeker", "exapro", "netbid", "equipt.com", "sigmaequipment"), "[Б/у]"),
 (("fermer.ru",), "[Форум]"),
 (("elib.sfu-kras",), "[ВКР]"),
 (("journals.ac.za",), "[Нау]"),
 (("bts.net.ua", "hagbes", "kranzle", "enologys", "e-battery", "ecovita", "anglianpumping", "boyser.sk", "scribd", "environmental-expert", "making.com"), "[Дилер]"),
 (("silkalleykz",), "[С]"),
]
def typ_of(u):
    for keys, t in TYPE_RULES:
        if any(k in u for k in keys):
            return t
    return "[Кат]"

rows11 = []
for l in open(os.path.join(D, "ctx.txt"), encoding="utf-8"):
    f, u, txt = l.rstrip("\n").split("\t", 2)
    if not f.startswith("03") or u in used:
        continue
    cell, _, rowtxt = txt.partition(" || ")
    # название: текст ячейки до ссылки
    pos = cell.find(u)
    before = cell[:pos] if pos > 0 else ""
    before = re.split(r"https?://\S+", before)[-1]          # текст после предыдущей ссылки
    title = before.strip(" ;—–()[]").strip()
    title = re.sub(r"^\S+\s*\]\s*;?\s*", "", title) if title.startswith(("сниппет", "не открыт")) else title
    if title.count("(") > title.count(")"):
        title += ")"
    if not title or len(title) < 4:
        title = urlparse(u).netloc.replace("www.", "")
    note = re.search(r"\[(сниппет[^\]]*|не открыт[^\]]*)\]", cell)
    def short(x, n=45):
        x = x.strip()
        return x if len(x) <= n else x[:n].rsplit(" ", 1)[0] + "…"
    parts = [short(p) for p in rowtxt.split("|")]
    sheet = f.split(":")[1]
    if sheet.startswith("Б") or sheet.startswith("А"):
        no = parts[0]
        sel = parts[3:6] if sheet.startswith("Б") else parts[1:2] + parts[3:5]
        what = ", ".join(x for x in sel if x and x != "None")
        where = f"03 {sheet[0]}, № {no}"
    else:
        what, where = parts[0], f"03 «{sheet}»"
    ov = None
    if note and chk.get(u) in ("200", "206"):
        ov = "Открыта сейчас; в 03 цифра взята из сниппета поиска (при сборе страница не открывалась)"
    rows11.append((u, title, typ_of(u), "—", what, where, ov))
    used.add(u)

# ---------------------------------------------------------------- вывод
all_urls = set(chk)
missing = sorted(all_urls - used)
if missing:
    sys.stderr.write("НЕ ВКЛЮЧЕНЫ:\n" + "\n".join(missing) + "\n")

sections = [
 ("1. Официальные сайты предприятий", S1),
 ("2. Государственные реестры и агрегаторы", S2),
 ("3. СМИ, блоги, рекламные материалы", S3),
 ("4. Карты, геоданные, материалы подрядчиков, объявления", S4),
 ("5. Сетевые компании, энергетика, тарифы", S5),
 ("6. Нормативные правовые акты РК", S6),
 ("7. Строительные нормы и стандарты", S7),
 ("8. Методики, справочники, аналоги РФ", S8),
 ("9. Отраслевые и научные исследования", S9),
 ("10. Каталоги электрооборудования", S10),
 ("11. Каталоги и данные технологического оборудования (`03`, листы «А», «Б», «Коэффициенты»)", rows11),
]
body = []
for h, rows in sections:
    body.append(f"## {h}\n\n{table(rows)}\n")
total = counter[0]

stat = {}
for u, s_ in final.items():
    k = ("Открыта" if s_.startswith("Открыта") else
         "Таймаут zakon.uchet.kz" if "zakon.uchet" in u and chk.get(u) == "000" else
         "Закрыта для робота или отдаёт заглушку" if ("закрыта" in s_.lower() or "заглушку" in s_) else
         "404" if "404" in s_ else "Таймаут" if "таймаут" in s_.lower() else s_)
    stat[k] = stat.get(k, 0) + 1
nourl = total - len(final)

print(open(os.path.join(os.path.dirname(__file__), "head.md"), encoding="utf-8").read()
      .replace("{TOTAL}", str(total)).replace("{URLS}", str(len(final))).replace("{NOURL}", str(nourl))
      .replace("{STAT}", "; ".join(f"{k} — {v}" for k, v in sorted(stat.items(), key=lambda x: -x[1]))))
print("\n".join(body))
print(open(os.path.join(os.path.dirname(__file__), "tail.md"), encoding="utf-8").read())
