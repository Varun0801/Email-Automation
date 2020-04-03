#used SSL for authentication
#used python3.x version

import base64, ssl  #importing base64 for encoding, ssl for authentication and security reason.
from socket import *

msg = "\r\n I love computer networks!"# the msg to be sent
endmsg = "\r\n.\r\n" #period


# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver 
#Fill in start 
mailserver = 'smtp.gmail.com' #Using Google mail server for smtp
port = 465 #465 for ssl authentication 
#Fill in end

# Create socket called clientSocket and establish a SSL connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM) # Create socket called clientSocket
clientSocket = ssl.wrap_socket(clientSocket) #SSL wrapper for sock
clientSocket.connect((mailserver, port))#connecting SSL connection with mailserver
#Fill in end

recv = clientSocket.recv(2048)#To establishing SSL connection with mailserver
recv = str(recv, 'utf-8') #encoding response from server
print(recv)
if recv[:3] != '220':#condition to check the reply from server
    print('220 reply not received from server.')

# Send HELO command and print server response.

heloCommand = 'HELO Alice\r\n' #HELO command
clientSocket.send(heloCommand.encode('utf-8'))#handshaking with server
recv1 = clientSocket.recv(2048)#storing the response from server
recv1 = str(recv1, 'utf-8')#encoding the response
print(recv1)
if recv1[:3] != '250': #condition to check replay from server
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.

 # Fill in start

authentication_Msg = 'AUTH LOGIN\r\n'#sending AUTH LOGIN Command for authentication
cr_Msg = '\r\n'#declaring variable for carriage return
mail_from = 'qwertyforwork@gmail.com' #from email address
mail_rcpt = input('enter To email:')#To email address thru input
user_name = 'qwertyforwork' #variable for username
pwd = 'jyppeoscgghmqlbf'#variable password
print(authentication_Msg)

clientSocket.send(authentication_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the reseponse from server
print(str(respon, 'utf-8'))

user64 = base64.b64encode(user_name.encode('utf-8'))#encoding username using base64
pass64 = base64.b64encode(pwd.encode('utf-8'))#encoding password using base64
print(user64)

clientSocket.send(user64)#handshaking with server
clientSocket.send(cr_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the reseponse from server
print(str(respon, 'utf-8'))
print(pass64)

clientSocket.send(pass64)#handshaking with server
clientSocket.send(cr_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the reseponse from server
print(str(respon, 'utf-8'))
from_Msg = 'MAIL FROM: <' + mail_from + '>\r\n'#sending MAIL FROM command 
print(from_Msg)

clientSocket.send(from_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the reseponse from server
print(str(respon, 'utf-8'))

# Fill in end

# Send RCPT TO command and print server response.

# Fill in start

rcpt_Msg = 'RCPT TO: <' + mail_rcpt + '>\r\n'#sending RCPT TO command
print(rcpt_Msg)

clientSocket.send(rcpt_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the response from server
print(str(respon, 'utf-8'))

# Fill in end

# Send DATA command and print server response.

# Fill in start

data_Msg = 'DATA\r\n'#Send DATA command
print(data_Msg)

clientSocket.send(data_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the response from server
print(str(respon, 'utf-8'))

# Fill in end

# Send message data.

# Fill in start

mail_body = msg + '\r\n'#  message data
print(mail_body)
clientSocket.send(mail_body.encode('utf-8'))#handshaking with server

# Fill in end

# Message ends with a single period.

# Fill in start

print(endmsg)#Message ends with a single period
clientSocket.send(endmsg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the response from server
print(str(respon, 'utf-8'))

# Fill in end

# Send QUIT command and get server response.

# Fill in start

quit_Msg = 'QUIT\r\n'#Send QUIT command to server
print(quit_Msg)
clientSocket.send(quit_Msg.encode('utf-8'))#handshaking with server
respon = clientSocket.recv(2048)#storing the response from server
print(str(respon, 'utf-8'))

# Fill in end
