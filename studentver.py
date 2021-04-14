#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from glob import glob
import os
from cryptography.fernet import Fernet
import csv


# In[2]:


active = True
while(active==True):
    print("Welcome to the Chapel Attendance Program")
    print("Enter a command to start the program.")
    print("search: search a specific student's chapel records by ID.")
    print("exit: shuts down the program.\n\n")
    x = input()
    
    if( x == "search" ):
        id = input("What is your id number? ")
        
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        
        #This uses te generated key to decrypt the file.
        # using the key
        fernet = Fernet(key)
  
        # opening the encrypted file
        with open('CpytMaster.csv', 'rb') as enc_file:
            encrypted = enc_file.read()

        #decrypting the file
        decrypted = fernet.decrypt(encrypted)
  
        # opening the file in write mode and
        # writing the decrypted data
        with open('CpytMaster.csv', 'wb') as dec_file:
            dec_file.write(decrypted)
            
        searchfile = open('Cpytmaster.csv', 'r')
        reader = csv.reader(searchfile, delimiter = ',')
        totalcount = 0
        guestcount = 0
        nooncount = 0
        sturecitalcount = 0
        faccount=0
        stdenscount = 0
        outsidecount = 0
        namealready = 0
        for row in reader:
            if id in row[3]:
                print (row[3],row[6],)
                totalcount += 1
                if("Guest-Artist" in row[6]):
                    guestcount+= 1
                if("Music-Noon" in row[6]):
                    nooncount+= 1
                if("Student-Recital" in row[6]):
                    sturecitalcount+= 1 
                if("Faculty-Recital" in row[6]):
                    faccount+= 1
                if("Student-Ensemble" in row[6]):
                    stdenscount+= 1
                if("outside" in row[6]):
                    outsidecount+= 1
                    
                    
        print("Total Concerts Attended: ",totalcount )
        print("Guest Artist Concerts Attended: ", guestcount)
        print("Music at Noon Concerts Attended: ", nooncount)
        print("Student Recital Concerts Attended: ", sturecitalcount)
        print("Faculty Recital Concerts Attended: ", faccount)
        print("Student Ensemble Concerts Attended: ", stdenscount)
        print("Outside Professional Concerts Attended: ", outsidecount)
        print("\n\n")
        
        with open('CpytMaster.csv', 'rb') as file:
            original = file.read()    
        encrypted = fernet.encrypt(original)
        with open('CpytMaster.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            
    if (x == 'exit'):
        active = False


# In[ ]:




