f1=open('dev.txt', 'r')
f2=open('teng.txt', 'w')
f3=open('thin.txt', 'w')
f4=open('toth.txt', 'w')
f5=open('tname.txt', 'w')

data = f1.read()

eng = []
hin = []
oth = []
name = []

w = [x.split(" ") for x in data.split('\n')]

for i in range(0, len(w)-1):
    for x in range(0, len(w[i])-1):
        if w[i][x][len(w[i][x])-1] == "E":
            eng.append(w[i][x])
        elif w[i][x][len(w[i][x])-1] == "H":
            hin.append(w[i][x])
        elif w[i][x][len(w[i][x])-1] == "O":
            oth.append(w[i][x])
        else:
            name.append(w[i][x])
#set(eng)
#set(hin)
#set(oth)
#set(name)

for i in eng:
    i.replace("\E", "")
    f2.write("%s\n" % i)
for i in hin:
    f3.write("%s\n" % i)
for i in oth:
    f4.write("%s\n" % i)
for i in name:
    f5.write("%s\n" % i)

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
