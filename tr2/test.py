import pandas as pd

#-*------------prpr -----------------
l=int(input("donne le number of line : "))
while l<0 : 
    l=int(input("donne le number of line : "))
c=int(input("donne le number of column : "))
while c<0 : 
    c=int(input("donne le number of column : "))

df=pd.DataFrame()
index=[]

#*------------remplissage index -----------------

for i in range(l):
    index.append(input("donne le nom de la ligne {} : ".format(i+1)))
#*------------remplissage tableau -----------------
for i in range(l):
    ch=input("donne le name of column : ")
    t=[]
    for j in range(c):
        t.append(input("donne le note de {} de etudel {} : ".format(df.index[i],ch)))
    df[ch]=t

print (df)

#-*------------affiche -----------------


