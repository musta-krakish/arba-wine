# 10. Источники и проверка достоверности

Дата проверки ссылок: **16.11.2026** (новые ссылки файлов 03, 12, 13 — 22.11.2026). Реестр собран автоматически из всех файлов папки (`01`–`13`, включая листы xlsx) и из входных данных экономической модели. Скрипты: `scripts/10/check_urls.sh` (проверка curl), `scripts/10/build_10.py` (сборка).

Всего уникальных ссылок: **406**. Итог проверки: Открыта — 373; Закрыта для автоматической проверки — 14; Адрес API — 8; 404 — 6; Таймаут / ошибка — 5.

## 1. Как оценивалась достоверность

Каждая цифра в файлах имеет статус показателя (ПОДТВЕРЖДЕНО / ТИПОВОЕ / РАСЧЁТНОЕ / НЕИЗВЕСТНО). Здесь — надёжность самого источника по его типу.

| Тип | Что это | Надёжность для проекта | Ссылок |
|---|---|---|---|
| [С] | Сайт предприятия | Данные со слов компании; не инженерные исходные данные | 5 |
| [Р] | Реестры и агрегаторы | Вторичный (агрегатор реестров); финансы — оценки сервиса; сверять с stat.gov.kz/kgd.gov.kz | 4 |
| [ОФ] | Официальные организации | Высокая (госорган, сетевая компания, Нацбанк) | 19 |
| [НПА/НТД] | Законы, правила, нормы | Высокая по содержанию; действующую редакцию сверять на adilet.zan.kz | 106 |
| [Нау] | Научные и отраслевые публикации | Высокая для удельных показателей и методик | 25 |
| [Кат] | Каталоги и паспорта производителей | Основа статуса ТИПОВОЕ (паспорт/каталог производителя) | 130 |
| [Дилер/Магазин] | Дилеры и магазины | Средняя: цены и характеристики сверять с производителем | 49 |
| [Б/у] | Объявления б/у | Низкая: только порядок величины | 3 |
| [СМИ] | СМИ, блоги, обзоры | Средняя/низкая: факты событий; цифры — заявления; реклама помечена | 54 |
| [Гео/Данные] | Карты, климат, рельеф, почвы | Открытые данные и модели (OSM, реанализ, ЦМР); не обследование | 11 |

Что означает результат проверки:

- **Открыта** — сервер вернул страницу или файл (HTTP 200/206).
- **adilet.zan.kz** открывается, но текст и статус акта подгружаются скриптом с авторизацией; автоматически редакцию не проверить — **открыть каждый акт в браузере**.
- **Закрыта для автоматической проверки (403/429)** — сайт отказывает роботу; ссылка, скорее всего, рабочая. Проверить в браузере.
- **Адрес API** — базовый адрес сервиса данных (рельеф, маршруты, почвы, климат, МЧС); сами запросы с параметрами при расчёте работали, а «голый» адрес отвечает ошибкой — это нормально.
- **Не открывается (404)** — ссылка устарела; на выводы см. раздел 3.

## 2. Реестр ссылок (по файлу, где использованы впервые)


