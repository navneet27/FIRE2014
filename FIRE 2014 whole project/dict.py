import re, pickle

with open ("hinen.txt") as myfile:
	data=myfile.read().replace('\t', ' ')
d=re.sub(r'\n', r' ', data)
d=d.split()
i = iter(d)
b = dict(zip(i, i))
#print (b)
#dic = open('hineng.pkl', 'wb')
#pickle.dump(b, dic)
#dic.close()
