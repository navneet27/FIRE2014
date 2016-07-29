with open('test2.txt', 'r') as f:
    data = f.read()
g= open("trial.txt", 'a')
w = [x.split(";") for x in data.split('\n')]
n=[]
for i in range(0, len(w)-1, 2):
	for j in range(0, len(w[i])-2):
		n.append(w[i][j] + " " + w[i+1][j])
for i in n:
	g.write("%s\n" % i)
g.close()
