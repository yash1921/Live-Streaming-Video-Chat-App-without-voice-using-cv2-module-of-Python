#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import urllib
import json
import pickle
import numpy as np
import cv2


# In[ ]:


url = 'http://192.168.1.4:8080/shot.jpg'


# In[ ]:


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip="192.168.1.5"
port=1234


# In[ ]:


s.connect((ip,port))


# In[ ]:


while True:
    
    x = s.recv(1000000)
    print("Recieved")
    
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.resize(img,(700,500))
    ret, buffer = cv2.imencode('.jpg',img)
    bytedata = pickle.dumps(buffer)
    
    s.send(bytedata)
    try:
        data = pickle.loads(x)
        data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if data is not None :
            cv2.imshow('photo',data)
            if cv2.waitKey(10) == 13 :
                break
    except: 
        print("Waiting for the server!")
     
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




