# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 16:38:10 2020

@author: Admin
"""

import smtplib
username=input("nhap username:")
password=input("nhap password:")
sendusername=input("nhap email nhan:")
n=int(input("nhap so lan gui n="))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
msg = input("nhap thong diep:")
i=1
while i<=n:
    server.sendmail(username ,sendusername, msg)
    i+=1
server.quit()

    


