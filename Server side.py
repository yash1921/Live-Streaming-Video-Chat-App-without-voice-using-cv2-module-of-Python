#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Required Libraries-

import socket        #connecting two nodes on a network to communicate with each other.
import json         
import pickle        #converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) .
import cv2           #for image processing, video capture and analysis.


# In[ ]:


#This will return video from the first webcam on your computer

cap = cv2.VideoCapture(0)

#AF_INET refers to the address family ipv4. 
#The SOCK_STREAM means connection oriented TCP protocol.

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#IP address.

ip="192.168.1.5"

#Port number-which is used to identify the process that needs to consume the packet.
port=1234


# In[ ]:


#Bind method assigns an IP address and a port number to a socket instance.

s.bind((ip,port))
print("Binded")

#The listen function is typically used by servers that can have more than one connection request at a time. 

s.listen()


# In[ ]:


#o and addr both are variables, 
#o-where o stores the data from the client.
#addr-it recieves the port number and IP address.
#They recieves the data in the form of bytes.

o , addr = s.accept()

#Making use of string formatting.

print("Connected to {}".format(addr))

#In order to iterate over a block of code as long as the test expression (condition) is true we are using "While loop for the same"
while True:
    
    # ret is a boolean regarding whether or not there was a return.
    # photo is frame where each photo has to be return.
    # photo will be in 3D array form.
    #buffer is an another variable that will store the data into prescribed format.
    
    ret , photo = cap.read()
    
    #buffer is an another variable that will store the data into prescribed format.
    #convert (encode) the image format into streaming data and assign it to memory cache.
    
    ret, buffer = cv2.imencode('.jpg',photo)
    
    #serializes a python object hierarchy and returns the bytes object of the serialized object.
    
    bytedata = pickle.dumps(buffer)
    o.send(bytedata)

    x = o.recv(1000000) #Imposing the limit of data.
    
    #Using try and except block inorder to avoid the error.
    
    try:
        
        #used to load pickled data from a bytes string.
        
        data = pickle.loads(x)
        
        # reads data from specified memory cache and converts (​decodes) data into image format.
        
        data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if data is not None :
            cv2.imshow('serverphoto',data)
            if cv2.waitKey(10) == 13 :
                break
    except: 
        print("Waiting for the client!")
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




