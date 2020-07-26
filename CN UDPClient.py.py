#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
# In[11]:
serverName = '192.168.1.28'
serverPort = 5581
Sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
name = input('Your Name')
city = input('Birthplace')
message = "Your name is "+name+" and city you were born is "+city
Sock.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = Sock.recvfrom(2048)
print (modifiedMessage.decode())
Sock.close()


# In[ ]:




