# a=input("rownanie\n")
a="15*(1+2)=0"
z=0
en=0
ch=[]
for i in a:
    if i=="(" and en==0: 
        z+=1
    if i==")" and en==0: 
        z-=1
    if i=="=": en=1

if z==0 and en==1: print("prawidłowe działanie")
else: print("błąd")


