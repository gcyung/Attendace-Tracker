#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from glob import glob
import os
from cryptography.fernet import Fernet


# In[2]:


filenames = glob('biola*.csv') 
dataframes = [pd.read_csv(f) for f in filenames]
con = pd.concat([pd.read_csv(fp).assign(Concert=os.path.basename(fp)) for fp in filenames])


# In[3]:


con.sort_values(by=["StudentNumber"], inplace = True)
print(con)
con.to_csv('Master.csv')


# In[10]:


#This function generates an encryption key
key = Fernet.generate_key()
  
# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()


# In[14]:


#This function uses the key to encrypt the master file.
#using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open('master.csv', 'rb') as file:
    original = file.read()
      
# encrypting the file
encrypted = fernet.encrypt(original)
  
# opening the file in write mode and 
# writing the encrypted data
with open('master.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    


# In[15]:


#This uses te generated key to decrypt the file.
# using the key
fernet = Fernet(key)
  
# opening the encrypted file
with open('master.csv', 'rb') as enc_file:
    encrypted = enc_file.read()

#decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('master.csv', 'wb') as dec_file:
    dec_file.write(decrypted)

