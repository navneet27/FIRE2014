import re
with open("2013.txt", "r") as f:
    d=f.read()
w = [x.split() for x in d.split('\n')]
a=[]
hh=0
he=0
eh=0
ee=0
th=0
te=0
for i in range(0, len(w)):
	for j in range(0, len(w[i])):
		a.append(w[i][j])

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
print ("HH= ", hh, " HE= ", he, " EH= ", eh, " EE= ", ee, " TH=", th, " TE=", te)
