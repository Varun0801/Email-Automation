import smtplib #secure mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_user = "girik7411@gmail.com"
email_send = "girikumar.kolla@gmail.com"

subject = "Python"

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = 'Python'

body = "Hello! first mail using python script" # The /n separates the message
msg.attach(MIMEText(body,'plain'))


text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

#Next, log in to the server
server.login(email_user, "Kumari96")
#Send the mail

server.sendmail(email_user, email_send, text) 
server.quit()
