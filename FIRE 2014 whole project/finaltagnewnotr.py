from totaldict import dtc
from collections import defaultdict
import re

with open("test2.txt", "r") as f1:
    d1=f1.read()
#    d1.lower()
with open("thinf.txt", "r") as f2:
    d2=f2.read()
#    d2.lower()
with open("tengf.txt", "r") as f3:
    d3=f3.read()
#    d3.lower()
with open("tnamef.txt", "r") as f4:
    d4=f4.read()
#    d4.lower()
#with open("tothf.txt", "r") as f5:
#    d5=f5.read()
#    d5.lower()
with open("indianplaces.txt", "r") as f6:
    d6=f6.read()
#    d6.lower()
with open("allnames.txt", "r") as f7:
    d7=f7.read()
#    d7.lower()
    
w = [x.split() for x in d1.split('\n')]
wh = sorted([x.split(' ') for x in d2.split('\n')])
we = sorted([x.split(' ') for x in d3.split('\n')])
wn = sorted([x.split(' ') for x in d4.split('\n')])
#wo = sorted([x.split(' ') for x in d5.split('\n')])
wip = sorted([x.split(' ') for x in d6.split('\n')])
wan = sorted([x.split(' ') for x in d7.split('\n')])

dh = defaultdict(list)
de = defaultdict(list)
dn = defaultdict(list)
#do = defaultdict(list)
dip = defaultdict(list)
dan = defaultdict(list)

for x1 in range(2, len(wh)):
    dh[wh[x1][0][0]].append(wh[x1][0])
for x2 in range(1, len(we)):
    de[we[x2][0][0]].append(we[x2][0])
for x3 in range(1, len(wn)):
    dn[wn[x3][0][0]].append(wn[x3][0])
#for x4 in range(1, len(wo)):
#    do[wo[x4][0][0]].append(wo[x4][0])
for x5 in range(1, len(wip)):
    dip[wip[x5][0][0]].append(wip[x5][0])
for x6 in range(1, len(wan)):
    dan[wan[x6][0][0]].append(wan[x6][0])

bi = ['so', 'in', 'me', 'to', 'us', 'par', 'do']

with open("2013.txt", "r") as f:
    d=f.read()
p = [x.split() for x in d.split('\n')]
a=[]
hh=0
he=0
eh=0
ee=0
th=0
te=0
for i in range(0, len(p)):
    for j in range(0, len(p[i])):
        a.append(p[i][j])

for i in range(0, len(a)-1):
    if re.match(r'...+[\H]...*', a[i]):
        if re.match(r'...+[\H]...*', a[i+1]):
            hh +=1
        if re.match(r'...+[\E]', a[i+1]):
            he +=1
        th +=1
    if re.match(r'...+[\E]', a[i]):
        if re.match(r'...+[\H]...*', a[i+1]):
            eh +=1
        if re.match(r'...+[\E]', a[i+1]):
            ee +=1
        te +=1
phh = hh/th    #probability of hindi followed by hindi
phe = he/te
peh = eh/th
pee = ee/te

lang = {} #to keep tag of which language was it previously

for i in range(0, len(w)):
    if te > th:
        prevh=0     #default english
    else:
        prevh=1     #default hindi
    for j in range(0, len(w[i])):
        h = prevh
        if prevh == 0:
            if phh >= 0.5:
                h = 1
            else:
                h = 0
        else:
            if pee >= 0.5:
                h = 0
            else:
                h = 1
        low=w[i][j].lower()
        lowf=low[0]
        if re.match(r'[\.\=\:\;\,\#\@\(\)\`\~\$\*\!\?\'\"\+\-\\\/\|\{\}\[\]\_\<\>]+', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif re.match(r'[0-9]+', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif re.match(r'[a-zA-Z]+[\@]+[a-zA-Z\.]*', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif re.match(r'[a-zA-Z]+[\']+[a-z]*', w[i][j]):
            print (w[i][j] + '\E', end=" ")
        elif re.match(r'[A-Za-z]+[\-]+[a-z]*', w[i][j]):
            print (w[i][j] + '\E', end=" ")
        elif re.match(r'[A-Za-z]+[\+\-]+', w[i][j]):
            print (w[i][j] + '\E', end=" ")
        elif re.match(r'http+', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif re.match(r'www.[A-Za-z0-9]+.com', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif re.match(r'[A-Za-z0-9]+.com', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif re.match(r'[a-zA-Z]+-[a-zA-Z]*', w[i][j]):
            print (w[i][j] + '\O', end=" ")
        elif low in bi:     # Bilingual words
            if h==0:
                print (w[i][j] + '\E', end=" ")
            else:
                if lowf in dtc and low in dtc[lowf]:
                    print (w[i][j] + '\H', end=" ")
                elif lowf in dtc and low in dtc['exb']:
                    print (w[i][j] + '\H', end=" ")
                elif lowf in dtc and low in dtc['exj']:
                    print (w[i][j] + '\H', end=" ")
                else:
                    print (w[i][j] + '\H', end=" ")
        elif low in dh[lowf]:
            if lowf in dtc and low in dtc[lowf]:
                print (w[i][j] + '\H', end=" ")
            elif lowf in dtc and low in dtc['exb']:
                print (w[i][j] + '\H', end=" ")
            elif lowf in dtc and low in dtc['exj']:
                print (w[i][j] + '\H', end=" ")
            else:
                print (w[i][j] + '\H', end=" ")
            prevh=1
        elif low in de[lowf]:
            print (w[i][j] + '\E', end=" ")
            prevh=0
        elif low in dn[lowf]:
            if low in dip[lowf]:
                print ('[' + w[i][j] + ']' + 'L', end=" ")
            elif low in dan[lowf]:
                print ('[' + w[i][j] + ']' + 'P', end=" ")
            elif len(w[i][j]) <= 4 or w[i][j].isupper():
                print ('[' + w[i][j] + ']' + 'A', end=" ")
            else:
                print ('[' + w[i][j] + ']' + 'O', end=" ")
        elif low in dan[lowf]:
            print ('[' + w[i][j] + ']' + 'P', end=" ")
        elif low in dip[lowf]:
            print ('[' + w[i][j] + ']' + 'L', end=" ")
        elif w[i][j].isupper():
            print ('[' + w[i][j] + ']' + 'A', end=" ")
        else:
            if h==1:
                if lowf in dtc and low in dtc[lowf]:
                    print (w[i][j] + '\H', end=" ")
                elif lowf in dtc and low in dtc['exb']:
                    print (w[i][j] + '\H', end=" ")
                elif lowf in dtc and low in dtc['exj']:
                    print (w[i][j] + '\H', end=" ")
                else:
                    print (w[i][j] + '\H', end=" ")
            else:
                print (w[i][j] + '\E', end=" ")
    print()