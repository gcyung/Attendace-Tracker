# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:55:19 2021

@author: james
"""

from cryptography.fernet import Fernet
import csv
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

#Creating the frame
window = tk.Tk()
frame = tk.Frame(master=window,borderwidth=10)
greeting = tk.Label(text="Concert Attendance Program")

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
        
     for row in reader:
         if id in row[3]:
            if(namealready==0):
                 print(row[1],row[2],row[3])
                 name_mes = row[3]
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
    
    
     with open('CpytMaster.csv', 'rb') as file:
            original = file.read()    
            encrypted = fernet.encrypt(original)
     with open('CpytMaster.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
           
search_button = tk.Button(
    text="Search",
    width = 40,
    height = 10,
    bg="white",
    fg="black",
    borderwidth = 5,
    command = lambda:handle_search_click()
)

greeting.pack()
search_button.pack()
frame.pack()
window.mainloop()