from os import name
import pandas as pd
import numpy as np
import aseegg as ag
import matplotlib.pyplot as plt
import datetime as dt

moje_dane=pd.read_csv('moje_dane.txt', names = ['signal','time'])
moje_dane1=pd.read_csv('moje_dane1.txt', names = ['signal','time'])
data=pd.DataFrame()

#usunięcie startu
moje_dane = moje_dane[moje_dane.loc[moje_dane['signal'] == 'start'].index[0]+1:]
moje_dane1 = moje_dane1[moje_dane1.loc[moje_dane1['signal'] == 'start'].index[0]+1:]


minLen = min(len(moje_dane), len(moje_dane1))
moje_dane = moje_dane[:minLen]
moje_dane1 = moje_dane1[:minLen]

#średnia
data['sig'] = moje_dane['signal'].astype(float).values
data['sig1'] = moje_dane1['signal'].astype(float).values
data['signal'] = (data['sig'] + data['sig1']) / 2 
data.drop(['sig','sig1'],axis=1,inplace=True)

#zamiana na sekundy
tStart = dt.datetime.strptime(moje_dane.iat[0,1],'%H:%M:%S.%f')

ts = []

for i, row in moje_dane.iterrows(): #iterrowas = iterowanie po wierszach
    ts.append(str(dt.datetime.strptime(row['time'],'%H:%M:%S.%f')-tStart))

data['time'] = ts

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z']
blink = []
letterCol = []
letter = 0
for i in range(2,60,4):
    blink.append(i)
    blink.append(i+1)

letterFlag = False

#dodawanie kolumny z literami
for i, row in data.iterrows():
    if i != 0:
        s = int(dt.datetime.strftime(dt.datetime.strptime(row['time'],"%H:%M:%S.%f"),"%S"))
    if i == 0:
        data.drop(i, inplace=True)
    elif s not in blink:
        data.drop(i, inplace=True)
        if letterFlag == True:
            if letter == 23:
                letter = 0
            else:
                letter += 1
        letterFlag = False
    else:
        letterCol.append(letters[letter])
        letterFlag = True

        
data['letter'] = letterCol

data['signal']=ag.pasmowozaporowy(data['signal'], 200, 49, 51)
data['letter'] = letterCol
data['signal'] = ag.pasmowozaporowy(data['signal'], 200, 49, 51)
data['signal'] = ag.gornoprzepustowy(data['signal'], 200, 3)

list_blink=[]

for i, row in data.iterrows():
    if row['signal']<(-50000): 
        list_blink.append(row['letter'])
    else:
        continue

print((' '.join(map(str, list_blink))))
data.to_csv('dane.csv', encoding='utf-8')

