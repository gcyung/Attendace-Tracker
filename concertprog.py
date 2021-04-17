# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:58:45 2021

@author: james
"""

#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd
from glob import glob
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


#Reading in all of the files within the current folder with that start with a biola string.
filenames = glob('biola*.csv') 
dataframes = [pd.read_csv(f) for f in filenames]
con = pd.concat([pd.read_csv(fp).assign(Concert=os.path.basename(fp)) for fp in filenames])
con.sort_values(by=["StudentNumber"], inplace = True)


###Creating a UI###

#Creating the frame
window = tk.Tk()
frame = tk.Frame(master=window,borderwidth=10)
greeting = tk.Label(text="Concert Attendance Program")



#Creating the Buttons

def handle_compile_click():
    con.to_csv('Master.csv')
    messagebox.showinfo("Compile","Created a master file at Master.csv")
    
compile_button = tk.Button(
    text="Compile",
    width=40,
    height=10,
    bg="white",
    fg="black",
    borderwidth = 5,
    command = lambda:handle_compile_click()
)



def handle_search_click():
     totalcount = 0
     guestcount = 0
     nooncount = 0
     sturecitalcount = 0
     faccount=0
     stdenscount = 0
     outsidecount = 0
     namealready = 0
     valid = False
     while(valid == False):
         id = simpledialog.askstring("Search", "Type in the ID number that you want to search.", parent=window)
         if (len(id) != 7):
             messagebox.showerror("Error", "Invalid ID number, please try again.")
         else:
             valid = True
     searchfile = open('master.csv', 'r')
     reader = csv.reader(searchfile, delimiter = ',')
        
     for row in reader:
         if id in row[3]:
            if(namealready==0):
                 print(row[1],row[2],row[3])
                 name_mes = row[1] +" "+ row[2] +" "+  row[3]
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
                    
     ts = str(totalcount)
     gcs = str(guestcount)
     nc = str(nooncount)
     stcs = str(sturecitalcount)
     fcs = str(faccount)
     secs = str(stdenscount)
     opcs = str(outsidecount)
            
     mes_string = ("Total Concerts Attended: " + ts +"\n"
                          + "Guest Artist Concerts Attended: " + gcs +"\n"
                          +"Music at Noon Concerts Attended: " + nc +"\n"
                          +"Student Recital Concerts Attended: " + stcs +"\n"
                          +"Faculty Recital Concerts Attended: "+ fcs +"\n"
                          +"Student Ensemble Concerts Attended: " + secs +"\n"
                          +"Outside Professional Concerts Attended: " + opcs +"\n"
                          )
            
     messagebox.showinfo(name_mes,mes_string)
     print(mes_string)
            
           
search_button = tk.Button(
    text="Search",
    width = 40,
    height = 10,
    bg="white",
    fg="black",
    borderwidth = 5,
    command = lambda:handle_search_click()
)


def handle_encrypt_click():
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
        messagebox.showinfo("Encrypt","Created an encrypted file at CyptMaster.csv and a key at keyfile.key")

encrypt_button = tk.Button(
    text="Encrypt",
    width = 40,
    height = 10,
    bg="white",
    fg="black",
    borderwidth = 5,
    command = lambda:handle_encrypt_click()
)





#Packing the UI elements
greeting.pack()
compile_button.pack()
search_button.pack()
encrypt_button.pack()
frame.pack()








#calling the program's main loop
window.mainloop()



