import smtplib #secure mail transfer protocol
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls() #transport layer security

#Next, log in to the server
server.login("uppugundla@gmail.com", "Sairam.52")

#Send the mail
msg = "Hello! first mail using python script" # The /n separates the message from the headers
server.sendmail("uppugundla@gmail.com", "polisettijaikanth@gmail.com", msg) 