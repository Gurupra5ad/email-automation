import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tedwaitforitmosby05@gmail.com', 'iloverobin')
server.sendmail('tedwaitforitmosby05@gmail.com',
                'guruprasad2511@gmail.com',                      
                 'Hey, This is smtp automated mail'
                 )                      