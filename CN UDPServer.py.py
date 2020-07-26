#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
serverPort = 5581
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Sock.bind(('0.0.0.0', serverPort))
print ('The server is ready to receive') 
while 1:
    message, clientAddress = Sock.recvfrom(2048)
    message = message.decode()
    modifiedMessage = message.upper()
    Sock.sendto(modifiedMessage.encode(), clientAddress)


# In[ ]:




