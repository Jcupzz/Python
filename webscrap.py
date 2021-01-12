# This is a program that takes url from csv file using pandas library of python and opens that url in 
# new tab of default web browser of the OS. It is made to do the web development challenge submission
# evaluation easier.
import time
import pandas as pd;
import webbrowser
collist = ['Live link of the project hosted ']
df = pd.read_csv("C:\Jcupzz255\py\webresponse.csv",usecols=collist,skipinitialspace=True) # set path of your csv 
listy = str(df)
new = []
for i in range(len(df)):
    new.append(str(df.values[i]))
for j in range(len(df)):
    newer = new[j][1:-1]
    webbrowser.open_new_tab(newer[1:-1])
    time.sleep(120) # change time delay here