### 01_Arba_Wine

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 1 | ElDala.kz — Arba Wine | [eldala.kz/dannye/kompanii/5183-arba-wine](https://eldala.kz/dannye/kompanii/5183-arba-wine) | [Р] | 01 | Открыта |
| 2 | adata.kz | [pk.adata.kz/company/990540004450](https://pk.adata.kz/company/990540004450) | [Р] | 01 | Открыта |
| 3 | statsnet.co — ТОО «ARBA WINE» | [statsnet.co/en/companies/kz/3975074](https://statsnet.co/en/companies/kz/3975074) | [Р] | 01 | Не ответил (таймаут) |
| 4 | EMIS — Arba Wine TOO | [www.emis.cn/php/company-profile/KZ/Arba_Wine_TOO__Arba_Wi…](https://www.emis.cn/php/company-profile/KZ/Arba_Wine_TOO__Arba_Wine_ТОО__en_8588346.html) | [Р] | 01 | Открыта |
| 5 | arbawine.com — «Сбор урожая» | [arbawine.com/ru/сбор-урожая](https://arbawine.com/ru/сбор-урожая) | [С] | 01, 02, 13 | Открыта |
| 6 | arbawine.com — «Технология винификации» | [arbawine.com/ru/технология-винификации](https://arbawine.com/ru/технология-винификации) | [С] | 01, 02, 13 | Открыта |
| 7 | SCMP (Su-Lin Tan), перепечатка Yahoo Finance | [finance.yahoo.com/news/china-australia-relations-kazakhst…](https://finance.yahoo.com/news/china-australia-relations-kazakhstan-serbia-093000984.html) | [СМИ] | 01 | Открыта |
| 8 | informburo.kz — «Тайна популярности бренда Arba Wine» [Рек] | [informburo.kz/stati/tayna-populyarnosti-brenda-arba-wine.…](https://informburo.kz/stati/tayna-populyarnosti-brenda-arba-wine.html) | [СМИ] | 01 | Открыта |
| 9 | kapital.kz — «От зарождения до вершин: путь Arba Wine за 10 лет» | [kapital.kz/business/121321/ot-zarozhdeniya-do-vershin-put…](https://kapital.kz/business/121321/ot-zarozhdeniya-do-vershin-put-arba-wine-za-10-let.html) | [СМИ] | 01 | Открыта |
| 10 | tengrinews.kz — «Уникальность виноградников Arba Wine» [Рек] | [tengrinews.kz/news/unikalnost-vinogradnikov-arba-wine-454…](https://tengrinews.kz/news/unikalnost-vinogradnikov-arba-wine-454421/) | [СМИ] | 01 | Открыта |
| 11 | Times of Central Asia — «Kazakhstan to export wine to China, Russia and Europe» | [timesca.com/kazakhstan-to-export-wine-to-china-russia-and…](https://timesca.com/kazakhstan-to-export-wine-to-china-russia-and-europe/) | [СМИ] | 01 | Открыта |
| 12 | vc.ru, блог «БГ» — «Винодельня Arba Wine» | [vc.ru/id1342027/536203-vinodelnya-arba-wine](https://vc.ru/id1342027/536203-vinodelnya-arba-wine) | [СМИ] | 01, 13 | Открыта |
| 13 | inbusiness.kz — «Национальному бренду Arba Wine — 10 лет» | [www.inbusiness.kz/ru/news/nacionalnomu-brendu-arba-wine-1…](https://www.inbusiness.kz/ru/news/nacionalnomu-brendu-arba-wine-10-let) | [СМИ] | 01 | Открыта |
| 14 | The Buyer — «Tasting the wines of Kazakhstan» (J. Keay | [www.the-buyer.net/tasting/wine/tasting-the-wines-of-kazak…](https://www.the-buyer.net/tasting/wine/tasting-the-wines-of-kazakhstan) | [СМИ] | 01 | Открыта |
| 15 | zakon.kz — «Arba Wine: как возрождение виноградников приносит пользу селу» | [www.zakon.kz/sobytiia/6377519-Arba-Wine-kak-vozrozhdenie-…](https://www.zakon.kz/sobytiia/6377519-Arba-Wine-kak-vozrozhdenie-vinogradnikov-prinosit-polzu-selu.html) | [СМИ] | 01, 02 | Открыта |

### 02_Технология

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 16 | Texas A&M AgriLife. Barrel use (presentation) | [aggie-horticulture.tamu.edu/wp-content/uploads/sites/13/2…](https://aggie-horticulture.tamu.edu/wp-content/uploads/sites/13/2018/08/Barrel-use-short-ver-8.3.18.pdf) | [Кат] | 02 | Открыта |
| 17 | Margaret River Wine Association. Sustainability Case Study 2 (цит. Kumar et al. 2009: 2,4 кЛ/т; 0,4–8,0 кЛ/т д | [margaretriver.wine/wp-content/uploads/2023/02/MRWA-Sustai…](https://margaretriver.wine/wp-content/uploads/2023/02/MRWA-Sustainability-Case-Study-2_Final.pdf) | [Кат] | 02 | Открыта |
| 18 | Bucher Vaslin. Bucher XPro 5/8/15 (проспект GB) | [www.bvnorthamerica.com/s/Bucher-XPro-GB.pdf](https://www.bvnorthamerica.com/s/Bucher-XPro-GB.pdf) | [Кат] | 02, 03 | Открыта |
| 19 | Bucher Vaslin. Guide Inertys (GB) | [www.bvnorthamerica.com/s/Guide-Inertys-GB-p9pe.pdf](https://www.bvnorthamerica.com/s/Guide-Inertys-GB-p9pe.pdf) | [Кат] | 02 | Открыта |
| 20 | Cornell CALS. Grapes 101: Grapes in a Bottle of Wine (150 галлонов/т, диапазон 130–180; 756 бут./т) | [cals.cornell.edu/news/2021/05/grapes-101-grapes-bottle-wine](https://cals.cornell.edu/news/2021/05/grapes-101-grapes-bottle-wine) | [Нау] | 02 | Открыта |
| 21 | Zoecklein B. Wine Proteins and Protein Stability. Virginia Tech | [enology.fst.vt.edu/downloads/wm_issues/Wine%20Proteins%20…](https://enology.fst.vt.edu/downloads/wm_issues/Wine%20Proteins%20and%20Protein%20Stability.pdf) | [Нау] | 02 | Открыта |
| 22 | Guchu E., Ebeler S.E., Lee J. et al. Monitoring selected monomeric polyphenol composition in pre- and post-fer | [escholarship.org/content/qt4mg0m2m3/qt4mg0m2m3.pdf](https://escholarship.org/content/qt4mg0m2m3/qt4mg0m2m3.pdf) | [Нау] | 02 | Открыта |
| 23 | AWRI. Malolactic fermentation in red wine (fact sheet) | [www.awri.com.au/files/attachment/mlf-in-red-wine](https://www.awri.com.au/files/attachment/mlf-in-red-wine) | [Нау] | 02 | Открыта |
| 24 | AWRI. Cold stabilisation | [www.awri.com.au/industry_support/winemaking_resources/sto…](https://www.awri.com.au/industry_support/winemaking_resources/storage-and-packaging/pre-packaging-preparation/cold-stabilisation/) | [Нау] | 02 | Открыта |
| 25 | AWRI. Fermentation temperature | [www.awri.com.au/industry_support/winemaking_resources/win…](https://www.awri.com.au/industry_support/winemaking_resources/winemaking-practices/fermentation-temperature/) | [Нау] | 02 | Открыта |
| 26 | AWRI. Extended post-fermentation maceration | [www.awri.com.au/industry_support/winemaking_resources/win…](https://www.awri.com.au/industry_support/winemaking_resources/winemaking-practices/winemaking-treatment-extended-post-fermentation-maceration/) | [Нау] | 02 | Открыта |
| 27 | Godden P. The effects of fermentation temperature on the composition of red wines // AWRI Technical Review № 2 | [www.awri.com.au/wp-content/uploads/2021/06/Technical_Revi…](https://www.awri.com.au/wp-content/uploads/2021/06/Technical_Review_Issue_252_Godden.pdf) | [Нау] | 02 | Открыта |
| 28 | Zoecklein B. Potassium Bitartrate Stabilization of Wines. Virginia Tech (−4 °C 14/21 сут; 4 г/л KHT; структура | [www.enology.fst.vt.edu/downloads/wm_issues/Potassium%20Bi…](https://www.enology.fst.vt.edu/downloads/wm_issues/Potassium%20Bitartrate%20Stabilization%20of%20Wines.pdf) | [Нау] | 02 | Открыта |
| 29 | Zoecklein B. Red Wine Production, Section 3. Virginia Tech | [www.enology.fst.vt.edu/downloads/wm_issues/Red%20Wine%20P…](https://www.enology.fst.vt.edu/downloads/wm_issues/Red%20Wine%20Production/Red%20Wine%20Production%20-%20Section%203.pdf) | [Нау] | 02 | Открыта |
| 30 | Zoecklein B. Winery Wastewater. Virginia Tech (табл. 1–3; Chouinard 2009, Goss 2006, Smith 2002) | [www.enology.fst.vt.edu/downloads/wm_issues/Winery%20Waste…](https://www.enology.fst.vt.edu/downloads/wm_issues/Winery%20Waste%20Water.pdf) | [Нау] | 02 | Открыта |
| 31 | OIV. International Code of Oenological Practices, Issue 2023/01 (листы 1.12; 2.1.2, с. II.2.1-7; 2.1.4; 2.1.5, | [www.oiv.int/sites/default/files/publication/2023-04/CPO%2…](https://www.oiv.int/sites/default/files/publication/2023-04/CPO%20complet%20EN%202023.pdf) | [Нау] | 02 | Открыта |
| 32 | Weber E., Hirschfelt D., Smith R. How Much Wine Can a Small Vineyard Produce? UC Cooperative Extension, Small | [www.waterboards.ca.gov/waterrights/water_issues/programs/…](https://www.waterboards.ca.gov/waterrights/water_issues/programs/hearings/donovan/docs/wr60.pdf) | [Нау] | 02 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 33 | Arba Wine — Винный погреб | [arbawine.com/ru/винный-погреб](https://arbawine.com/ru/винный-погреб) | [С] | 02 | Открыта |
| 34 | Arba Wine — Технология розлива | [arbawine.com/ru/технология-розлива](https://arbawine.com/ru/технология-розлива) | [С] | 02, 03, 13 | Открыта |
| 35 | «Есть истина в вине Каракемера», informburo.kz | [informburo.kz/stati/est-istina-v-vine-karakemera.html](https://informburo.kz/stati/est-istina-v-vine-karakemera.html) | [СМИ] | 02, 13 | Открыта |

### 03_Ведомость ЭП

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 36 | Тангенциальный фильтр (альтернатива) — CFKN50 (2023) | [www.equipt.com/listings/1174311-used-2023-della-toffola-c…](https://www.equipt.com/listings/1174311-used-2023-della-toffola-cfkn50-ultrafiltration-filters-in-oregon) | [Б/у] | 03 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 37 | Этикетировщик линейный самоклеящийся с аппликатором термоусадочной капсулы — Saturno 2T (2015) | [www.usedbottlinglines.com/machines/used-labeling-machine-…](https://www.usedbottlinglines.com/machines/used-labeling-machine-with-capsuler-2000-bph-et227) | [Б/у] | 03 | Открыта |
| 38 | TEROS 11/12 User Manual, METER | [data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_…](https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/20587_TEROS11-12_Manual_Web.pdf) | [Гео/Данные] | 03, 08 | Открыта |
| 39 | Пожарный насос ВПВ (вариант 2×2,5 л/с) — CRI 15-3 (96502002) | [anglianpumping.com/app/uploads/2023/03/96502002_CRI_15-3_…](https://anglianpumping.com/app/uploads/2023/03/96502002_CRI_15-3_A-FGJ-I-V-HQQV.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 40 | Скважинный насос — SP 7-17 | [anglianpumping.com/app/uploads/2023/03/98699158_SP_7-17.pdf](https://anglianpumping.com/app/uploads/2023/03/98699158_SP_7-17.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 41 | Приточная установка с электрокалорифером — 1000 Lux (калорифер 14,4 кВт) | [breezart.ru/catalog/1000-lux/](https://breezart.ru/catalog/1000-lux/) | [Дилер/Магазин] | 03 | Открыта |
| 42 | Приточная установка с водяным калорифером (вариант при газовой котельной) — 2000 Aqua | [breezart.ru/catalog/2000-aqua/](https://breezart.ru/catalog/2000-aqua/) | [Дилер/Магазин] | 03 | Открыта |
| 43 | Пневмопресс мембранный (альтернатива) — Velvet 34 | [dme1923.com/wp-content/uploads/2024/07/04c_Vel003NV_ITA.pdf](https://dme1923.com/wp-content/uploads/2024/07/04c_Vel003NV_ITA.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 44 | Гребнеотделитель-дробилка — Kappa 15 | [dme1923.com/wp-content/uploads/2025/04/02a_Kappa002NV_ITA…](https://dme1923.com/wp-content/uploads/2025/04/02a_Kappa002NV_ITA.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 45 | Установка контактной холодной стабилизации (альтернатива) — Unicrystal C 36 Super | [making.com/wp-content/uploads/2024/09/Cadalpe_2657_brochu…](https://making.com/wp-content/uploads/2024/09/Cadalpe_2657_brochure.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 46 | Аналог моноблока 12/12/1 (ополаск./розлив/укупорка) — Uniblocco 12/12/1 | [making.com/wp-content/uploads/2024/09/Della_Toffola-_3388…](https://making.com/wp-content/uploads/2024/09/Della_Toffola-_3388_brochure.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 47 | Чиллер гликолевый, спиральный, воздушное охлаждение — RAF/151E | [making.com/wp-content/uploads/2024/09/Della_Toffola-_3405…](https://making.com/wp-content/uploads/2024/09/Della_Toffola-_3405_brochure.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 48 | Зарядное устройство АКБ погрузчика 48 В/80 А (ВЧ) — SHARP 50 CG5320 | [prod.cyb.com.au/media/hckdptjd/century-sharp-50-48v-80a-c…](https://prod.cyb.com.au/media/hckdptjd/century-sharp-50-48v-80a-cg5320.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 49 | Зарядное устройство АКБ электроштабелёра 24 В/30 А (ВЧ) — SHARP 20 CG5302 | [prod.cyb.com.au/media/lyylvrq2/century-sharp-20-24v-30a_c…](https://prod.cyb.com.au/media/lyylvrq2/century-sharp-20-24v-30a_cg5302.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 50 | Скважинный насос (прежний кандидат) — SP 17-7 (MS4000) | [www.anglianpumping.com/app/uploads/2023/03/12A01907_SP_17…](https://www.anglianpumping.com/app/uploads/2023/03/12A01907_SP_177.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 51 | Паллетообмотчик стретч-плёнкой (поворотный стол) — Rotoplat 508 | [www.springpack.co.uk/wp/wp-content/uploads/2025/01/Rotopl…](https://www.springpack.co.uk/wp/wp-content/uploads/2025/01/Rotoplat-508-708-User-Manual.pdf) | [Дилер/Магазин] | 03 | Открыта |
| 52 | DJI Agras T50 — Specs | [ag.dji.com/t50/specs](https://ag.dji.com/t50/specs) | [Кат] | 03, 08 | Открыта |
| 53 | DJI Agras T55 — Specs | [ag.dji.com/t55/specs](https://ag.dji.com/t55/specs) | [Кат] | 03, 08 | Открыта |
| 54 | Grundfos CR, CRI, CRN 50 Hz data booklet | [api.grundfos.com/literature/Grundfosliterature-6014742.pdf](https://api.grundfos.com/literature/Grundfosliterature-6014742.pdf) | [Кат] | 03, 08 | Открыта |
| 55 | Шкаф хранения и зарядки Li-ion АКБ БПЛА — ION-PRO-90 CHARGE IO90.195.120.PC.WDC | [asecos.nt-rt.ru/images/manuals/3-shkafy-batarry_ION_eng.pdf](https://asecos.nt-rt.ru/images/manuals/3-shkafy-batarry_ION_eng.pdf) | [Кат] | 03 | Открыта |
| 56 | Электропарогенератор — Bacchus Industrial 14,6 кВт | [assets.3.commercebuild.com/d5f80a936b5655dd7584ccc31173fc…](https://assets.3.commercebuild.com/d5f80a936b5655dd7584ccc31173fc59/contents/ckfinder/images/Downloads-Tab-Brochures/Tecnovap-brochures/Bacchus_Industrial_EN_compressed.pdf) | [Кат] | 03 | Открыта |
| 57 | Azud Helix Automatic 201 | [azud.com/wp-content/uploads/2023/02/AZUD_HELIX_AUTO_201-E…](https://azud.com/wp-content/uploads/2023/02/AZUD_HELIX_AUTO_201-ENG.pdf) | [Кат] | 03, 08 | **Не открывается (404)** |
| 58 | Резервированный источник питания ОПС — РИП-12 исп.50 (РИП-12-3/17М1-Р-RS) | [bolid.ru/production/rip-12_rs.html](https://bolid.ru/production/rip-12_rs.html) | [Кат] | 03 | Открыта |
| 59 | Кулачковый насос (как у Arba) — B215 («CSF A LOBI B215-3200» на сайте Arba) | [boyser.sk/cerpadla/Omac/OMAC_Lobe_%20Pumps_Technical_%20M…](https://boyser.sk/cerpadla/Omac/OMAC_Lobe_%20Pumps_Technical_%20Manual_EN.pdf) | [Кат] | 03 | Открыта |
| 60 | Bermad S-390-T-2W product page | [catalog.bermad.com/BERMAD-Assets/Irrigation/Solenoids/IR-…](https://catalog.bermad.com/BERMAD-Assets/Irrigation/Solenoids/IR-SOLENOID-S-390T-2W/S-390-T-2W-Product-Page-Metric-English.pdf) | [Кат] | 03, 08 | Открыта |
| 61 | Аналог малого моноблока Alfatek — Easy Compact (Robot Compact 7/1), 2018 | [cdn.machineseeker.com/data/listing/doc/52/00/18006286-01.pdf](https://cdn.machineseeker.com/data/listing/doc/52/00/18006286-01.pdf) | [Кат] | 03 | Открыта |
| 62 | Заклейщик коробов скотчем — SK10 | [cdn.shopify.com/s/files/1/0023/1479/7103/files/SIAT-Datas…](https://cdn.shopify.com/s/files/1/0023/1479/7103/files/SIAT-Datasheet-SK10.pdf) | [Кат] | 03 | Открыта |
| 63 | Винтовой компрессор со встроенным рефрижераторным осушителем — SM 10 T | [d15gaovuyz6h3b.cloudfront.net/asset/204664918567/document…](https://d15gaovuyz6h3b.cloudfront.net/asset/204664918567/document_qmgcqvj3cd03hbbb2pauclfj1r) | [Кат] | 03 | Открыта |
| 64 | Регулятор температуры танка — DN33 / ir33 (115…230 В) | [digitalassets.reecegroup.com.au/m/8a4802e36f72b100/origin…](https://digitalassets.reecegroup.com.au/m/8a4802e36f72b100/original/Technical-Guide-CAREL-DN33-Universal-Controllers.pdf) | [Кат] | 03 | Открыта |
| 65 | Соленоидный клапан гликоля на танке — EV220B/EV221B + катушка BB230AS (018F7351) | [doc.7-el.ru/e/ev221b_en.pdf](https://doc.7-el.ru/e/ev221b_en.pdf) | [Кат] | 03 | Открыта |
| 66 | RAK7289V2 Datasheet | [docs.rakwireless.com/Product-Categories/WisGate/RAK7289-V…](https://docs.rakwireless.com/Product-Categories/WisGate/RAK7289-V2/Datasheet/) | [Кат] | 03, 08 | Открыта |
| 67 | Генератор азота PSA со встроенным компрессором — Plus 5 | [enologys.com/public/Store/gb/home/123-nitrogen-generator-…](https://enologys.com/public/Store/gb/home/123-nitrogen-generator-024-to-2-nm-normal-cubic-metre.html) | [Кат] | 03 | Открыта |
| 68 | Аналог мойки-сушки бутылок — BESC-TA550 | [eshop.czechminibreweries.com/product/besc-ta550/](https://eshop.czechminibreweries.com/product/besc-ta550/) | [Кат] | 03 | Открыта |
| 69 | Каплеструйный принтер (датер) — 1580 | [global.videojet.com/wp-content/uploads/dam/pdf/NA%20-%20E…](https://global.videojet.com/wp-content/uploads/dam/pdf/NA%20-%20English/Specification-Sheet/ss-1580-us.pdf) | [Кат] | 03 | Открыта |
| 70 | Этикетировщик самоклеящийся — 6012W | [italianpavilion-propakmena.digital.ice.it/wp-content/uplo…](https://italianpavilion-propakmena.digital.ice.it/wp-content/uploads/2026/05/20210126-CATALOGUE-6012_2017.pdf) | [Кат] | 03 | Открыта |
| 71 | 3. Этикетировщик + капсулятор (термоусадка) — вариант 1 — 6512 | [italianpavilion-propakmena.digital.ice.it/wp-content/uplo…](https://italianpavilion-propakmena.digital.ice.it/wp-content/uploads/2026/05/20241008-063834-24-CAT-6500_2024.pdf) | [Кат] | 03 | Открыта |
| 72 | Моноблок ополаскивание/продувка–розлив–укупорка пробкой под вакуумом (+капсула) — 1306 Y (9 ополаск. / 8 клапа | [italianpavilion-propakmena.digital.ice.it/wp-content/uplo…](https://italianpavilion-propakmena.digital.ice.it/wp-content/uploads/2026/05/20241018-150631-24-CAT-Serie-Y-2024.pdf) | [Кат] | 03 | Открыта |
| 73 | Заклейщик коробов (вариант) — XL35 S (2009) | [machineryline.info/-/sale/carton-sealers/Siat/XL-35-S--24…](https://machineryline.info/-/sale/carton-sealers/Siat/XL-35-S--24010319041759985600) | [Кат] | 03 | Открыта |
| 74 | Сплит-система для винного погреба — SP100 | [media.fondis.com/p/6jmnhsw0l2gl](https://media.fondis.com/p/6jmnhsw0l2gl) | [Кат] | 03 | Открыта |
| 75 | Аналог: очистные МЕГА-М-100 (бытовые стоки) — МЕГА-М-100 | [mega.unilos.ru/](https://mega.unilos.ru/) | [Кат] | 03 | Открыта |
| 76 | Весы платформенные 3 т для ящиков/контейнеров с виноградом (терминал) — IND570 (корпус harsh/panel) + платформ | [mt.com/dam/ind/MTA/Platforms/Brochures/New_K-Line/PFK/PFK](https://mt.com/dam/ind/MTA/Platforms/Brochures/New_K-Line/PFK/PFK) | [Кат] | 03 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 77 | Насосная станция повышения давления (2 насоса с ЧРП) — Hydro Multi-E 2 CRE 5-5 (91048855) | [res.cloudinary.com/sonepar-fr/raw/upload/s--ET6Aka3j--/v1…](https://res.cloudinary.com/sonepar-fr/raw/upload/s--ET6Aka3j--/v1/documents/6879/91048855_Fiche.pdf) | [Кат] | 03 | Открыта |
| 78 | Импеллерный насос (ременной, 2 скорости) — GR MAJOR 60 (2-скор.) | [sealing.com.ua/wa-data/public/site/docs/LIVERANI_%D0%A1at…](https://sealing.com.ua/wa-data/public/site/docs/LIVERANI_%D0%A1atalog_GR.pdf) | [Кат] | 03 | Открыта |
| 79 | Собственные нужды ДГУ: подогреватель охлаждающей жидкости, зарядное АКБ — KD100 (60 Гц, США) — опции | [techcomm.rehlko.com/techcomm/pdf/g5642.pdf](https://techcomm.rehlko.com/techcomm/pdf/g5642.pdf) | [Кат] | 03 | Открыта |
| 80 | Осевой настенный вентилятор вытяжки CO2 (нижняя зона) — OV 4D 450 | [ventilation-system.com/product/ov-4d-450/](https://ventilation-system.com/product/ov-4d-450/) | [Кат] | 03 | Открыта |
| 81 | Накопительный водонагреватель 462 л с фланцевым ТЭН 12 кВт — OKCE 500 S + TPK 210-12 | [voltar.com.ua/uploads/files/document/Drazice_vandens_sild…](https://voltar.com.ua/uploads/files/document/Drazice_vandens_sildytuvu_katalogas_en.pdf) | [Кат] | 03 | Открыта |
| 82 | Винтовой компрессор (альтернатива) — G 7 / G 11 | [www.atlascopco.com/content/dam/atlas-copco/local-countrie…](https://www.atlascopco.com/content/dam/atlas-copco/local-countries/new-zealand/documents/G%202-90_Wuxi%20_leaflet_EN_2935081344.pdf) | [Кат] | 03 | Открыта |
| 83 | Генератор азота PSA — PN 30 N | [www.boge.com/f/287325279136465/x/8cd3fb3caa/boge-us-data-…](https://www.boge.com/f/287325279136465/x/8cd3fb3caa/boge-us-data-sheet-nitrogen-generators.pdf) | [Кат] | 03 | Открыта |
| 84 | Пневмопресс мембранный (основной, белые) — XPlus 40 (IT) | [www.buchervaslin.com/en/produit/bucher-xplus/](https://www.buchervaslin.com/en/produit/bucher-xplus/) | [Кат] | 03 | Открыта |
| 85 | Гребнеотделитель осцилляционный — Delta Oscillys XM | [www.buchervaslin.com/en/produit/delta-oscillys-xm/](https://www.buchervaslin.com/en/produit/delta-oscillys-xm/) | [Кат] | 03 | Открыта |
| 86 | Пневмопресс мембранный (малый, красные/малые партии/резерв) — XPro 15 | [www.buchervaslin.com/wp-content/uploads/2023/11/Catalogue…](https://www.buchervaslin.com/wp-content/uploads/2023/11/Catalogue-Bucher-FR.pdf) | [Кат] | 03 | Открыта |
| 87 | Пневмопресс мембранный (основной, белые) — XPlus 40 (IT) | [www.bvnorthamerica.com/s/Bucher-XPlus-IT-GB.pdf](https://www.bvnorthamerica.com/s/Bucher-XPlus-IT-GB.pdf) | [Кат] | 03 | Открыта |
| 88 | Тепловой насос воздух–вода реверсивный — HAEevo Tech 031 | [www.c-o-k.ru/library/instructions/mta/teplovye-nasosy/114…](https://www.c-o-k.ru/library/instructions/mta/teplovye-nasosy/114606.pdf) | [Кат] | 03 | Открыта |
| 89 | Машина мойки ящиков для винограда — EKW 1500 (2 стадии: мойка + ополаскивание) | [www.christeyns.com/wp-content/uploads/2023/11/C-EQ-LAVADO…](https://www.christeyns.com/wp-content/uploads/2023/11/C-EQ-LAVADORA-CAJAS-CHR-2022_EN.pdf) | [Кат] | 03 | Открыта |
| 90 | Сплит-система АБК/лаборатории — FTXM35R + RXM35R | [www.daikin.eu/content/dam/document-library/catalogues/ac/…](https://www.daikin.eu/content/dam/document-library/catalogues/ac/split/ftxm-r/FTXM-R) | [Кат] | 03 | **Не открывается (404)** |
| 91 | Гребнеотделитель-дробилка — TOP 5 | [www.enoveneta.it/wp-content/uploads/2025/07/TOP-5-10-15-2…](https://www.enoveneta.it/wp-content/uploads/2025/07/TOP-5-10-15-25_LEAFLET_A3_IT-EN_2025web.pdf) | [Кат] | 03 | Открыта |
| 92 | Насос мезги эллиптический роторный с бункером — EVP1 501 | [www.enoveneta.it/wp-content/uploads/2026/06/EVP_LEAFLET_A…](https://www.enoveneta.it/wp-content/uploads/2026/06/EVP_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 93 | Флотатор (опция) — Compact Clear 100 | [www.enoveneta.it/wp-content/uploads/2026/06/FLOTTATORI_LE…](https://www.enoveneta.it/wp-content/uploads/2026/06/FLOTTATORI_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 94 | Пластинчатый фильтр 40×40 — FRC-40-20 | [www.enoveneta.it/wp-content/uploads/2026/06/FRC_LEAFLET_A…](https://www.enoveneta.it/wp-content/uploads/2026/06/FRC_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 95 | Намывной фильтр малый (рекомендуется) — FRM-3 | [www.enoveneta.it/wp-content/uploads/2026/06/FRM_LEAFLET_A…](https://www.enoveneta.it/wp-content/uploads/2026/06/FRM_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 96 | Кулачковый (ротационно-лопастной) насос — LOBEV 25 E | [www.enoveneta.it/wp-content/uploads/2026/06/LOBEV_LEAFLET…](https://www.enoveneta.it/wp-content/uploads/2026/06/LOBEV_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 97 | Насос мезги винтовой (моно) с бункером — Mohno T 608 | [www.enoveneta.it/wp-content/uploads/2026/06/MOHNO_LEAFLET…](https://www.enoveneta.it/wp-content/uploads/2026/06/MOHNO_LEAFLET_A3_IT-EN_2026-web.pdf) | [Кат] | 03 | Открыта |
| 98 | Пневмопресс мембранный (альтернатива) — PPA/PPC 26 | [www.enoveneta.it/wp-content/uploads/2026/06/PP-9-45_LEAFL…](https://www.enoveneta.it/wp-content/uploads/2026/06/PP-9-45_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 99 | Сортировочный вибростол — TVC 3 EVO | [www.enoveneta.it/wp-content/uploads/2026/06/SELEZIONE-UVA…](https://www.enoveneta.it/wp-content/uploads/2026/06/SELEZIONE-UVA_LEAFLET_4-ANTE_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 100 | Импеллерный насос вина/сусла (двухскоростной) — T60 2 VEL | [www.enoveneta.it/wp-content/uploads/2026/06/T-40-60-80-10…](https://www.enoveneta.it/wp-content/uploads/2026/06/T-40-60-80-100_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 101 | Бункер-приёмник вибрационный — Tramoggia vibrante 40 (4,0 т) | [www.enoveneta.it/wp-content/uploads/2026/06/TRAMOGGE-VIBR…](https://www.enoveneta.it/wp-content/uploads/2026/06/TRAMOGGE-VIBRANTI_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 102 | Бункер-приёмник со шнеком — Tramoggia 2000×3000 (3,6 т) | [www.enoveneta.it/wp-content/uploads/2026/06/TRAMOGGE_LEAF…](https://www.enoveneta.it/wp-content/uploads/2026/06/TRAMOGGE_LEAFLET_A3_IT-EN_2026web.pdf) | [Кат] | 03 | Открыта |
| 103 | Электрокотёл отопления АБК — Скат 24 KR 13 | [www.expertcen.ru/product/protherm-skat-24-kr-13.html](https://www.expertcen.ru/product/protherm-skat-24-kr-13.html) | [Кат] | 03 | Открыта |
| 104 | Тест на тартратную стабильность — Crystaltherm | [www.gibertini.com/media/files/crystaltherm-eng-rev-1-62e6…](https://www.gibertini.com/media/files/crystaltherm-eng-rev-1-62e636142d590183362576.pdf) | [Кат] | 03 | Открыта |
| 105 | Автоматический дистиллятор (спирт, летучая кислотность, SO2) — Super DEE | [www.gibertini.com/media/files/superdee-eng-62e797bb2c9121…](https://www.gibertini.com/media/files/superdee-eng-62e797bb2c912172617399.pdf) | [Кат] | 03 | Открыта |
| 106 | Боковая мешалка танка — CPG | [www.inoxpa.com/products/mixing/agitators/agitator-wine-tank](https://www.inoxpa.com/products/mixing/agitators/agitator-wine-tank) | [Кат] | 03 | Открыта |
| 107 | Мобильная CIP-станция — CIP Manual Mobile (300 л) | [www.inoxpa.com/products/systems/cip-systems/cip-manual-mo…](https://www.inoxpa.com/products/systems/cip-systems/cip-manual-mobile-cleaning-system) | [Кат] | 03 | Открыта |
| 108 | Аппарат высокого давления с подогревом (дизельная горелка) — HDS 8/18-4 C | [www.kaercher.com/int/professional/high-pressure-cleaners/…](https://www.kaercher.com/int/professional/high-pressure-cleaners/hot-water-high-pressure-cleaners/compact-class/hds-8-18-4-c-11749000.html) | [Кат] | 03 | Открыта |
| 109 | Аппарат высокого давления с электронагревом (альтернатива) — HDS-E 8/16-4 M 24 kW | [www.kaercher.com/int/professional/high-pressure-cleaners/…](https://www.kaercher.com/int/professional/high-pressure-cleaners/hot-water-high-pressure-cleaners/special-class/hds-e-8-16-4-m-24-kw-10309040.html) | [Кат] | 03 | Открыта |
| 110 | Чиллер технологический (альтернатива другого производителя) — TAEevo Tech 201 | [www.klima-therm.com/se/files/page_files/602/taeevo-tech-f…](https://www.klima-therm.com/se/files/page_files/602/taeevo-tech-fly.pdf) | [Кат] | 03 | Открыта |
| 111 | Чиллер гликолевый, воздушное охлаждение конденсатора, 2 компрессора — TAEevo Tech 201 (исп. P3, осевые вентиля | [www.klima-therm.com/se/files/page_files/602/taeevo-tech-t…](https://www.klima-therm.com/se/files/page_files/602/taeevo-tech-tekniska-data.pdf) | [Кат] | 03 | Открыта |
| 112 | Насос гликолевого контура (вторичный) — CR 15-3 A-A-A-E-HQQE (96501906) | [www.lenntech.com/grundfos/CR015/96501906/CR-15-3-A-A-A-E-…](https://www.lenntech.com/grundfos/CR015/96501906/CR-15-3-A-A-A-E-HQQE.html) | [Кат] | 03 | Открыта |
| 113 | Насос пожаротушения внутреннего противопожарного водопровода — CR 45-2 A-F-A-E-HQQE (96122799) | [www.lenntech.com/grundfos/CRFAM/96122799/CR-45-2-A-F-A-E-…](https://www.lenntech.com/grundfos/CRFAM/96122799/CR-45-2-A-F-A-E-HQQE.html) | [Кат] | 03 | Открыта |
| 114 | Жокей-насос системы пожаротушения — CR 3-10 A-A-A-E-HQQE (96529510) | [www.lenntech.com/grundfos/CRFAM/96529510/CR-3-10-A-A-A-E-…](https://www.lenntech.com/grundfos/CRFAM/96529510/CR-3-10-A-A-A-E-HQQE.html) | [Кат] | 03 | Открыта |
| 115 | Высокотемпературный тепловой насос на CO2 (альтернатива ТЭН) — QAHV-N560YA-HPB | [www.mitsubishi-electric.co.nz/materials/PRODUCT/Hot-Water…](https://www.mitsubishi-electric.co.nz/materials/PRODUCT/Hot-Water-Heat-Pump/QAHV-N560YA-HPB/01_Specifications/SPC_QAHV-N560YA-HPB.pdf) | [Кат] | 03 | Открыта |
| 116 | Весы платформенные 3 т для ящиков/контейнеров с виноградом (терминал) — IND570 (корпус harsh/panel) + платформ | [www.mt.com/content/dam/product_organizations/industry/Ind…](https://www.mt.com/content/dam/product_organizations/industry/IndustrialTerminals/30372927_08_MAR_DS_IND570xx_EN_LTR.pdf) | [Кат] | 03 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 117 | NetaJet 4G List of configurator items, V002.01, февраль 2018 | [www.netafim.com/globalassets/netajet-4g-lp/netajet-4g-lis…](https://www.netafim.com/globalassets/netajet-4g-lp/netajet-4g-list-of-configurator-items-11.4.18.pdf) | [Кат] | 03, 08 | Открыта |
| 118 | Газоанализатор CO₂ (датчик NDIR) — GDA 4350 (NDIR, диапазон 5 % об.) | [www.onetemp.com.au/wp-content/uploads/2024/01/GDA-4350-CO…](https://www.onetemp.com.au/wp-content/uploads/2024/01/GDA-4350-CO2-Sensor-Datasheet.pdf) | [Кат] | 03 | Открыта |
| 119 | Капсулятор — MINIBLOC OTTICO | [www.resale.de/robino-und-galandrino-minibloc/Nr-169824224](https://www.resale.de/robino-und-galandrino-minibloc/Nr-169824224) | [Кат] | 03 | Открыта |
| 120 | Насос пожаротушения внутреннего противопожарного водопровода — CR 45-2 A-F-A-E-HQQE (96122799) | [www.solarics.de/cdn/shop/files/96122799_CR_452_AFAEHQQE.pdf](https://www.solarics.de/cdn/shop/files/96122799_CR_452_AFAEHQQE.pdf) | [Кат] | 03 | Открыта |
| 121 | Намывной (кизельгуровый) фильтр с горизонтальными дисками — MAC/5 | [www.spadoni.it/wp-content/uploads/2024/05/Filtri_a-dischi…](https://www.spadoni.it/wp-content/uploads/2024/05/Filtri_a-dischi_orizzontali_serie-MAC.pdf) | [Кат] | 03 | Открыта |
| 122 | 5. ЛОС (бытового типа, справочно) — ТОПАС 150 (двухкорпусная с распределительной ёмкостью) | [www.topol-eco.ru/upload/iblock/0c7/katalog_uosv_topas.pdf](https://www.topol-eco.ru/upload/iblock/0c7/katalog_uosv_topas.pdf) | [Кат] | 03 | Открыта |
| 123 | Компактная установка для хозяйственно-бытовых стоков АБК — TOPAS S 5 (5–8 ЭЖ) | [www.topolwater.com/en/products/domestic-wwtps/topas-s/](https://www.topolwater.com/en/products/domestic-wwtps/topas-s/) | [Кат] | 03 | Открыта |
| 124 | Увлажнитель погреба — Hygromaster | [www.winemaster.fr/en/wine-cellar-air-conditioner/hygromas…](https://www.winemaster.fr/en/wine-cellar-air-conditioner/hygromaster/) | [Кат] | 03 | Открыта |
| 125 | Пожарный насос внутреннего противопожарного водопровода (2×5 л/с) — CR 45-x или установка Hydro MX 1/1 — подоб | [new-shop.ksm.kz/media/egfntd/ntdgo/SP_RK_4.01-101-2012.pdf](https://new-shop.ksm.kz/media/egfntd/ntdgo/SP_RK_4.01-101-2012.pdf) | [НПА/НТД] | 03 | Открыта |

### 05_Расчёт

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 126 | — | [www.awri.com.au/wp-content/uploads/ImprovingRefrigeration…](https://www.awri.com.au/wp-content/uploads/ImprovingRefrigerationEfficiency.pdf) | [Нау] | 05 | Открыта |
| 127 | — | [orda.kz/ot-lozy-do-butylki-pochemu-kazahstanskomu-vinu-tr…](https://orda.kz/ot-lozy-do-butylki-pochemu-kazahstanskomu-vinu-trudno-konkurirovat-s-importom-416592/) | [СМИ] | 05, 09 | Открыта |

### 06_Участок

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 128 | Open-Meteo Elevation API (Copernicus DEM GLO-90) | [api.open-meteo.com/v1/elevation](https://api.open-meteo.com/v1/elevation) | [Гео/Данные] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 129 | models=era5_land, era5 | [archive-api.open-meteo.com/v1/archive](https://archive-api.open-meteo.com/v1/archive) | [Гео/Данные] | 06 | Открыта |
| 130 | Зеркало Overpass API (OSM): ПС, ЛЭП, дороги, landuse, водотоки, ООПТ. Метка данных OSM 2026-11-15T20:24Z. © уч | [maps.mail.ru/osm/tools/overpass/api/interpreter](https://maps.mail.ru/osm/tools/overpass/api/interpreter) | [Гео/Данные] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 131 | ISRIC SoilGrids 2.0 (классы WRB, свойства почв) | [rest.isric.org/soilgrids/v2.0/](https://rest.isric.org/soilgrids/v2.0/) | [Гео/Данные] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 132 | OSRM (маршруты по OSM) | [router.project-osrm.org/](https://router.project-osrm.org/) | [Гео/Данные] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 133 | Esri World Imagery (© Esri, Maxar, Earthstar Geographics) | [server.arcgisonline.com/ArcGIS/rest/services/World_Imager…](https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer) | [Гео/Данные] | 06 | Открыта |
| 134 | OSM: ПС «Чилик» 220/110/35/10 кВ | [www.openstreetmap.org/way/1103905577](https://www.openstreetmap.org/way/1103905577) | [Гео/Данные] | 06 | Открыта |
| 135 | OSM: ПС у Тургеня (без названия) | [www.openstreetmap.org/way/1492738094](https://www.openstreetmap.org/way/1492738094) | [Гео/Данные] | 06 | Открыта |
| 136 | OSM: ПС у Шонжы (без названия) | [www.openstreetmap.org/way/1550745914](https://www.openstreetmap.org/way/1550745914) | [Гео/Данные] | 06 | Открыта |
| 137 | Водный кодекс РК 2025 г. (адрес по типовой схеме, не сверен) | [adilet.zan.kz/rus/docs/K2500000178](https://adilet.zan.kz/rus/docs/K2500000178) | [НПА/НТД] | 06, 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 138 | Brian Eife. The Napa Valley of Central Asia? (Arba закапывает лозы на зиму) | [bellisariostudentmedia.psu.edu/story/the-napa-valley-of-c…](https://bellisariostudentmedia.psu.edu/story/the-napa-valley-of-central-asia) | [Нау] | 06 | Открыта |
| 139 | Департамент АИС ГЗК: схемы, почвенная карта, картограмма категорий земель | [aisgzk.kz/aisgzk/ru/content/maps/](https://aisgzk.kz/aisgzk/ru/content/maps/) | [ОФ] | 06 | Открыта |
| 140 | МЧС РК / «Казакстан Гарыш Сапары»: населённые пункты в сейсмических зонах от 7 баллов, Алматинская обл. | [arcgis.gharysh.kz/server/rest/services/KM_MCHS/NP_Seism_z…](https://arcgis.gharysh.kz/server/rest/services/KM_MCHS/NP_Seism_zone/MapServer) | [ОФ] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 141 | МЧС РК: экстент паводков по опасному уровню (гидропосты) | [argissrv.gharysh.kz/arcgis/rest/services/MCHS/Extent_pavo…](https://argissrv.gharysh.kz/arcgis/rest/services/MCHS/Extent_pavodki/MapServer) | [ОФ] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 142 | МЧС РК: селеопасные и оползнеопасные зоны (100 и 500 м) | [argissrv.gharysh.kz/arcgis/rest/services/MCHS/Extent_sele…](https://argissrv.gharysh.kz/arcgis/rest/services/MCHS/Extent_seleopolzen/MapServer) | [ОФ] | 06 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 143 | Портал земельных торгов | [e-auction.gosreestr.kz/](https://e-auction.gosreestr.kz/) | [ОФ] | 06 | Не ответил (таймаут) |
| 144 | Публичная кадастровая карта (НАО «Правительство для граждан») | [map.gov4c.kz/egkn/](https://map.gov4c.kz/egkn/) | [ОФ] | 06 | Открыта |
| 145 | АО «АЖК». Исполнение инвестпрограммы (ПСД реконструкции ПС-68И «Шелек») — из 04 | [www.azhk.kz/images/260901-x-1.xlsx](https://www.azhk.kz/images/260901-x-1.xlsx) | [ОФ] | 06 | Открыта |
| 146 | АО «АЖК». Информация о резерве, наличии свободных и доступных мощностей… сетей 35 кВ и выше за 3 кв. 2026 г. ( | [www.azhk.kz/images/261005-x-1.xlsx](https://www.azhk.kz/images/261005-x-1.xlsx) | [ОФ] | 06 | Открыта |
| 147 | АО «АЖК». Есикский РЭС | [www.azhk.kz/ru/company/region/esikskii](https://www.azhk.kz/ru/company/region/esikskii) | [ОФ] | 06 | Открыта |
| 148 | АО «АЖК». Шелекский РЭС | [www.azhk.kz/ru/company/region/shelekskii](https://www.azhk.kz/ru/company/region/shelekskii) | [ОФ] | 06 | Открыта |
| 149 | Tengrinews: провалы напряжения в Енбекшиказахском р-не | [tengrinews.kz/home-news/hotim-normalnoy-jizni-jiteli-alma…](https://tengrinews.kz/home-news/hotim-normalnoy-jizni-jiteli-almatinskoy-oblasti-jaluyutsya-605065/) | [СМИ] | 06 | Открыта |
| 150 | Jancis Robinson: статья о Arba (каменистые почвы долины) | [www.jancisrobinson.com/articles/wwc21-arba-kazakhstan](https://www.jancisrobinson.com/articles/wwc21-arba-kazakhstan) | [СМИ] | 06 | Закрыта для автоматической проверки (403) — проверить в браузере |

### 08_Орошение_БПЛА

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 151 | NASA POWER Climatology API v2.10.1, 2001–2025 | [power.larc.nasa.gov/api/temporal/climatology/point?…latit…](https://power.larc.nasa.gov/api/temporal/climatology/point?…latitude=43.43&longitude=77.62) | [Гео/Данные] | 08 | Адрес API (не страница) — запросы с параметрами работали при расчёте |
| 152 | XAG P150 Max — Specs | [www.xa.com/en/p150max/p150maxspecs](https://www.xa.com/en/p150max/p150maxspecs) | [Дилер/Магазин] | 08 | Открыта |
| 153 | DJI, «Grape Vineyard Farming…», 17.10.2024 | [ag.dji.com/case-studies/vineyard-dji-agriculture-solution](https://ag.dji.com/case-studies/vineyard-dji-agriculture-solution) | [Кат] | 08 | Открыта |
| 154 | DJI Agras T100 — Specs | [ag.dji.com/t100/specs](https://ag.dji.com/t100/specs) | [Кат] | 08 | Открыта |
| 155 | DJI Agras T25P — Specs | [ag.dji.com/t25p/specs](https://ag.dji.com/t25p/specs) | [Кат] | 08 | Открыта |
| 156 | DroneDJ: анонс T55, T100 Dual Battery | [dronedj.com/2026/07/02/new-dji-agricultural-drones-agras/](https://dronedj.com/2026/07/02/new-dji-agricultural-drones-agras/) | [Кат] | 08 | Открыта |
| 157 | Казгидромет, «Климат Алматы» (нормы 1991–2020) | [kazhydromet.kz/en/klimat/almaty](https://kazhydromet.kz/en/klimat/almaty) | [Кат] | 08 | Открыта |
| 158 | METER TEROS 12 tech specs | [metergroup.com/products/teros-12/teros-12-tech-specs/](https://metergroup.com/products/teros-12/teros-12-tech-specs/) | [Кат] | 08 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 159 | DJI DB1560/DB800 User Guide (мультиязычный, англ. с. 2–10) | [summit-agro.com/ar/es/wp-content/uploads/2026/02/Bateria-…](https://summit-agro.com/ar/es/wp-content/uploads/2026/02/Bateria-DB1560-DB800-Manual-de-Usuario.pdf) | [Кат] | 08 | Открыта |
| 160 | Netafim NetaJet 5G product sheet | [www.netafim.co.za/globalassets/sa-uploads/nsa_productshee…](https://www.netafim.co.za/globalassets/sa-uploads/nsa_productsheet_netajet5g_march2026.pdf) | [Кат] | 08 | Открыта |
| 161 | Правила использования БАС (приказ № 706, рег. 22031) | [adilet.zan.kz/rus/docs/V2000022031](https://adilet.zan.kz/rus/docs/V2000022031) | [НПА/НТД] | 08, 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 162 | FAOLEX kaz80484 | [faolex.fao.org/docs/pdf/kaz80484.pdf](https://faolex.fao.org/docs/pdf/kaz80484.pdf) | [НПА/НТД] | 08 | Открыта |
| 163 | Приказ № 340 от 12.05.2023 | [zakon.uchet.kz/rus/docs/V2300032476](https://zakon.uchet.kz/rus/docs/V2300032476) | [НПА/НТД] | 08 | Открыта |
| 164 | Файзиев Ж. Н., Фархадов А. А. «Влияние различных норм капельного орошения…», Universum: химия и биология № 8(1 | [7universum.com/typeset/nature/8146/articles/23243/Fayziev…](https://7universum.com/typeset/nature/8146/articles/23243/Fayziev%20Zhamoliddin%20Nasirovich.pdf) | [Нау] | 08 | Открыта |
| 165 | Acta Scientiarum: Agronomy (2024), БПЛА против ранцевого опрыскивателя, милдью | [doaj.org/article/0f701202af5b45fda93ea4605959bdf2](https://doaj.org/article/0f701202af5b45fda93ea4605959bdf2) | [Нау] | 08 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 166 | Туринский университет (цитирует Spigno 2015: выжимка, гребни, осадок) | [iris.unito.it/retrieve/e27ce42b-d0d9-2581-e053-d805fe0acb…](https://iris.unito.it/retrieve/e27ce42b-d0d9-2581-e053-d805fe0acbaa/500.pdf) | [Нау] | 08 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 167 | FAO-56 гл. 6 | [www.fao.org/4/x0490e/x0490e0b.htm](https://www.fao.org/4/x0490e/x0490e0b.htm) | [Нау] | 08 | Открыта |
| 168 | OIV Collective Expertise «Managing by-products of vitivinicultural origin», 2018, с. 9 | [www.oiv.int/public/medias/6268/managing-viticulture-by-pr…](https://www.oiv.int/public/medias/6268/managing-viticulture-by-products-print.pdf) | [Нау] | 08 | Открыта |
| 169 | zakon.kz: зоны полётов БАС до 200 м над городами | [www.zakon.kz/pravo/6390617-polety-bespilotnikov-otregulir…](https://www.zakon.kz/pravo/6390617-polety-bespilotnikov-otregulirovali-v-kazakhstane.html) | [СМИ] | 08 | Открыта |
| 170 | zakon.kz, 27.04.2026 | [www.zakon.kz/pravo/6515963-ispolzovanie-vozdushnogo-prost…](https://www.zakon.kz/pravo/6515963-ispolzovanie-vozdushnogo-prostranstva-kazakhstana-vneseny-izmeneniya.html) | [СМИ] | 08, 11 | Открыта |

### 09_Экономика

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 171 | — | [alco24.kz/c/vino/fabricator/arba-wine/](https://alco24.kz/c/vino/fabricator/arba-wine/) | [Дилер/Магазин] | 09 | Открыта |
| 172 | — | [almawine.kz/catalog/vino/beloe/18008/](https://almawine.kz/catalog/vino/beloe/18008/) | [Дилер/Магазин] | 09 | Открыта |
| 173 | — | [almawine.kz/catalog/vino/krasnoe/15253/](https://almawine.kz/catalog/vino/krasnoe/15253/) | [Дилер/Магазин] | 09 | **Не открывается (404)** |
| 174 | — | [champagne.kz/product/?product=1334](https://champagne.kz/product/?product=1334) | [Дилер/Магазин] | 09 | Открыта |
| 175 | — | [newelitalco.kz/ru/catalog/shirak-arba-shiraz-136-075l_87](https://newelitalco.kz/ru/catalog/shirak-arba-shiraz-136-075l_87) | [Дилер/Магазин] | 09 | Открыта |
| 176 | — | [newxo.kz/product/silk-alley-merlot-075-l](https://newxo.kz/product/silk-alley-merlot-075-l) | [Дилер/Магазин] | 09 | Открыта |
| 177 | — | [pegas61.ru/products/butylka-bordo-0-75-2/](https://pegas61.ru/products/butylka-bordo-0-75-2/) | [Дилер/Магазин] | 09 | Открыта |
| 178 | — | [satu.kz/Ktp-250kva.html](https://satu.kz/Ktp-250kva.html) | [Дилер/Магазин] | 09 | Открыта |
| 179 | — | [satu.kz/Podstantsii-2ktp.html](https://satu.kz/Podstantsii-2ktp.html) | [Дилер/Магазин] | 09 | Открыта |
| 180 | — | [shop.chinchin.kz/catalog/vino/lagul_arba_saperavi_0_75_l/](https://shop.chinchin.kz/catalog/vino/lagul_arba_saperavi_0_75_l/) | [Дилер/Магазин] | 09 | Не ответил (таймаут) |
| 181 | — | [twood.fr/en/products/barrique-225l](https://twood.fr/en/products/barrique-225l) | [Дилер/Магазин] | 09 | Закрыта для автоматической проверки (429) — проверить в браузере |
| 182 | — | [upakovkatorg.ru/spetsializirovanaja-upakovka/kryshki-dlja…](https://upakovkatorg.ru/spetsializirovanaja-upakovka/kryshki-dlja-butylok/probki-vinnye-i-konyachnye-korkovye-i-rezbovye/aglomerirovannaya-korkovaya-probka-dlya-vina-s-2-mya-naturalnymi-diskami) | [Дилер/Магазин] | 09 | Открыта |
| 183 | — | [wolt.com/ru/kaz/almaty/venue/smallala28](https://wolt.com/ru/kaz/almaty/venue/smallala28) | [Дилер/Магазин] | 09 | Открыта |
| 184 | — | [www.almawine.kz/catalog/vino/krasnoe/](https://www.almawine.kz/catalog/vino/krasnoe/) | [Дилер/Магазин] | 09 | Открыта |
| 185 | — | [www.destiller.com/wine/grapes-presses/pneumatic-presses](https://www.destiller.com/wine/grapes-presses/pneumatic-presses) | [Дилер/Магазин] | 09 | Открыта |
| 186 | — | [www.destiller.com/wine/labelling](https://www.destiller.com/wine/labelling) | [Дилер/Магазин] | 09 | Открыта |
| 187 | — | [www.tcwequipment.com/products/quinti-wine-bottling-lines](https://www.tcwequipment.com/products/quinti-wine-bottling-lines) | [Дилер/Магазин] | 09 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 188 | — | [www.wineandbarrels.eu/shop/20-wine-barrels/](https://www.wineandbarrels.eu/shop/20-wine-barrels/) | [Дилер/Магазин] | 09 | Открыта |
| 189 | — | [www.winemakersdepot.com/Zambelli/Effe-50](https://www.winemakersdepot.com/Zambelli/Effe-50) | [Дилер/Магазин] | 09 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 190 | — | [apps.apple.com/kz/app/arba-wine-family/id1512898192](https://apps.apple.com/kz/app/arba-wine-family/id1512898192) | [Кат] | 09 | Открыта |
| 191 | — | [energyprom.kz/articles-ru/industries-ru/bezvinnye-proizvo…](https://energyprom.kz/articles-ru/industries-ru/bezvinnye-proizvodstvo-vina-v-kazahstane-padaet-vtoroj-god-podryad/) | [Кат] | 09 | Открыта |
| 192 | — | [standard.kz/ru/post/2026_11_kazaxstancy-stali-pit-mense-k…](https://standard.kz/ru/post/2026_11_kazaxstancy-stali-pit-mense-koniaka-vina-i-piva-286) | [Кат] | 09 | Открыта |
| 193 | — | [www.semey-vodokanal.kz/news/338-nazar-audaryyz-vnimanie-i…](https://www.semey-vodokanal.kz/news/338-nazar-audaryyz-vnimanie-istochnik-https-wwwsemey-vodokanalkz-page-2-.html) | [Кат] | 09 | Открыта |
| 194 | не открылась. Копия:  — открылась.  — открылась карточка «старой редакции» от 10.06.2025. Копия kaf.kz (ред. 2 | [adilet.zan.kz/rus/docs/V1800017320](https://adilet.zan.kz/rus/docs/V1800017320) | [НПА/НТД] | 09, 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 195 | — | [adilet.zan.kz/rus/docs/V2100022057](https://adilet.zan.kz/rus/docs/V2100022057) | [НПА/НТД] | 09 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 196 | — | [adilet.zan.kz/rus/docs/V2100025174](https://adilet.zan.kz/rus/docs/V2100025174) | [НПА/НТД] | 09 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 197 | — | [cdb.kz/sistema/pravovaya-baza/ob-ustanovlenii-stavok-plat…](https://cdb.kz/sistema/pravovaya-baza/ob-ustanovlenii-stavok-platy-za-polzovanie-vodnymi-resursami-iz-poverkhnostnykh-istochnikov-almatinskoy-oblasti/) | [НПА/НТД] | 09 | Открыта |
| 198 | — | [www.alta.ru/tamdoc/25kz0682/](https://www.alta.ru/tamdoc/25kz0682/) | [НПА/НТД] | 09 | Открыта |
| 199 | — | [s3.wp.wsu.edu/uploads/sites/2056/2023/05/Small-Winery-Inv…](https://s3.wp.wsu.edu/uploads/sites/2056/2023/05/Small-Winery-Investments-and-Operating-Costs.pdf) | [Нау] | 09 | Открыта |
| 200 | — | [almatysu.kz/tarify.html](https://almatysu.kz/tarify.html) | [ОФ] | 09 | Открыта |
| 201 | — | [esalmaty.kz/ru/i4160](https://esalmaty.kz/ru/i4160) | [ОФ] | 09 | Открыта |
| 202 | — | [nationalbank.kz/rss/get_rates.cfm?fdate=16.11.2026](https://nationalbank.kz/rss/get_rates.cfm?fdate=16.11.2026) | [ОФ] | 09 | Открыта |
| 203 | — | [qazsu.kz/Потребителям/](https://qazsu.kz/Потребителям/) | [ОФ] | 09 | Открыта |
| 204 | — | [stat.gov.kz/ru/region/almatyobl/](https://stat.gov.kz/ru/region/almatyobl/) | [ОФ] | 09 | Открыта |
| 205 | — | [www.azhk.kz/ru/tarify](https://www.azhk.kz/ru/tarify) | [ОФ] | 09 | Открыта |
| 206 | — | [www.esalmaty.kz/images/docs/2025/2609112312-x-1.pdf](https://www.esalmaty.kz/images/docs/2025/2609112312-x-1.pdf) | [ОФ] | 09 | Открыта |
| 207 | — | [arbawine.com/ru/order](https://arbawine.com/ru/order) | [С] | 09 | Открыта |
| 208 | — | [airpress.kz/economics/fermeram-vozmeshhenie-zatrat-poliv-…](https://airpress.kz/economics/fermeram-vozmeshhenie-zatrat-poliv-80-proczentov/) | [СМИ] | 09 | Открыта |
| 209 | — | [ashlandcontainer.com/blog/wine-packaging-pricing-guide](https://ashlandcontainer.com/blog/wine-packaging-pricing-guide) | [СМИ] | 09 | Открыта |
| 210 | — | [bes.media/news/nalogoviy-kodeks-2026-chto-izmenitsya-dlya…](https://bes.media/news/nalogoviy-kodeks-2026-chto-izmenitsya-dlya-biznesa-rk-v-novom-godu/) | [СМИ] | 09 | Открыта |
| 211 | — | [cler.pro/blog/baza-znaniy/sozdat-vinogradnik-chto-eto-i-s…](https://cler.pro/blog/baza-znaniy/sozdat-vinogradnik-chto-eto-i-skolko-stoit/) | [СМИ] | 09 | Открыта |
| 212 | — | [damu.kz/upload/Files/Biznes-plani/Biznes_plan_Vyrashivani…](https://damu.kz/upload/Files/Biznes-plani/Biznes_plan_VyrashivanieVinnogoVinogradaIStolovykhSortovVinogradaVVinogradnikakh.pdf) | [СМИ] | 09 | Открыта |
| 213 | — | [finratings.kz/data/salary/average/](https://finratings.kz/data/salary/average/) | [СМИ] | 09 | Открыта |
| 214 | — | [forbes.kz/news/newsid_184152](https://forbes.kz/news/newsid_184152) | [СМИ] | 09 | Открыта |
| 215 | — | [inbusiness.kz/ru/last/kapelnoe-oroshenie-vyroslo-pochti-v…](https://inbusiness.kz/ru/last/kapelnoe-oroshenie-vyroslo-pochti-v-shest-raz-v-kazahstane) | [СМИ] | 09 | Открыта |
| 216 | — | [inbusiness.kz/ru/news/kazahstane-pereschitali-tarify-na-vodu](https://inbusiness.kz/ru/news/kazahstane-pereschitali-tarify-na-vodu) | [СМИ] | 09 | Открыта |
| 217 | — | [llamasfinancial.com/how-much-does-it-cost-to-produce-a-bo…](https://llamasfinancial.com/how-much-does-it-cost-to-produce-a-bottle-of-wine/) | [СМИ] | 09 | Открыта |
| 218 | — | [mybuh.kz/news/stavki-aktsizov-na-alkogolnuyu-produktsiyu-…](https://mybuh.kz/news/stavki-aktsizov-na-alkogolnuyu-produktsiyu-v-2026-godu/) | [СМИ] | 09 | Открыта |
| 219 | — | [pro1c.kz/news/zakonodatelstvo/aktsizy-v-novom-nalogovom-k…](https://pro1c.kz/news/zakonodatelstvo/aktsizy-v-novom-nalogovom-kodekse-2026-goda-chto-izmenilos/) | [СМИ] | 09 | Открыта |
| 220 | — | [profi-dom.kz/sklady](https://profi-dom.kz/sklady) | [СМИ] | 09 | Открыта |
| 221 | — | [sdchenma.com/blog/wine-fermentation-tank-price-features-c…](https://sdchenma.com/blog/wine-fermentation-tank-price-features-comparison-2025-guide/) | [СМИ] | 09 | Открыта |
| 222 | — | [stroihub.com/blog/angary-iz-sendvich-paneley](https://stroihub.com/blog/angary-iz-sendvich-paneley) | [СМИ] | 09 | Открыта |
| 223 | — | [tengrinews.kz/private_finance/nazvana-srednyaya-zarplata-…](https://tengrinews.kz/private_finance/nazvana-srednyaya-zarplata-v-kazahstane-novyie-dannyie-611447/) | [СМИ] | 09 | Открыта |
| 224 | — | [thepolishedpalate.substack.com/p/where-your-money-goes-in…](https://thepolishedpalate.substack.com/p/where-your-money-goes-in-wine) | [СМИ] | 09 | Открыта |
| 225 | — | [uchet.kz/news/nds-2026-stavki-zachet-i-lgoty-glavnoe/](https://uchet.kz/news/nds-2026-stavki-zachet-i-lgoty-glavnoe/) | [СМИ] | 09 | Открыта |
| 226 | — | [uppersetup.com/ru/blog/employer-payroll-taxes-and-contrib…](https://uppersetup.com/ru/blog/employer-payroll-taxes-and-contributions-in-kazakhstan-2026) | [СМИ] | 09 | Открыта |
| 227 | — | [vc.ru/money/2883329-formirovanie-tseny-na-vino-v-rossii](https://vc.ru/money/2883329-formirovanie-tseny-na-vino-v-rossii) | [СМИ] | 09 | Открыта |
| 228 | — | [wine-and-spirits.md/orientirovochnye-tseny-na-vinograd-te…](https://wine-and-spirits.md/orientirovochnye-tseny-na-vinograd-tehnicheskih-sortov-urozhaya-2025/) | [СМИ] | 09 | Открыта |
| 229 | — | [www.cepaos.com/en-AU/blog/production-cost-bottle-wine-aus…](https://www.cepaos.com/en-AU/blog/production-cost-bottle-wine-australia) | [СМИ] | 09 | Открыта |
| 230 | — | [www.inform.kz/ru/skolko-stoit-vinograd-v-kazahstane-76f90c](https://www.inform.kz/ru/skolko-stoit-vinograd-v-kazahstane-76f90c) | [СМИ] | 09 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 231 | — | [www.inshymkent.kz/news/1666588/v-uko-sadovnik-vnedril-nov…](https://www.inshymkent.kz/news/1666588/v-uko-sadovnik-vnedril-novuu-tehnologiu-vyrasivania-vinograda-na-kamenistoj-pocve) | [СМИ] | 09 | Открыта |
| 232 | — | [www.nur.kz/nurfin/economy/2451924-potreblenie-alkogolya-p…](https://www.nur.kz/nurfin/economy/2451924-potreblenie-alkogolya-padaet-a-ceny-na-nego-rastut-v-kazahstane/) | [СМИ] | 09 | Открыта |
| 233 | — | [www.nur.kz/nurfin/economy/2454438-kakie-zarplaty-platyat-…](https://www.nur.kz/nurfin/economy/2454438-kakie-zarplaty-platyat-v-malom-biznese-kazahstana/) | [СМИ] | 09 | Открыта |
| 234 | — | [www.pressdemocrat.com/2026/07/23/napa-small-winery-regula…](https://www.pressdemocrat.com/2026/07/23/napa-small-winery-regulation-cost-case-study-cal-poly/) | [СМИ] | 09 | Открыта |
| 235 | — | [www.weproject.media/articles/detail/prazdnik-urozhaya-gla…](https://www.weproject.media/articles/detail/prazdnik-urozhaya-glavnoe-sobytie-goda-dlya-vinodelni-arba-wine/) | [СМИ] | 09 | Открыта |
| 236 | — | [www.wineandbeersupply.com/blogs/content/mobile-bottling-v…](https://www.wineandbeersupply.com/blogs/content/mobile-bottling-vs-in-house-bottling-cost-breakdown) | [СМИ] | 09 | Открыта |

### 11_Нормативы

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 237 | не открылась.  — открылась (неофициальный источник | [ybcase.com/company-services/legal-services/postanovka-na-…](https://ybcase.com/company-services/legal-services/postanovka-na-ucet-bespilotnoj-aviacionnoj-sistemy-v-kazahstane) | [Б/у] | 11 | Открыта |
| 238 | ЭК Приложение 1 (ОВОС / скрининг) | [pavlodar.com/zakon/?all=110001&dok=06850](https://pavlodar.com/zakon/?all=110001&dok=06850) | [Дилер/Магазин] | 11 | Открыта |
| 239 | ЭК Приложение 2 (категории I–III) | [pavlodar.com/zakon/?all=110002&dok=06850](https://pavlodar.com/zakon/?all=110002&dok=06850) | [Дилер/Магазин] | 11 | Открыта |
| 240 | ЭК ст. 12 | [pavlodar.com/zakon/?dok=06850&uro=080012](https://pavlodar.com/zakon/?dok=06850&uro=080012) | [Дилер/Магазин] | 11 | Открыта |
| 241 | ЭК ст. 87 | [pavlodar.com/zakon/?dok=06850&uro=080087](https://pavlodar.com/zakon/?dok=06850&uro=080087) | [Дилер/Магазин] | 11 | Открыта |
| 242 | ЭК ст. 106 | [pavlodar.com/zakon/?dok=06850&uro=080106](https://pavlodar.com/zakon/?dok=06850&uro=080106) | [Дилер/Магазин] | 11 | Открыта |
| 243 | ЭК ст. 110 | [pavlodar.com/zakon/?dok=06850&uro=080110](https://pavlodar.com/zakon/?dok=06850&uro=080110) | [Дилер/Магазин] | 11 | Открыта |
| 244 | ЭК ст. 317 | [pavlodar.com/zakon/?dok=06850&uro=080324](https://pavlodar.com/zakon/?dok=06850&uro=080324) | [Дилер/Магазин] | 11 | Открыта |
| 245 | ЭК ст. 338 | [pavlodar.com/zakon/?dok=06850&uro=080346](https://pavlodar.com/zakon/?dok=06850&uro=080346) | [Дилер/Магазин] | 11 | Открыта |
| 246 | ВК ст. 45 | [pavlodar.com/zakon/?dok=07002&uro=080045](https://pavlodar.com/zakon/?dok=07002&uro=080045) | [Дилер/Магазин] | 11 | Открыта |
| 247 | ВК ст. 46 | [pavlodar.com/zakon/?dok=07002&uro=080046](https://pavlodar.com/zakon/?dok=07002&uro=080046) | [Дилер/Магазин] | 11 | Открыта |
| 248 | ВК ст. 85 | [pavlodar.com/zakon/?dok=07002&uro=080085](https://pavlodar.com/zakon/?dok=07002&uro=080085) | [Дилер/Магазин] | 11 | Открыта |
| 249 | ВК ст. 86 | [pavlodar.com/zakon/?dok=07002&uro=080086](https://pavlodar.com/zakon/?dok=07002&uro=080086) | [Дилер/Магазин] | 11 | Открыта |
| 250 | ВК ст. 123 | [pavlodar.com/zakon/?dok=07002&uro=080123](https://pavlodar.com/zakon/?dok=07002&uro=080123) | [Дилер/Магазин] | 11 | Открыта |
| 251 | ВК ст. 134 | [pavlodar.com/zakon/?dok=07002&uro=080134](https://pavlodar.com/zakon/?dok=07002&uro=080134) | [Дилер/Магазин] | 11 | Открыта |
| 252 | ВК РК — справка (опубликование, ввод в действие, отмена ВК 2003) | [pavlodar.com/zakon/info?dok=07002](https://pavlodar.com/zakon/info?dok=07002) | [Дилер/Магазин] | 11 | Открыта |
| 253 | не открылась. Копия:  — открылась. Приказ № 987:  — открылась карточка | [base.spinform.ru/show_doc.fwx?rgn=127901](https://base.spinform.ru/show_doc.fwx?rgn=127901) | [Кат] | 11 | Открыта |
| 254 | ВНТП 25-85 «Нормы технологического проектирования винодельческих заводов…» (СССР) (meganorm) | [meganorm.ru/Data1/9/9947/index.htm](https://meganorm.ru/Data1/9/9947/index.htm) | [Кат] | 11 | Открыта |
| 255 | Приказ ҚР ДСМ-2, полный текст исходной редакции | [pharmreviews.kz/categories/dokumenty/prikaz-i-o-ministra-…](https://pharmreviews.kz/categories/dokumenty/prikaz-i-o-ministra-zdravookhraneniya-rk-ot-11-yanvarya-2022-goda-r-dsm-2) | [Кат] | 11 | Открыта |
| 256 | не открылась. Копия:  — открылась | [adilet.zan.kz/rus/docs/G24RR000761](https://adilet.zan.kz/rus/docs/G24RR000761) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 257 | Официальная копия:  — не открылась. Рабочие копии:  — открылась, консолидированный текст с пометкой «Начало де | [adilet.zan.kz/rus/docs/H18EV000098](https://adilet.zan.kz/rus/docs/H18EV000098) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 258 | adilet:  — нет (JS).<br>prg:  — карточка, да.<br>Полный текст: pavlodar.com/zakon/?dok=06850 (база 08.09.2026) | [adilet.zan.kz/rus/docs/K2100000400](https://adilet.zan.kz/rus/docs/K2100000400) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 259 | не открылась. Копия:  — открылась. Приказ № 987:  — открылась карточка | [adilet.zan.kz/rus/docs/V1500010422](https://adilet.zan.kz/rus/docs/V1500010422) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 260 | не открылась | [adilet.zan.kz/rus/docs/V2100022673](https://adilet.zan.kz/rus/docs/V2100022673) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 261 | adilet:  — нет.<br>prg doc_id=35482139 — карточка, да.<br>Текст: cdb.kz (ред. 13.11.2023) — да | [adilet.zan.kz/rus/docs/V2100023538](https://adilet.zan.kz/rus/docs/V2100023538) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 262 | ТР «Общие требования к пожарной безопасности» (adilet V2100024045) | [adilet.zan.kz/rus/docs/V2100024045](https://adilet.zan.kz/rus/docs/V2100024045) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 263 | не открылась. Копия:  — открылась (PDF, текст декодирован | [adilet.zan.kz/rus/docs/V2100025366](https://adilet.zan.kz/rus/docs/V2100025366) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 264 | не открылась (JS-заглушка | [adilet.zan.kz/rus/docs/V2200026447](https://adilet.zan.kz/rus/docs/V2200026447) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 265 | не открылась.  — открылась;  — открылась (карточка | [adilet.zan.kz/rus/docs/Z070000301_](https://adilet.zan.kz/rus/docs/Z070000301_) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 266 | не открылась.  — открылась (демо, ст. 1–9 | [adilet.zan.kz/rus/docs/Z990000429_](https://adilet.zan.kz/rus/docs/Z990000429_) | [НПА/НТД] | 11 | Открыта (текст акта подгружается скриптом — проверить в браузере) |
| 267 | eec.eaeunion.org / docs.eaeunion.org: страница открылась (50 КБ), но текст ТР не извлечён. Рабочая копия:  — о | [base.garant.ru/70106650/](https://base.garant.ru/70106650/) | [НПА/НТД] | 11 | Открыта |
| 268 | Официальная копия:  — не открылась. Рабочие копии:  — открылась, консолидированный текст с пометкой «Начало де | [base.garant.ru/72123354/](https://base.garant.ru/72123354/) | [НПА/НТД] | 11 | Открыта |
| 269 | не открылась.  — открылась;  — открылась (карточка | [cdb.kz/sistema/pravovaya-baza/o-bezopasnosti-pishchevoy-p…](https://cdb.kz/sistema/pravovaya-baza/o-bezopasnosti-pishchevoy-produktsii/) | [НПА/НТД] | 11 | Открыта |
| 270 | Правила инвестсубсидирования АПК (№ 317), ред. 2018 — историческая | [cdb.kz/sistema/pravovaya-baza/o-vnesenii-izmeneniya-v-pri…](https://cdb.kz/sistema/pravovaya-baza/o-vnesenii-izmeneniya-v-prikaz-ispolnyayushchego-obyazannosti-ministra-selskogo-khozyaystva-respubliki-kazakhstan-ot-23-iyulya-2018-goda-317-ob-utverzhdenii-pravil-subsidirovaniya-po-vozmeshcheniyu-chasti-raskhodov-ponesennykh-subektom-agropromyshlen/) | [НПА/НТД] | 11 | Открыта |
| 271 | То же, полный текст | [cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-instruktsii…](https://cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-instruktsii-po-opredeleniyu-kategorii-obekta-okazyvayushchego-negativnoe-vozdeystvie/) | [НПА/НТД] | 11 | Открыта |
| 272 | Классификатор отходов (приказ № 314) | [cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-klassifikat…](https://cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-klassifikatora-otkhodov-314/) | [НПА/НТД] | 11 | Открыта |
| 273 | не открылась. Копия:  — открылась. Приказ № 987:  — открылась карточка | [cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-kvalifikats…](https://cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-kvalifikatsionnykh-trebovaniy-i-perechnya-dokumentov-podtverzhdayushchikh-sootvetstvie-im-dlya-osushchestvleniya-deyatelnosti-v-sferakh-proizvodstva-etilovogo-spirta-proizvodstva-alkogolnoy-produktsii-khraneniya-i-optovoy-realizatsii-/) | [НПА/НТД] | 11 | Открыта |
| 274 | открылась.  — не открылась (сайт недоступен | [cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-pravil-subs…](https://cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-pravil-subsidirovaniya-povysheniya-urozhaynosti-i-kachestva-produktsii-rastenievodst/) | [НПА/НТД] | 11 | Открыта |
| 275 | не открылась. Копия:  — открылась | [cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-tekhnichesk…](https://cdb.kz/sistema/pravovaya-baza/ob-utverzhdenii-tekhnicheskogo-reglamenta-o-bezopasnosti-alkogolnoy-produktsii-761/) | [НПА/НТД] | 11 | Открыта |
| 276 | не открылась. Копия:  — открылась (PDF, текст декодирован | [faolex.fao.org/docs/pdf/kaz109150.pdf](https://faolex.fao.org/docs/pdf/kaz109150.pdf) | [НПА/НТД] | 11 | Открыта |
| 277 | СП «...по установлению СЗЗ производственных объектов» (приказ МНЭ № 237, 2015, утратил силу) | [faolex.fao.org/docs/pdf/kaz184904.pdf](https://faolex.fao.org/docs/pdf/kaz184904.pdf) | [НПА/НТД] | 11 | Открыта |
| 278 | СП РК 2.03-30-2017* | [new-shop.ksm.kz/%D0%A1%D0%9F%20%D0%A0%D0%9A%202.03-30-201…](https://new-shop.ksm.kz/%D0%A1%D0%9F%20%D0%A0%D0%9A%202.03-30-2017.pdf) | [НПА/НТД] | 11 | **Не открывается (404)** |
| 279 | а также q=62133, 62485, 60896 | [new-shop.ksm.kz/catalog/search/?q=62619](https://new-shop.ksm.kz/catalog/search/?q=62619) | [НПА/НТД] | 11 | Открыта |
| 280 | перечень ЕГФНТД | [new-shop.ksm.kz/egfntd/ntdgo/kds/](https://new-shop.ksm.kz/egfntd/ntdgo/kds/) | [НПА/НТД] | 11 | Открыта |
| 281 | СН РК 4.01-03-2013 (с изм. № 58-НҚ от 01.06.2026) | [new-shop.ksm.kz/media/egfntd/ntdgo/%D0%A1%D0%9D_%D0%A0%D0…](https://new-shop.ksm.kz/media/egfntd/ntdgo/%D0%A1%D0%9D_%D0%A0%D0%9A_4.01-03-2013_58-%D0%9D%D0%9A.pdf) | [НПА/НТД] | 11 | Открыта |
| 282 | СП РК 3.01-103-2012* «Генеральные планы промышленных предприятий» (PDF ЕГФНТД) | [new-shop.ksm.kz/media/egfntd/ntdgo/%D0%A1%D0%9F_%D0%A0%D0…](https://new-shop.ksm.kz/media/egfntd/ntdgo/%D0%A1%D0%9F_%D0%A0%D0%9A_3.01-103-2012.pdf) | [НПА/НТД] | 11 | Открыта |
| 283 | СП РК 3.02-127-2013 «Производственные здания» (PDF) | [new-shop.ksm.kz/media/egfntd/ntdgo/%D0%A1%D0%9F_%D0%A0%D0…](https://new-shop.ksm.kz/media/egfntd/ntdgo/%D0%A1%D0%9F_%D0%A0%D0%9A_3.02-127-2013.pdf) | [НПА/НТД] | 11 | Открыта |
| 284 | СН РК 2.02-01-2023 «Пожарная безопасность зданий и сооружений» (PDF) | [new-shop.ksm.kz/media/egfntd/ntdgo/2_02_01_2023.pdf](https://new-shop.ksm.kz/media/egfntd/ntdgo/2_02_01_2023.pdf) | [НПА/НТД] | 11 | Открыта |
| 285 | СН РК 3.01-03-2011 «Генеральные планы промышленных предприятий» (PDF ЕГФНТД) | [new-shop.ksm.kz/media/egfntd/ntdgo/3_01_03_2011.pdf](https://new-shop.ksm.kz/media/egfntd/ntdgo/3_01_03_2011.pdf) | [НПА/НТД] | 11 | Открыта |
| 286 | СН РК 3.02-27-2023 «Производственные здания» (PDF) | [new-shop.ksm.kz/media/egfntd/ntdgo/3_02_27_2023.pdf](https://new-shop.ksm.kz/media/egfntd/ntdgo/3_02_27_2023.pdf) | [НПА/НТД] | 11 | Открыта |
| 287 | СП РК 2.02-101-2022 | [new-shop.ksm.kz/media/egfntd/ntdgo/C%D0%9F_%D0%A0%D0%9A_2…](https://new-shop.ksm.kz/media/egfntd/ntdgo/C%D0%9F_%D0%A0%D0%9A_2_5p3E3XW.02-101.pdf) | [НПА/НТД] | 11 | Открыта |
| 288 | СНиП РК 4.01-02-2009 «Водоснабжение. Наружные сети и сооружения» (PDF) | [new-shop.ksm.kz/media/egfntd/ntdgo/SANPIN_4.01_02_2009.pdf](https://new-shop.ksm.kz/media/egfntd/ntdgo/SANPIN_4.01_02_2009.pdf) | [НПА/НТД] | 11 | Открыта |
| 289 | СП РК 2.04-104-2012 | [new-shop.ksm.kz/media/egfntd/ntdgo/SP_RK_2.04-104-2012.pdf](https://new-shop.ksm.kz/media/egfntd/ntdgo/SP_RK_2.04-104-2012.pdf) | [НПА/НТД] | 11 | Открыта |
| 290 | То же, online.zakon.kz | [online.zakon.kz/Document/?doc_id=38237881](https://online.zakon.kz/Document/?doc_id=38237881) | [НПА/НТД] | 11 | Открыта |
| 291 | Официальная копия:  — не открылась. Рабочие копии:  — открылась, консолидированный текст с пометкой «Начало де | [ppt.ru/obzory/vstupaet-v-silu/reshenie-soveta-yeek-20-05-…](https://ppt.ru/obzory/vstupaet-v-silu/reshenie-soveta-yeek-20-05-2026-62) | [НПА/НТД] | 11 | Открыта |
| 292 | Обзор решения Совета ЕЭК № 21 от 21.02.2025 | [ppt.ru/obzory/vstupaet-v-silu/reshenie-soveta-yevraziysko…](https://ppt.ru/obzory/vstupaet-v-silu/reshenie-soveta-yevraziyskoy-ekonomicheskoy-komissii-21-02-2025-n-21) | [НПА/НТД] | 11 | Открыта |
| 293 | не открылась.  — открылась (демо, ст. 1–9 | [prg.kz/document/?doc_id=1013922](https://prg.kz/document/?doc_id=1013922) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 294 | РДС РК 4.04-185-2003 (prg 30002371) | [prg.kz/document/?doc_id=30002371](https://prg.kz/document/?doc_id=30002371) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 295 | не открылась.  — открылась;  — открылась (карточка | [prg.kz/document/?doc_id=30114108](https://prg.kz/document/?doc_id=30114108) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 296 | СНиП РК 4.01-02-2009 «Водоснабжение. Наружные сети и сооружения» (prg 30657627) | [prg.kz/document/?doc_id=30657627](https://prg.kz/document/?doc_id=30657627) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 297 | Пост. акимата Алматинской обл. № 246 о ВЗ и ВП рек (в т. ч. Тургень) | [prg.kz/document/?doc_id=31105608](https://prg.kz/document/?doc_id=31105608) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 298 | СН РК 4.01-03-2011 Водоотведение. Наружные сети и сооружения | [prg.kz/document/?doc_id=31130718](https://prg.kz/document/?doc_id=31130718) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 299 | СН РК 4.01-02-2011 (утратил силу) | [prg.kz/document/?doc_id=31219913](https://prg.kz/document/?doc_id=31219913) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 300 | открылась только карточка.  — открылась (консультация 11.10.2023 | [prg.kz/document/?doc_id=31548200](https://prg.kz/document/?doc_id=31548200) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 301 | Правила пожарной безопасности (prg 31623095) | [prg.kz/document/?doc_id=31623095](https://prg.kz/document/?doc_id=31623095) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 302 | СН РК 3.02-31-2023 / СП РК 3.02-131-2012 (здания для переработки с/х продукции) (prg 31713776) | [prg.kz/document/?doc_id=31713776](https://prg.kz/document/?doc_id=31713776) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 303 | СП РК 2.04-103-2013 (молниезащита) (prg 31753585) | [prg.kz/document/?doc_id=31753585](https://prg.kz/document/?doc_id=31753585) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 304 | Аннотация к приказу № 120-НҚ | [prg.kz/document/?doc_id=31784276](https://prg.kz/document/?doc_id=31784276) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 305 | ПУЭ РК (приказ МЭ № 230 от 20.03.2015, рег. 10851) (prg 32102729) | [prg.kz/document/?doc_id=32102729](https://prg.kz/document/?doc_id=32102729) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 306 | Правила приёма сточных вод в централизованные системы водоотведения (приказ МПС № 436) | [prg.kz/document/?doc_id=32276040](https://prg.kz/document/?doc_id=32276040) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 307 | не открылась. Копия:  — открылась.  — открылась карточка «старой редакции» от 10.06.2025. Копия kaf.kz (ред. 2 | [prg.kz/document/?doc_id=32510615](https://prg.kz/document/?doc_id=32510615) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 308 | СН РК 4.01-03-2013 | [prg.kz/document/?doc_id=32531475](https://prg.kz/document/?doc_id=32531475) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 309 | Водный кодекс РК 2025, карточка | [prg.kz/document/?doc_id=32546243](https://prg.kz/document/?doc_id=32546243) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 310 | СП РК 2.02-101-2022 (prg 33195180) | [prg.kz/document/?doc_id=33195180](https://prg.kz/document/?doc_id=33195180) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 311 | Аннотация к приказу № 436 | [prg.kz/document/?doc_id=33574781](https://prg.kz/document/?doc_id=33574781) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 312 | СН РК 2.02-01-2023 (пожарная безопасность зданий) (prg 34065963) | [prg.kz/document/?doc_id=34065963](https://prg.kz/document/?doc_id=34065963) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 313 | СП РК 4.04-106-2013 (prg 34120625) | [prg.kz/document/?doc_id=34120625](https://prg.kz/document/?doc_id=34120625) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 314 | открылась (карточка).  — открылась | [prg.kz/document/?doc_id=34239360](https://prg.kz/document/?doc_id=34239360) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 315 | СП РК 4.01-101-2012 | [prg.kz/document/?doc_id=34509278](https://prg.kz/document/?doc_id=34509278) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 316 | СН РК 3.02-31-2023 / СП РК 3.02-131-2012 (здания для переработки с/х продукции) (34566000) | [prg.kz/document/?doc_id=34566000](https://prg.kz/document/?doc_id=34566000) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 317 | ПТЭЭП РК (приказ МЭ № 246 от 30.03.2015, рег. 10949) (prg 35069881) | [prg.kz/document/?doc_id=35069881](https://prg.kz/document/?doc_id=35069881) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 318 | Правила выдачи экологических разрешений (приказ № 319) | [prg.kz/document/?doc_id=35264761](https://prg.kz/document/?doc_id=35264761) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 319 | То же, карточка | [prg.kz/document/?doc_id=35482139](https://prg.kz/document/?doc_id=35482139) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 320 | СП РК 4.02-101-2012 / СН РК 4.02-01-2011 (ОВиК) (35664024) | [prg.kz/document/?doc_id=35664024](https://prg.kz/document/?doc_id=35664024) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 321 | Правила установления границ ВЗ и ВП (приказ МВРИ № 120-НҚ) | [prg.kz/document/?doc_id=35667718](https://prg.kz/document/?doc_id=35667718) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 322 | СП РК 4.04-108-2014 (prg 35776703) | [prg.kz/document/?doc_id=35776703](https://prg.kz/document/?doc_id=35776703) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 323 | СП РК 4.02-101-2012 / СН РК 4.02-01-2011 (ОВиК) (prg 36515945) | [prg.kz/document/?doc_id=36515945](https://prg.kz/document/?doc_id=36515945) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 324 | открылась только карточка.  — открылась (консультация 11.10.2023 | [prg.kz/document/?doc_id=36958820](https://prg.kz/document/?doc_id=36958820) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 325 | СП РК 4.01-103-2013 | [prg.kz/document/?doc_id=36998352](https://prg.kz/document/?doc_id=36998352) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 326 | СН РК 2.02-02-2023 / СП РК 2.02-102-2022 (пожарная автоматика) (prg 37065985) | [prg.kz/document/?doc_id=37065985](https://prg.kz/document/?doc_id=37065985) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 327 | Строительный кодекс РК № 253-VIII от 09.01.2026 (prg 37270679) | [prg.kz/document/?doc_id=37270679](https://prg.kz/document/?doc_id=37270679) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 328 | СП РК 4.04-109-2013 (prg 37401178) | [prg.kz/document/?doc_id=37401178](https://prg.kz/document/?doc_id=37401178) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 329 | Правила субсидирования водосберегающих технологий орошения (приказ МВРИ № 153-НҚ) | [prg.kz/document/?doc_id=37512461](https://prg.kz/document/?doc_id=37512461) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 330 | prg.kz  — открылась (карточка и преамбула, демо).<br>pharmreviews.kz — полный текст исходной редакции (опублик | [prg.kz/document/?doc_id=38237881](https://prg.kz/document/?doc_id=38237881) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 331 | открылась (карточка | [prg.kz/document/?doc_id=38279735](https://prg.kz/document/?doc_id=38279735) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 332 | СП РК 2.04-104-2012 (освещение) (prg 38304152) | [prg.kz/document/?doc_id=38304152](https://prg.kz/document/?doc_id=38304152) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 333 | СП РК 4.04-105-2014 (prg 38338891) | [prg.kz/document/?doc_id=38338891](https://prg.kz/document/?doc_id=38338891) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 334 | СН РК 2.02-02-2023 / СП РК 2.02-102-2022 (пожарная автоматика) (38466567) | [prg.kz/document/?doc_id=38466567](https://prg.kz/document/?doc_id=38466567) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 335 | СН РК 4.04-07-2023 / СП РК 4.04-107-2013 (prg 38520762) | [prg.kz/document/?doc_id=38520762](https://prg.kz/document/?doc_id=38520762) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 336 | СН РК 2.04-01-2011 (освещение) (prg 38588660) | [prg.kz/document/?doc_id=38588660](https://prg.kz/document/?doc_id=38588660) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 337 | То же, карточка | [prg.kz/document/?doc_id=38589343](https://prg.kz/document/?doc_id=38589343) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 338 | СН РК 4.04-08-2023 (prg 38667733) | [prg.kz/document/?doc_id=38667733](https://prg.kz/document/?doc_id=38667733) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 339 | СН РК 4.04-07-2023 / СП РК 4.04-107-2013 (39059542) | [prg.kz/document/?doc_id=39059542](https://prg.kz/document/?doc_id=39059542) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 340 | СН РК 4.01-01-2011 (внутренний водопровод) (prg 39287975) | [prg.kz/document/?doc_id=39287975](https://prg.kz/document/?doc_id=39287975) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 341 | ТР «Общие требования к пожарной безопасности» (приказ МЧС № 405 от 17.08.2021, рег. 24045) (prg 39453446) | [prg.kz/document/?doc_id=39453446](https://prg.kz/document/?doc_id=39453446) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 342 | СП РК 4.01-102-2013 | [prg.kz/document/?doc_id=39762686](https://prg.kz/document/?doc_id=39762686) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 343 | adilet:  — нет (JS).<br>prg:  — карточка, да.<br>Полный текст: pavlodar.com/zakon/?dok=06850 (база 08.09.2026) | [prg.kz/document/?doc_id=39768520](https://prg.kz/document/?doc_id=39768520) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 344 | Приказ МЭ № 383-н/қ от 16.10.2026 «О внесении изменений и дополнений в некоторые приказы МЭ РК» (prg 39895436) | [prg.kz/document/?doc_id=39895436](https://prg.kz/document/?doc_id=39895436) | [НПА/НТД] | 11 | Открыта (карточка документа) |
| 345 | Официальная копия:  — не открылась. Рабочие копии:  — открылась, консолидированный текст с пометкой «Начало де | [www.alta.ru/tamdoc/18sr0098/](https://www.alta.ru/tamdoc/18sr0098/) | [НПА/НТД] | 11 | Открыта |
| 346 | Правила № 317, ред. 28.10.2025 | [www.kaf.kz/upload/iblock/b1d/weqahu9ai76iqxdeeeeoksb5l16i…](https://www.kaf.kz/upload/iblock/b1d/weqahu9ai76iqxdeeeeoksb5l16in6ok/Pravila-investsubsidirovaniya-_317-s-izmen.-na-28.10.25g.-na-rus.yaz..doc) | [НПА/НТД] | 11 | **Не открывается (404)** |
| 347 | не открылась | [zakon.uchet.kz/rus/docs/V1500011151](https://zakon.uchet.kz/rus/docs/V1500011151) | [НПА/НТД] | 11 | Открыта |
| 348 | Приказ МЗ от 31.12.2025 № 174 (рег. 37774) | [zakon.uchet.kz/rus/docs/V2500037774](https://zakon.uchet.kz/rus/docs/V2500037774) | [НПА/НТД] | 11 | Открыта |
| 349 | открылась.  — не открылась (сайт недоступен | [zakon.uchet.kz/rus/docs/V2600037924](https://zakon.uchet.kz/rus/docs/V2600037924) | [НПА/НТД] | 11 | Открыта |
| 350 | Приказ МФ РК № 302 от 14.05.2026 | [zakon.uchet.kz/rus/docs/V2600038722](https://zakon.uchet.kz/rus/docs/V2600038722) | [НПА/НТД] | 11 | Открыта |
| 351 | Приказ МЗ от 15.05.2026 № 51 (рег. 38728) | [zakon.uchet.kz/rus/docs/V2600038728](https://zakon.uchet.kz/rus/docs/V2600038728) | [НПА/НТД] | 11 | Открыта |
| 352 | ДСЭК Акмолинской обл.: «Что изменилось в порядке установления СЗЗ с 1 июля 2026 года?» (приказ № 51) | [www.gov.kz/memleket/entities/departament-kkbtu-akmolinsk/…](https://www.gov.kz/memleket/entities/departament-kkbtu-akmolinsk/press/news/details/1263498?lang=ru) | [ОФ] | 11 | Открыта |
| 353 | открылась | [www.gov.kz/memleket/entities/moa/press/news/details/11803…](https://www.gov.kz/memleket/entities/moa/press/news/details/1180322?lang=ru) | [ОФ] | 11 | Открыта |
| 354 | Bizmedia: изменения требований к СЗЗ (приказ от 31.12.2025) | [bizmedia.kz/2026-01-13-v-kazahstane-izmenili-trebovaniya-…](https://bizmedia.kz/2026-01-13-v-kazahstane-izmenili-trebovaniya-k-sanitarno-zashhitnym-zonam-dlya-biznesa/) | [СМИ] | 11 | Открыта |
| 355 | Статья о лицензировании (Mybuh) | [mybuh.kz/useful/proizvodstvo-slaboalkogolnoy-produktsii-k…](https://mybuh.kz/useful/proizvodstvo-slaboalkogolnoy-produktsii-kak-poluchit-litsenziyu.html) | [СМИ] | 11 | Открыта |
| 356 | открылась | [www.zakon.kz/pravo/6523140-v-kazakhstane-uzakonili-ispolz…](https://www.zakon.kz/pravo/6523140-v-kazakhstane-uzakonili-ispolzovanie-aerotaksi-i-bespilotnoy-aviatsii.html) | [СМИ] | 11 | Открыта |
| 357 | Правила пользования электроэнергией (приказ МЭ № 143, рег. 10403) | [www.zakon.kz/pravo/6536834](https://www.zakon.kz/pravo/6536834) | [СМИ] | 11 | Открыта |

### 13_Аналоги

| № | Источник | Ссылка | Тип | Где использован | Проверка 16.11.2026 |
|---|---|---|---|---|---|
| 358 | breezart.ru/where-to-buy/ | [www.breezart.ru/where-to-buy/](https://www.breezart.ru/where-to-buy/) | [Дилер/Магазин] | 13 | Не ответил (таймаут) |
| 359 | Uniud «Enhancing energy efficiency in wineries: a novel benchmarking approach». | [air.uniud.it/](https://air.uniud.it/) | [Кат] | 13 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 360 | hh.kz — ГОЛД ПРОДУКТ, АО | [almaty.hh.kz/employer/171613](https://almaty.hh.kz/employer/171613) | [Кат] | 13 | Открыта |
| 361 | hh.kz — поиск «винзавод» | [almaty.hh.kz/search/vacancy?text=%D0%B2%D0%B8%D0%BD%D0%B7…](https://almaty.hh.kz/search/vacancy?text=%D0%B2%D0%B8%D0%BD%D0%B7%D0%B0%D0%B2%D0%BE%D0%B4&area=40) | [Кат] | 13 | Открыта |
| 362 | artinox.tilda.ws/en/about-company | [artinox.tilda.ws/en/about-company](https://artinox.tilda.ws/en/about-company) | [Кат] | 13 | Открыта |
| 363 | Vela R. et al. «Improved energy efficiency in wineries using data from audits», Ciência Téc. Vitiv. 32(1) 62-7 | [dspace.uevora.pt/rdpc/bitstream/10174/21284/1/Vela_et_al_…](https://dspace.uevora.pt/rdpc/bitstream/10174/21284/1/Vela_et_al_ctv20173201p62.pdf) | [Кат] | 13 | Открыта |
| 364 | EU4Business, Winery Khareba (7–9 тыс. т; модели не названы; не аналог). | [eu4business.eu/success-stories/major-winemaking-company-u…](https://eu4business.eu/success-stories/major-winemaking-company-ups-production-with-eu4business-support/) | [Кат] | 13 | Открыта |
| 365 | gege24, объект 2764 (Кварели). | [gege24.com/en/object/2764](https://gege24.com/en/object/2764) | [Кат] | 13 | Открыта |
| 366 | gold-product.com/proizvodstvo-8 | [gold-product.com/proizvodstvo-8/](https://gold-product.com/proizvodstvo-8/) | [Кат] | 13 | Открыта |
| 367 | Realting, винзавод в Кварели, ID 3533264. | [realting.com/georgia/property/3533264](https://realting.com/georgia/property/3533264) | [Кат] | 13 | Открыта |
| 368 | Тезис UniPD по холодильной машине Tenuta Ca' Liva (Rhoss, ограничение договора 100 кВт; игристые вина). | [thesis.unipd.it/handle/20.500.12608/106411](https://thesis.unipd.it/handle/20.500.12608/106411) | [Кат] | 13 | Закрыта для автоматической проверки (403) — проверить в браузере |
| 369 | vaillant.kz | [vaillant.kz/](https://vaillant.kz/) | [Кат] | 13 | Открыта |
| 370 | Paolino S. «Applicazione della norma UNI CEI EN ISO 50001 alle Cantine Vinicole», PoliTo. | [webthesis.biblio.polito.it/7791/1/tesi.pdf](https://webthesis.biblio.polito.it/7791/1/tesi.pdf) | [Кат] | 13 | Открыта |
| 371 | winenomad.kz — Turgen Wines | [winenomad.kz/turgen-wines.html](https://winenomad.kz/turgen-wines.html) | [Кат] | 13 | Открыта |
| 372 | Winetitles «Bucher Vaslin at the heart of Waite winery». | [winetitles.com.au/?p=61842](https://winetitles.com.au/?p=61842) | [Кат] | 13 | Открыта |
| 373 | Agroscope / AGRIDEA, курс 06.07.2023 (около 0,24 кВт·ч/л). | [www.agroscope.admin.ch/dam/fr/sd-web/zseMxOcqfkfc/present…](https://www.agroscope.admin.ch/dam/fr/sd-web/zseMxOcqfkfc/presentations-cours-agridea-20230706.pdf) | [Кат] | 13 | Открыта |
| 374 | Bucher Industries «From pressure to serenity» (Cave Fin Bec). | [www.bucherindustries.com/en/record-collections/stories/fr…](https://www.bucherindustries.com/en/record-collections/stories/from-pressure-to-serenity) | [Кат] | 13 | Открыта |
| 375 | buchervaslin.com/en/Ourdealers/ | [www.buchervaslin.com/en/Ourdealers/](https://www.buchervaslin.com/en/Ourdealers/) | [Кат] | 13 | Открыта |
| 376 | Castello di Neive «Cantina nuova». | [www.castellodineive.it/cantina-nuova?lang=en](https://www.castellodineive.it/cantina-nuova?lang=en) | [Кат] | 13 | Открыта |
| 377 | daikinkz.com/ru_ru/contact.html | [www.daikinkz.com/ru_ru/contact.html](https://www.daikinkz.com/ru_ru/contact.html) | [Кат] | 13 | Открыта |
| 378 | enoveneta.it/en/contacts/ | [www.enoveneta.it/en/contacts/](https://www.enoveneta.it/en/contacts/) | [Кат] | 13 | Открыта |
| 379 | eseficiencia.es «El sector bodeguero rebajaría su factura energética». | [www.eseficiencia.es/2012/12/13/el-sector-bodeguero-rebaja…](https://www.eseficiencia.es/2012/12/13/el-sector-bodeguero-rebajaria-su-factura-energetica) | [Кат] | 13 | Открыта |
| 380 | gai1946.com/en/sales-network/ | [www.gai1946.com/en/sales-network/](https://www.gai1946.com/en/sales-network/) | [Кат] | 13 | Открыта |
| 381 | gortani.com/en/contacts | [www.gortani.com/en/contacts](https://www.gortani.com/en/contacts) | [Кат] | 13 | Открыта |
| 382 | Green Industries SA «Mitchell Wines — Managing tariffs by managing demand». | [www.greenindustries.sa.gov.au/case-studies/mitchell-wines…](https://www.greenindustries.sa.gov.au/case-studies/mitchell-wines-managing-tariffs-by-managing-demand) | [Кат] | 13 | Открыта |
| 383 | 2XE / Green Industries SA «Winery Resource Efficiency Benchmark Report». | [www.greenindustries.sa.gov.au/documents/Winery%20Resource…](https://www.greenindustries.sa.gov.au/documents/Winery%20Resource%20Efficiency%20Benchmark%20Report.pdf?downloadable=1) | [Кат] | 13 | Открыта |
| 384 | grundfos.com/kz | [www.grundfos.com/kz](https://www.grundfos.com/kz) | [Кат] | 13 | Не ответил (таймаут) |
| 385 | inmatec.de/en/ | [www.inmatec.de/en/](https://www.inmatec.de/en/) | [Кат] | 13 | Открыта |
| 386 | inoxpa.com | [www.inoxpa.com/](https://www.inoxpa.com/) | [Кат] | 13 | Открыта |
| 387 | kaercher.com/kz — официальные дилеры | [www.kaercher.com/kz/servis/podderzhka/oficialnye-dilery.html](https://www.kaercher.com/kz/servis/podderzhka/oficialnye-dilery.html) | [Кат] | 13 | Открыта |
| 388 | kaeser.com — Kazakhstan | [www.kaeser.com/int-en/company/about-us/kaeser-worldwide/k…](https://www.kaeser.com/int-en/company/about-us/kaeser-worldwide/kazakhstan) | [Кат] | 13 | Открыта |
| 389 | netafim.com/en/contact-us/ | [www.netafim.com/en/contact-us/](https://www.netafim.com/en/contact-us/) | [Кат] | 13 | Открыта |
| 390 | QFF «Stanthorpe horticulture farm 8». | [www.qff.org.au/newsroom/case-studies/stanthorpe-horticult…](https://www.qff.org.au/newsroom/case-studies/stanthorpe-horticulture-farm-8/) | [Кат] | 13 | **Не открывается (404)** |
| 391 | Réussir Vigne «En Dordogne, un chai innovant pour vinifier seul». | [www.reussir.fr/vigne%2F/en-dordogne-un-chai-innovant-pour…](https://www.reussir.fr/vigne%2F/en-dordogne-un-chai-innovant-pour-vinifier-seul) | [Кат] | 13 | Открыта |
| 392 | Réussir Vigne «En Savoie, une cave coopérative… chai partagé». | [www.reussir.fr/vigne/en-savoie-une-cave-cooperative-de-vi…](https://www.reussir.fr/vigne/en-savoie-une-cave-cooperative-de-vinification-investit-dans-un-chai-partage-pour-faciliter-les) | [Кат] | 13 | Открыта |
| 393 | Réussir «La thermorégulation, un gouffre énergétique». | [www.reussir.fr/vigne/la-thermoregulation-un-gouffre-energ…](https://www.reussir.fr/vigne/la-thermoregulation-un-gouffre-energetique) | [Кат] | 13 | Открыта |
| 394 | Réussir «Le pressoir pneumatique confirme sa polyvalence». | [www.reussir.fr/vigne/le-pneumatique-veritable-couteau-suisse](https://www.reussir.fr/vigne/le-pneumatique-veritable-couteau-suisse) | [Кат] | 13 | Открыта |
| 395 | ENEA, Tallini A. et al., RdS_PTR22-24_PR1.6_LA2.14_275. | [www.ricercasistemaelettrico.enea.it/archivio-documenti/se…](https://www.ricercasistemaelettrico.enea.it/archivio-documenti/send/600-report-progetto-1-6-2022-2023/5700-analisi-energetica-di-casi-di-studio-e-realizzazione-di-una-guida-per-l-efficientamento-energetico-delle-aziende-vitivinicole.html) | [Кат] | 13 | Открыта |
| 396 | Wotol, объявление о б/у Bucher RPF 50 (50 гл ≈ 3,8 т целых гроздей / 8–10 т мезги, около 7 кВт). | [www.wotol.com/product/bucher-rpf-50-pneumatic-press-close…](https://www.wotol.com/product/bucher-rpf-50-pneumatic-press-closed-tank/2616313) | [Кат] | 13 | Открыта |
| 397 | AWRI WIC Winemaking Services. | [www.awri.com.au/wic-winemaking-services/](https://www.awri.com.au/wic-winemaking-services/) | [Нау] | 13 | Открыта |
| 398 | AWRI «Winery refrigeration: opportunities to save electricity». | [www.awri.com.au/wp-content/uploads/2014/06/Winery-refrige…](https://www.awri.com.au/wp-content/uploads/2014/06/Winery-refrigeration-case-study.pdf) | [Нау] | 13 | Открыта |
| 399 | Abbott T. «Energy audit case study…», AWRI Technical Review 235. | [www.awri.com.au/wp-content/uploads/2018/08/Technical_Revi…](https://www.awri.com.au/wp-content/uploads/2018/08/Technical_Review_Issue_235_Abbott.pdf) | [Нау] | 13 | Открыта |
| 400 | Nordestgaard S. «Improving Winery Refrigeration Efficiency — Winery A». | [www.awri.com.au/wp-content/uploads/WineryA-CaseStudyRepor…](https://www.awri.com.au/wp-content/uploads/WineryA-CaseStudyReport.pdf) | [Нау] | 13 | Открыта |
| 401 | forbes.kz — Местное шато | [forbes.kz/articles/mestnoe_shato](https://forbes.kz/articles/mestnoe_shato) | [СМИ] | 13 | Открыта |
| 402 | forbes.kz — Шёлковая аллея | [forbes.kz/articles/shelkovaya_alleya_1559896226](https://forbes.kz/articles/shelkovaya_alleya_1559896226) | [СМИ] | 13 | Открыта |
| 403 | informburo.kz — цех игристого Бахус (реклама) | [informburo.kz/stati/v-zale-9-tysyach-butylok-remyuer-ezhe…](https://informburo.kz/stati/v-zale-9-tysyach-butylok-remyuer-ezhednevno-perevorachivaet-vse-.html) | [СМИ] | 13 | Открыта |
| 404 | the-buyer.net — Tasting the wines of Kazakhstan | [the-buyer.net/wine/tasting-the-wines-of-kazakhstan](https://the-buyer.net/wine/tasting-the-wines-of-kazakhstan) | [СМИ] | 13 | Открыта |
| 405 | weproject.media — Органическое вино… (Chateau Karakemer) | [weproject.media/articles/detail/organicheskoe-vino-yablok…](https://weproject.media/articles/detail/organicheskoe-vino-yabloki-i-korpeshki-kak-vozrozhdat-traditsionnoe-proizvodstvo-v-almaty/) | [СМИ] | 13 | Открыта |
| 406 | nur.kz — Казахстанские виноделы объединились | [www.nur.kz/1082538-kazakhstanskie-vinodely-obedinilis.html](https://www.nur.kz/1082538-kazakhstanskie-vinodely-obedinilis.html) | [СМИ] | 13 | Открыта |

## 3. Неоткрывшиеся ссылки и их влияние на выводы

| Ссылка | Что подтверждала | Влияние |
|---|---|---|
| https://statsnet.co/en/companies/kz/3975074 | statsnet.co — ТОО «ARBA WINE» | Реестровые данные Arba — есть adata, EMIS |
| https://azud.com/wp-content/uploads/2023/02/AZUD_HELIX_AUTO_201-ENG.pdf | Azud Helix Automatic 201 | Электрика контроллера фильтров Azud — в 03 мощность и так НЕИЗВЕСТНО |
| https://www.daikin.eu/content/dam/document-library/catalogues/ac/split/ftxm-r/FTXM-R | Сплит-система АБК/лаборатории — FTXM35R + RXM35R | Кондиционеры АБК 0,99 кВт — значение взято с другой страницы Daikin; ссылка, вероятно, усечена |
| https://e-auction.gosreestr.kz/ | Портал земельных торгов | Земельные торги — юридическая доступность участков в 06 не подтверждена |
| https://almawine.kz/catalog/vino/krasnoe/15253/ | — | Одна из цен Arba — есть другие магазины |
| https://shop.chinchin.kz/catalog/vino/lagul_arba_saperavi_0_75_l/ | — | Цена Arba — есть другие магазины |
| https://new-shop.ksm.kz/%D0%A1%D0%9F%20%D0%A0%D0%9A%202.03-30-2017.pdf | СП РК 2.03-30-2017* | СП РК 2.03-30-2017 (сейсмика) не открыт — в 06/07 сейсмичность по слою МЧС, отмечено «сверить» |
| https://www.kaf.kz/upload/iblock/b1d/weqahu9ai76iqxdeeeeoksb5l16in6ok/Pravila-investsubsidirovaniya-_317-s-izmen.-na-28.10.25g.-na-rus.yaz..doc | Правила № 317, ред. 28.10.2025 | Правила инвестсубсидирования № 317 (документ на сайте КАФ) — проценты субсидий в 09 помечены как допущение |
| https://www.breezart.ru/where-to-buy/ | breezart.ru/where-to-buy/ | Вспомогательная ссылка; цифры продублированы другими источниками или помечены |
| https://www.grundfos.com/kz | grundfos.com/kz | Вспомогательная ссылка; цифры продублированы другими источниками или помечены |
| https://www.qff.org.au/newsroom/case-studies/stanthorpe-horticulture-farm-8/ | QFF «Stanthorpe horticulture farm 8». | Вспомогательная ссылка; цифры продублированы другими источниками или помечены |

## 4. Источники без ссылки (книги, нормы на бумаге)

| Источник | Где | Статус |
|---|---|---|
| Boulton R.B., Singleton V.L., Bisson L.F., Kunkee R.E. Principles and Practices of Winemaking. Springer, 1996 | 02, 05 | Не открывался; теплота брожения взята по AWRI 2012 |
| Ribéreau-Gayon P. et al. Handbook of Enology. Vol. 1–2. Wiley, 2006 | 02 | Не открывался — сверить параметры «ТИПОВОЕ, первоисточник не сверен» |
| Валуйко Г.Г. Технология виноградных вин. Симферополь: Таврида, 2001 | 02 | Не открывался — нормативы выхода сусла по фракциям |
| Кишковский З.Н., Мержаниан А.А. Технология вина. М., 1984 | 02 | Не открывался |
| Кабышев А.В., Обухов С.Г. Расчёт и проектирование систем электроснабжения. Томск: ТПУ, 2005 | 03 (Ки, cosφ) | Из прежнего исследования (лист «Коэффициенты») |
| Радкевич В.Н. и др. Расчёт электрических нагрузок промышленных предприятий. БНТУ, 2013 | 03 | Из прежнего исследования |
| ВНТП 03-86, прил. 15 | 03 | Из прежнего исследования (dnaop.com) |
| Della Toffola, каталог «Impianti di Refrigerazione», с. 7 | 03 (Чиллеры) | Ссылка — в 03, лист «Ведомость»; дата каталога не указана |
| KAZNEX INVEST, 2016 — до 300 тыс. бут./год Arba | 01 | Найден через Times of Central Asia (04.05.2016) — ссылка в 01 |

## 5. Что проверить вручную перед защитой

1. Открыть на **adilet.zan.kz** в браузере все акты из 11_Нормативная_база (особенно санитарные правила СЗЗ — п. о «первичном виноделии» и п. 23 о 2 000 м; Водный кодекс 2025; правила БАС № 706) и сверить действующие редакции.
2. Проверить ссылки с пометкой «Закрыта для автоматической проверки».
3. Сохранить PDF-копии каталогов производителей, на которые опирается 03 (сайты меняются).
4. Для финансов Arba (01) — получить платный отчёт statsnet/adata или ответ компании; оценки ElDala не использовать как отчётность.
5. Для площадки (06) — ручная проверка кадастровой карты map.gov4c.kz/egkn по координатам.
