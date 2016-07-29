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

bi = ['so', 'in', 'me', 'to', 'us', 'par']

for i in range(0, len(w)):
    h=0
    for j in range(0, len(w[i])):
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
#        elif w[i][j].lower() in do[w[i][j][0]]:
#            print (w[i][j] + '/O', end=" ")
        elif low in bi:
            if h==0:
                print (w[i][j] + '\E', end=" ")
            else:
                if lowf in dtc and low in dtc[lowf]:
                    print (w[i][j] + '\H=' + dtc[lowf][low], end=" ")
                elif lowf in dtc and low in dtc['exb']:
                    print (w[i][j] + '\H=' + dtc['exb'][low], end=" ")
                elif lowf in dtc and low in dtc['exj']:
                    print (w[i][j] + '\H=' + dtc['exj'][low], end=" ")
                else:
                    print (w[i][j] + '\H=', end=" ")
        elif low in dh[lowf]:
            if lowf in dtc and low in dtc[lowf]:
                print (w[i][j] + '\H=' + dtc[lowf][low], end=" ")
            elif lowf in dtc and low in dtc['exb']:
                print (w[i][j] + '\H=' + dtc['exb'][low], end=" ")
            elif lowf in dtc and low in dtc['exj']:
                print (w[i][j] + '\H=' + dtc['exj'][low], end=" ")
            else:
                print (w[i][j] + '\H=', end=" ")
            h=1
        elif low in de[lowf]:
            print (w[i][j] + '\E', end=" ")
            h=0
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
                    print (w[i][j] + '\H=' + dtc[lowf][low], end=" ")
                elif lowf in dtc and low in dtc['exb']:
                    print (w[i][j] + '\H=' + dtc['exb'][low], end=" ")
                elif lowf in dtc and low in dtc['exj']:
                    print (w[i][j] + '\H=' + dtc['exj'][low], end=" ")
                else:
                    print (w[i][j] + '\H=', end=" ")
            else:
                print (w[i][j] + '\E', end=" ")
    print()