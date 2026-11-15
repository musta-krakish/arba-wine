"""Общие стили для xlsx-файлов исследования."""
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

FONT = "Arial"
_s = Side(style="thin", color="999999")
thin = Border(left=_s, right=_s, top=_s, bottom=_s)
wrap = Alignment(wrap_text=True, vertical="top")
HDR_FILL = PatternFill("solid", fgColor="1F4E78")
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")


def style_title(ws, cell, text):
    ws[cell] = text
    ws[cell].font = Font(name=FONT, bold=True, size=13)


def style_header(ws, row, ncol):
    for c in range(1, ncol + 1):
        cl = ws.cell(row=row, column=c)
        cl.font = Font(name=FONT, bold=True, color="FFFFFF")
        cl.fill = HDR_FILL
        cl.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cl.border = thin


def style_input(cell):
    cell.font = Font(name=FONT, color="0000FF")
    cell.fill = INPUT_FILL


def autowidth(ws, widths):
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


def set_font_all(wb):
    """Arial для всех ячеек, сохраняя жирность/цвет."""
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                f = c.font
                if f is None or f.name != FONT:
                    c.font = Font(name=FONT, bold=f.bold if f else False, italic=f.italic if f else False,
                                  color=f.color if f else None, size=f.size if f and f.size else 10)
