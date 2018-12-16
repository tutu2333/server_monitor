import openpyxl

def read_excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.get_sheet_by_name("sheet1")

    excel_rows = []

    for row in sheet.rows:
        excel_row = []
        for cell in row:
            excel_row.append(cell.value)
        excel_rows.append(excel_row)

    return excel_rows





