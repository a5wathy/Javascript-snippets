import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login("aswathy241989@gmail.com","rakesh143")
print('logged in')

msg = "YOUR MESSAGE!"
server.sendmail("aswathy241989@gmail.com", "rakesh.scorpion@gmail.com", msg)
server.quit()
