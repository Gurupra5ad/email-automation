from openpyxl import load_workbook
wb = load_workbook(filename='mail_id.xlsx', read_only=True)
ws = wb['emails']

for row in ws.rows:
    for cell in row:
        print(cell.value)

wb.close()