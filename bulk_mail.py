from openpyxl import load_workbook
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tedwaitforitmosby05@gmail.com', 'iloverobin')
                      
wb = load_workbook(filename='mail_id.xlsx', read_only=True)
ws = wb['emails']

for row in ws.rows:
    for cell in row:
        server.sendmail('tedwaitforitmosby05@gmail.com',
                cell.value,                      
                 'Hey, This is smtp automated mail'
                 )
wb.close()