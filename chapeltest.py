#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd
from glob import glob
import os
from cryptography.fernet import Fernet

filenames = glob('biola*.csv') 
dataframes = [pd.read_csv(f) for f in filenames]
con = pd.concat([pd.read_csv(fp).assign(Concert=os.path.basename(fp)) for fp in filenames])
con.sort_values(by=["StudentNumber"], inplace = True)

active = True

while(active==True):
    print("Welcome to the Concert Attendance Program")
    print("Enter a command to start the program.")
    print("compile: Create a Master CSV file based of files within the folder.")
    print("encrypt: generate an encrypted master csv file.")
    print("search: search a specific student's chapel records by student ID.")
    print("exit: shuts down the program.\n\n")
    x = input()
    
    if( x == "encrypt"):
        key = Fernet.generate_key()
  
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        with open('master.csv', 'rb') as file:
            original = file.read()    
        encrypted = fernet.encrypt(original)
        with open('CpytMaster.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print("Created encrypted file CpytMaster.csv")
        print("Encryption key stored at keyfile.key\n\n")
            
    if( x == "compile" ):
        con.to_csv('Master.csv')
        print("Created a master file at Master.csv")
        
    if (x == "search"):
        totalcount = 0
        guestcount = 0
        nooncount = 0
        sturecitalcount = 0
        faccount=0
        stdenscount = 0
        outsidecount = 0
        namealready = 0
        id = input("Enter a student's id number.\n")
        searchfile = open('master.csv', 'r')
        reader = csv.reader(searchfile, delimiter = ',')
        
        for row in reader:
            if id in row[3]:
                if(namealready==0):
                    print(row[1],row[2],row[3])
                    namealready +=1      
                print (row[6])
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
        
        
    if (x == 'exit'):
        active = False