"""Расчёт электрических нагрузок учебного варианта (группа В, 03_Электроприемники.xlsx)
по РТМ 36.18.32.4-92. Входные данные — V.json (выгрузка листа «В_Учебный_Arba» с вычисленными формулами)."""
import json, math, sys
V = json.load(open(sys.argv[1]))
def f(x):
    try: return float(x)
    except (TypeError, ValueError): return None
# --- Таблица 1 РТМ (T0 = 10 мин), Ки-столбцы и nэ-строки
KI1 = [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
N = None
# Табл. 1 РТМ 36.18.32.4-92 (п. 2.11), T0 = 10 мин. Только значения из источника; None — в источнике нет.
T1 = {1:[N,N,N,N,N,1.60,1.33,1.14,1.0], 2:[N,N,N,N,N,1.60,1.33,1.14,1.0], 3:[N,N,N,N,N,1.34,1.22,1.14,1.0],
      4:[3.24,2.35,1.91,1.47,1.25,1.21,1.12,1.06,1.0], 5:[2.84,2.09,1.72,1.35,1.16,1.16,1.08,1.03,1.0],
      6:[2.64,1.96,1.62,1.28,1.11,1.13,1.06,1.01,1.0], 7:[2.49,1.86,1.54,1.23,1.12,1.10,1.04,1.0,1.0],
      8:[2.37,1.78,1.48,1.19,1.10,1.08,1.02,1.0,1.0], 9:[2.27,1.71,1.43,1.16,1.09,1.07,1.01,1.0,1.0],
      10:[2.18,1.65,1.39,1.13,1.07,1.05,1.0,1.0,1.0], 11:[N,N,N,1.10,1.06,1.04,1.0,1.0,1.0],
      12:[2.04,1.56,1.32,1.08,1.05,1.03,1.0,1.0,1.0], 13:[N,N,N,1.06,1.04,1.01,1.0,1.0,1.0],
      14:[N,N,N,1.05,1.02,1.0,1.0,1.0,1.0], 15:[1.89,1.46,1.25,1.03,1.0,1.0,1.0,1.0,1.0],
      16:[N,N,N,1.02,1.0,1.0,1.0,1.0,1.0], 17:[N,N,N,1.0,1.0,1.0,1.0,1.0,1.0]}
KI2 = [0.1,0.15,0.2,0.3,0.4,0.5,0.6,0.7]
T2 = [(1,[8.0,5.33,4.0,2.67,2.0,1.6,1.33,1.14]),(2,[5.01,3.44,2.69,1.9,1.52,1.24,1.11,1.0]),(3,[2.94,2.17,1.8,1.42,1.23,1.14,1.08,1.0]),
      (4,[2.28,1.73,1.46,1.19,1.06,1.04,1.0,0.97]),(5,[1.31,1.12,1.02,1.0,0.98,0.96,0.94,0.93]),(8,[1.2,1.0,0.96,0.95,0.94,0.93,0.92,0.91]),
      (10,[1.1,0.97,0.91,0.9,0.9,0.9,0.9,0.9]),(25,[0.8,0.8,0.8,0.85,0.85,0.85,0.9,0.9]),(50,[0.75,0.75,0.75,0.75,0.75,0.8,0.85,0.85]),(10**9,[0.65,0.65,0.65,0.7,0.7,0.75,0.8,0.8])]
def col(ki, cols):  # ближайший меньший столбец (в запас)
    i = max(j for j, c in enumerate(cols) if c <= ki + 1e-9) if ki >= cols[0] else 0
    return i
def kr1(ne, ki):
    ne = max(1, min(int(ne), 17)); v = T1[ne][col(ki, KI1)]
    assert v is not None, f'Кр нет в источнике: nэ={ne}, Ки={ki}'
    return v
def kr2(ne, ki):
    for lim, row in T2:
        if ne <= lim: return row[col(ki, KI2)]
# --- распределение по узлам (ШР) и категориям
NODE = {"Приёмное отделение":"ШР-1 Приёмка и прессование","Прессовое отделение":"ШР-1 Приёмка и прессование",
 "Холодильная станция":"ШР-2 Холодильная станция","Бродильное отделение":"ШР-3 Бродильное отделение",
 "Отделение обработки":"ШР-4 Обработка и компрессорная","Компрессорная":"ШР-4 Обработка и компрессорная",
 "Цех розлива (2 500 бут/ч)":"ШР-5 Розлив и склад","Склад готовой продукции":"ШР-5 Розлив и склад",
 "Погреба":"ШР-6 Вспомогательные","Мойка и санобработка":"ШР-6 Вспомогательные","Водоснабжение":"ШР-6 Вспомогательные",
 "Водоподготовка":"ШР-6 Вспомогательные","Котельная":"ШР-6 Вспомогательные","Лаборатория":"ШР-6 Вспомогательные",
 "Пожарная насосная":"ЩАП Аварийное питание (I кат.)","Освещение":"ЩО Освещение"}
CAT = {"ШР-1 Приёмка и прессование":"II","ШР-2 Холодильная станция":"II","ШР-3 Бродильное отделение":"II (аварийная вентиляция — I)",
 "ШР-4 Обработка и компрессорная":"II/III","ШР-5 Розлив и склад":"III","ШР-6 Вспомогательные":"II/III","ЩАП Аварийное питание (I кат.)":"I","ЩО Освещение":"III (аварийное — I)"}
SEASONAL = {"ШР-1 Приёмка и прессование"}
items = []
for x in V:
    p, n, rez, ki, cs = f(x["p"]), f(x["cnt"]), f(x["rez"]) or 0, f(x["ki"]), f(x["cos"])
    if p is None or ki is None: continue
    nw = int(round(n - rez))
    items.append(dict(name=x["name"], cex=x["cex"], node="ЩАП Аварийное питание (I кат.)" if "аварийная" in x["name"].lower() else NODE[x["cex"]], n=int(n), nw=nw, p=p, ki=ki, tg=math.tan(math.acos(cs)), light=x["cex"]=="Освещение"))
def node_calc(its, table=1):
    pw = [(i["p"], i["nw"]) for i in its if i["nw"] > 0 and not i["light"]]
    sP = sum(p*n for p, n in pw)
    if sP == 0: return None
    sKP = sum(i["p"]*i["nw"]*i["ki"] for i in its if not i["light"])
    sKPtg = sum(i["p"]*i["nw"]*i["ki"]*i["tg"] for i in its if not i["light"])
    nn = sum(n for _, n in pw)
    ne = sP**2 / sum(n*p*p for p, n in pw)
    if ne > nn: ne = nn
    ki = sKP / sP
    kr = kr1(ne, ki) if table == 1 else kr2(ne, ki)
    pr = kr * sKP; pmax = max(p for p, _ in pw)
    if pr < pmax: pr = pmax
    if table == 1: qr = (1.1 if ne <= 10 else 1.0) * sKPtg
    else: qr = kr * sKPtg
    return dict(n=nn, sP=sP, ki=ki, ne=ne, kr=kr, sKP=sKP, sKPtg=sKPtg, pr=pr, qr=qr)
nodes = {}
for i in items: nodes.setdefault(i["node"], []).append(i)
print("== Узлы (табл. 1 РТМ, T0 = 10 мин)")
res = {}
for nd, its in nodes.items():
    if nd == "ЩО Освещение":
        P = sum(i["p"]*i["ki"] for i in its); Q = sum(i["p"]*i["ki"]*i["tg"] for i in its)
        res[nd] = dict(n=len(its), sP=sum(i["p"] for i in its), ki=None, ne=None, kr=None, pr=P, qr=Q)
    else:
        r = node_calc(its); res[nd] = r
    if r is None:
        print(f"{nd:34s} — все приёмники резервные/аварийные, в нормальном режиме в расчёт не входят"); continue
    r = res[nd]; S = math.hypot(r["pr"], r["qr"]); I = S/(math.sqrt(3)*0.4)
    r["S"] = S; r["I"] = I
    print(f'{nd:34s} n={r["n"]:2d} ΣPн={r["sP"]:6.1f} Ки={r["ki"] if r["ki"] is None else round(r["ki"],2)} nэ={r["ne"] if r["ne"] is None else round(r["ne"],1)} Кр={r["kr"]} Pр={r["pr"]:6.1f} Qр={r["qr"]:6.1f} Sр={S:6.1f} Iр={I:6.1f} кат={CAT[nd]}')
def plant(exclude=set()):
    its = [i for i in items if not i["light"] and i["node"] not in exclude]
    pw = [(i["p"], i["nw"]) for i in its if i["nw"] > 0]
    sP = sum(p*n for p, n in pw); sKP = sum(i["p"]*i["nw"]*i["ki"] for i in its); sKPtg = sum(i["p"]*i["nw"]*i["ki"]*i["tg"] for i in its)
    nn = sum(n for _, n in pw); pmax = max(p for p, _ in pw)
    ne = min(nn, 2*sP/pmax); ki = sKP/sP; kr = kr2(int(ne), ki)
    pr = max(kr*sKP, pmax); qr = kr*sKPtg
    L = [i for i in items if i["light"]]; pl = sum(i["p"]*i["ki"] for i in L); ql = sum(i["p"]*i["ki"]*i["tg"] for i in L)
    return dict(sP=sP, nn=nn, ne=ne, ki=ki, kr=kr, sKP=sKP, sKPtg=sKPtg, prs=pr, qrs=qr, pl=pl, ql=ql, P=pr+pl, Q=qr+ql)
for label, ex in (("СЕЗОН (всё оборудование)", set()), ("МЕЖСЕЗОНЬЕ (без ШР-1)", SEASONAL)):
    r = plant(ex); S = math.hypot(r["P"], r["Q"])
    print(f'\n== На шинах 0,4 кВ ТП, {label} (табл. 2 РТМ, T0 = 2,5 ч)')
    print(f'ΣPн={r["sP"]:.1f} n={r["nn"]} nэ=2ΣP/pmax={r["ne"]:.1f} Ки={r["ki"]:.3f} Кр={r["kr"]} ΣКиPн={r["sKP"]:.1f} ΣКиPнtg={r["sKPtg"]:.1f}')
    print(f'Pр.сил={r["prs"]:.1f} Qр.сил={r["qrs"]:.1f} + освещение P={r["pl"]:.1f} Q={r["ql"]:.1f} → Pр={r["P"]:.1f} Qр={r["Q"]:.1f} Sр={S:.1f} кВА cosφ={r["P"]/S:.3f} tgφ={r["Q"]/r["P"]:.3f}')
    if not ex: SEAS = r
# --- КРМ
P, Q = SEAS["P"], SEAS["Q"]; tg1 = Q/P; tg2 = math.tan(math.acos(0.93))
Qk = P*(tg1 - tg2); print(f"\n== КРМ: tgφ1={tg1:.3f} → tgφ2={tg2:.3f} (cosφ 0,93): Qк.треб={Qk:.1f} квар")
for qk in (50, 75):
    Q2 = Q - qk; S2 = math.hypot(P, Q2); print(f"  УКМ {qk} квар: Q={Q2:.1f} S={S2:.1f} cosφ={P/S2:.3f}")
# --- трансформаторы
qk = 50; S2 = math.hypot(P, Q - qk)
print(f"\n== Трансформаторы: Sр после КРМ = {S2:.1f} кВА; при Кз=0,7 Sном ≥ Sр/(2·0,7) = {S2/1.4:.1f} кВА")
TMG = {100:(290,1970,4.5),160:(410,2600,4.5),250:(570,3700,4.5),400:(830,5400,4.5)}
for s in (160, 250):
    kz = S2/(2*s); print(f"  2×{s}: Кз норм = {kz:.2f}; аварийно 1 тр-р: {S2/s:.2f} ({'≤1,4 ОК' if S2/s <= 1.4 else '>1,4'})")
for s in (250, 400):
    print(f"  1×{s}: Кз = {S2/s:.2f}")
r = plant(SEASONAL)
print(f"  межсезонье: Sр без КРМ = {math.hypot(r['P'], r['Q']):.1f} кВА; Кз 2×160 = {math.hypot(r['P'], r['Q'])/320:.2f}")
# --- I категория и ДГУ
I_items = [i for i in items if "аварийн" in i["name"].lower() or i["cex"] == "Пожарная насосная"]
pI = 2*2.2 + 7.5 + 0.2 + 0.1*22.2
print(f"\n== I категория: авар. вентиляция 2×2,2 + пожарный насос 7,5 (1 раб.) + газоанализаторы ≈0,2 + авар. освещение ≈10 % внутр. (2,2) = {pI:.1f} кВт")
pII = 3.0 + 4.4 + 2.2
print(f"   ответственные II (по выбору): насос гликоля 3,0 + общеобм. вентиляция 4,4 + климат погреба 2,2 = {pII:.1f} кВт; всего {pI+pII:.1f} кВт; ×1,25 = {(pI+pII)*1.25:.1f} кВт")
print(f"   пуск двигателя 7,5 кВт: по ГОСТ 33115 до 70 % Pдгу при Pдгу ≤ 60 кВт → Pдгу ≥ {7.5/0.7:.1f} кВт")
json.dump(dict(seas=SEAS), open("/dev/null", "w"))
