with open('hinen.txt') as f:
    data=f.read().replace('\t', ' ')
words = [x.split() for x in data.split('\n')]
words = sorted(words)
d={}
for i in range (1, len(words)-1):
	d[words[i][0]] = words[i][1]
print (d)
