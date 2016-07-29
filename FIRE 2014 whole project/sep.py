f1=open("hinenf.txt", "r")
f2=open("adic.txt", "w")
f3=open("bdic.txt", "w")
f4=open("cdic.txt", "w")
f5=open("ddic.txt", "w")
f6=open("edic.txt", "w")
f7=open("fdic.txt", "w")
f8=open("gdic.txt", "w")
f9=open("hdic.txt", "w")
f10=open("idic.txt", "w")
f11=open("jdic.txt", "w")
f12=open("kdic.txt", "w")
f13=open("ldic.txt", "w")
f14=open("mdic.txt", "w")
f15=open("ndic.txt", "w")
f16=open("odic.txt", "w")
f17=open("pdic.txt", "w")
f18=open("qdic.txt", "w")
f19=open("rdic.txt", "w")
f20=open("sdic.txt", "w")
f21=open("tdic.txt", "w")
f22=open("udic.txt", "w")
f23=open("vdic.txt", "w")
f24=open("wdic.txt", "w")
f25=open("xdic.txt", "w")
f26=open("ydic.txt", "w")
f27=open("zdic.txt", "w")


#with open("hinen.txt", "r") as f1, open("adic.txt", "w") as f2, open("bdic.txt", "w") as f3, open("cdic.txt", "w") as f4, open("ddic.txt", "w") as f5, open("edic.txt", "w") as f6, open("fdic.txt", "w") as f7, open("gdic.txt", "w") as f8, open("hdic.txt", "w") as f9, open("idic.txt", "w") as f10, open("jdic.txt", "w") as f11, open("kdic.txt", "w") as f12, open("ldic.txt", "w") as f13, open("mdic.txt", "w") as f14, open("ndic.txt", "w") as f15, open("odic.txt", "w") as f16, open("pdic.txt", "w") as f17, open("qdic.txt", "w") as f18, open("rdic.txt", "w") as f19, open("sdic.txt", "w") as f20, open("tdic.txt", "w") as f21, open("udic.txt", "w") as f22, open("vdic.txt", "w") as f23, open("wdic.txt", "w") as f24, open("xdic.txt", "w") as f25, open("ydic.txt", "w") as f26, open("zdic.txt", "w") as f27:
l=f1.read()
na = []
nb = []
nc = []
nd = []
ne = []
nf = []
ng = []
nh = []
ni = []
nj = []
nk = []
nl = []
nm = []
nn = []
no = []
np = []
nq = []
nr = []
ns = []
nt = []
nu = []
nv = []
nw = []
nx = []
ny = []
nz = []
w = [x.split() for x in l.split('\n')] #split every line
for i in range(1, len(w)-1):
    if w[i][0][0] == 'a':
        na.append(w[i])	#save into list
    elif w[i][0][0] == 'b':
        nb.append(w[i])
    elif w[i][0][0] == 'c':
        nc.append(w[i])
    elif w[i][0][0] == 'd':
        nd.append(w[i])
    elif w[i][0][0] == 'e':
    	ne.append(w[i])
    elif w[i][0][0] == 'f':
    	nf.append(w[i])
    elif w[i][0][0] == 'g':
        ng.append(w[i])
    elif w[i][0][0] == 'h':
        nh.append(w[i])
    elif w[i][0][0] == 'i':
        ni.append(w[i])
    elif w[i][0][0] == 'j':
        nj.append(w[i])
    elif w[i][0][0] == 'k':
        nk.append(w[i])
    elif w[i][0][0] == 'l':
        nl.append(w[i])
    elif w[i][0][0] == 'm':
        nm.append(w[i])
    elif w[i][0][0] == 'n':
    	nn.append(w[i])
    elif w[i][0][0] == 'o':
        no.append(w[i])
    elif w[i][0][0] == 'p':
        np.append(w[i])
    elif w[i][0][0] == 'q':
        nq.append(w[i])
    elif w[i][0][0] == 'r':
        nr.append(w[i])
    elif w[i][0][0] == 's':
        ns.append(w[i])
    elif w[i][0][0] == 't':
        nt.append(w[i])
    elif w[i][0][0] == 'u':
        nu.append(w[i])
    elif w[i][0][0] == 'v':
        nv.append(w[i])
    elif w[i][0][0] == 'w':
        nw.append(w[i])
    elif w[i][0][0] == 'x':
        nx.append(w[i])
    elif w[i][0][0] == 'y':
        ny.append(w[i])
    elif w[i][0][0] == 'z':
        nz.append(w[i])
    else:
            continue
for i in na:
    f2.write("%s\n" % i)
for i in nb:
    f3.write("%s\n" % i)
for i in nc:
    f4.write("%s\n" % i)
for i in nd:
    f5.write("%s\n" % i)
for i in ne:
    f6.write("%s\n" % i)
for i in nf:
    f7.write("%s\n" % i)
for i in ng:
    f8.write("%s\n" % i)
for i in nh:
    f9.write("%s\n" % i)
for i in ni:
    f10.write("%s\n" % i)
for i in nj:
    f11.write("%s\n" % i)
for i in nk:
    f12.write("%s\n" % i)
for i in nl:
    f13.write("%s\n" % i)
for i in nm:
    f14.write("%s\n" % i)
for i in nn:
    f15.write("%s\n" % i)
for i in no:
    f16.write("%s\n" % i)
for i in np:
    f17.write("%s\n" % i)
for i in nq:
    f18.write("%s\n" % i)
for i in nr:
    f19.write("%s\n" % i)
for i in ns:
    f20.write("%s\n" % i)
for i in nt:
    f21.write("%s\n" % i)
for i in nu:
    f22.write("%s\n" % i)
for i in nv:
    f23.write("%s\n" % i)
for i in nw:
    f24.write("%s\n" % i)
for i in nx:
    f25.write("%s\n" % i)
for i in ny:
    f26.write("%s\n" % i)
for i in nz:
    f27.write("%s\n" % i)
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
f9.close()
f10.close()
f11.close()
f12.close()
f13.close()
f14.close()
f15.close()
f16.close()
f17.close()
f18.close()
f19.close()
f20.close()
f21.close()
f22.close()
f23.close()
f24.close()
f25.close()
f26.close()
f27.close()
