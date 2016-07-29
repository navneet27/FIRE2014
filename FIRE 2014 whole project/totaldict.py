f2=open("adic.txt")
f3=open("bdic.txt")
f4=open("cdic.txt")
f5=open("ddic.txt")
f6=open("edic.txt")
f7=open("fdic.txt")
f8=open("gdic.txt")
f9=open("hdic.txt")
f10=open("idic.txt")
f11=open("jdic.txt")
f12=open("kdic.txt")
f13=open("ldic.txt")
f14=open("mdic.txt")
f15=open("ndic.txt")
f16=open("odic.txt")
f17=open("pdic.txt")
f18=open("qdic.txt")
f19=open("rdic.txt")
f20=open("sdic.txt")
f21=open("tdic.txt")
f22=open("udic.txt")
f23=open("vdic.txt")
f24=open("wdic.txt")
f25=open("xdic.txt")
f26=open("ydic.txt")
f27=open("zdic.txt")
f28=open("extrab.txt")
f29=open("extraj.txt")

#with open("adic.txt") as f2, open("bdic.txt") as f3, open("cdic.txt") as f4, open("ddic.txt") as f5, open("edic.txt") as f6, open("fdic.txt") as f7, open("gdic.txt") as f8, open("hdic.txt") as f9, open("idic.txt") as f10, open("jdic.txt") as f11, open("kdic.txt") as f12, open("ldic.txt") as f13, open("mdic.txt") as f14, open("ndic.txt") as f15, open("odic.txt") as f16, open("pdic.txt") as f17, open("qdic.txt") as f18, open("rdic.txt") as f19, open("sdic.txt") as f20, open("tdic.txt") as f21, open("udic.txt") as f22, open("vdic.txt") as f23, open("wdic.txt") as f24, open("xdic.txt") as f25, open("ydic.txt") as f26, open("zdic.txt") as f27:
d1=f2.read().replace('[', '')
d2=f3.read().replace('[', '')
d3=f4.read().replace('[', '')
d4=f5.read().replace('[', '')
d5=f6.read().replace('[', '')
d6=f7.read().replace('[', '')
d7=f8.read().replace('[', '')
d8=f9.read().replace('[', '')
d9=f10.read().replace('[', '')
d10=f11.read().replace('[', '')
d11=f12.read().replace('[', '')
d12=f13.read().replace('[', '')
d13=f14.read().replace('[', '')
d14=f15.read().replace('[', '')
d15=f16.read().replace('[', '')
d16=f17.read().replace('[', '')
d17=f18.read().replace('[', '')
d18=f19.read().replace('[', '')
d19=f20.read().replace('[', '')
d20=f21.read().replace('[', '')
d21=f22.read().replace('[', '')
d22=f23.read().replace('[', '')
d23=f24.read().replace('[', '')
d24=f25.read().replace('[', '')
d25=f26.read().replace('[', '')
d26=f27.read().replace('[', '')
d27=f28.read().replace('[', '')
d28=f29.read().replace('[', '')
d1=d1.replace(']', '')
d2=d2.replace(']', '')
d3=d3.replace(']', '')
d4=d4.replace(']', '')
d5=d5.replace(']', '')
d6=d6.replace(']', '')
d7=d7.replace(']', '')
d8=d8.replace(']', '')
d9=d9.replace(']', '')
d10=d10.replace(']', '')
d11=d11.replace(']', '')
d12=d12.replace(']', '')
d13=d13.replace(']', '')
d14=d14.replace(']', '')
d15=d15.replace(']', '')
d16=d16.replace(']', '')
d17=d17.replace(']', '')
d18=d18.replace(']', '')
d19=d19.replace(']', '')
d20=d20.replace(']', '')
d21=d21.replace(']', '')
d22=d22.replace(']', '')
d23=d23.replace(']', '')
d24=d24.replace(']', '')
d25=d25.replace(']', '')
d26=d26.replace(']', '')
d27=d27.replace(']', '')
d28=d28.replace(']', '')
d1=d1.replace('\'', '')
d2=d2.replace('\'', '')
d3=d3.replace('\'', '')
d4=d4.replace('\'', '')
d5=d5.replace('\'', '')
d6=d6.replace('\'', '')
d7=d7.replace('\'', '')
d8=d8.replace('\'', '')
d9=d9.replace('\'', '')
d10=d10.replace('\'', '')
d11=d11.replace('\'', '')
d12=d12.replace('\'', '')
d13=d13.replace('\'', '')
d14=d14.replace('\'', '')
d15=d15.replace('\'', '')
d16=d16.replace('\'', '')
d17=d17.replace('\'', '')
d18=d18.replace('\'', '')
d19=d19.replace('\'', '')
d20=d20.replace('\'', '')
d21=d21.replace('\'', '')
d22=d22.replace('\'', '')
d23=d23.replace('\'', '')
d24=d24.replace('\'', '')
d25=d25.replace('\'', '')
d26=d26.replace('\'', '')
d27=d27.replace('\'', '')
d28=d28.replace('\'', '')
d1=d1.replace(',', '')
d2=d2.replace(',', '')
d3=d3.replace(',', '')
d4=d4.replace(',', '')
d5=d5.replace(',', '')
d6=d6.replace(',', '')
d7=d7.replace(',', '')
d8=d8.replace(',', '')
d9=d9.replace(',', '')
d10=d10.replace(',', '')
d11=d11.replace(',', '')
d12=d12.replace(',', '')
d13=d13.replace(',', '')
d14=d14.replace(',', '')
d15=d15.replace(',', '')
d16=d16.replace(',', '')
d17=d17.replace(',', '')
d18=d18.replace(',', '')
d19=d19.replace(',', '')
d20=d20.replace(',', '')
d21=d21.replace(',', '')
d22=d22.replace(',', '')
d23=d23.replace(',', '')
d24=d24.replace(',', '')
d25=d25.replace(',', '')
d26=d26.replace(',', '')
d27=d27.replace(',', '')
d28=d28.replace(',', '')

w1 = sorted([x.split() for x in d1.split('\n')])
w2 = sorted([x.split() for x in d2.split('\n')])
w3 = sorted([x.split() for x in d3.split('\n')])
w4 = sorted([x.split() for x in d4.split('\n')])
w5 = sorted([x.split() for x in d5.split('\n')])
w6 = sorted([x.split() for x in d6.split('\n')])
w7 = sorted([x.split() for x in d7.split('\n')])
w8 = sorted([x.split() for x in d8.split('\n')])
w9 = sorted([x.split() for x in d9.split('\n')])
w10 = sorted([x.split() for x in d10.split('\n')])
w11 = sorted([x.split() for x in d11.split('\n')])
w12 = sorted([x.split() for x in d12.split('\n')])
w13 = sorted([x.split() for x in d13.split('\n')])
w14 = sorted([x.split() for x in d14.split('\n')])
w15 = sorted([x.split() for x in d15.split('\n')])
w16 = sorted([x.split() for x in d16.split('\n')])
w17 = sorted([x.split() for x in d17.split('\n')])
w18 = sorted([x.split() for x in d18.split('\n')])
w19 = sorted([x.split() for x in d19.split('\n')])
w20 = sorted([x.split() for x in d20.split('\n')])
w21 = sorted([x.split() for x in d21.split('\n')])
w22 = sorted([x.split() for x in d22.split('\n')])
w23 = sorted([x.split() for x in d23.split('\n')])
w24 = sorted([x.split() for x in d24.split('\n')])
w25 = sorted([x.split() for x in d25.split('\n')])
w26 = sorted([x.split() for x in d26.split('\n')])
w27 = sorted([x.split() for x in d27.split('\n')])
w28 = sorted([x.split() for x in d28.split('\n')])


dtc = {}
a = {}
b = {}
c = {}
d = {}
e = {}
f = {}
g = {}
h = {}
i = {}
j = {}
k = {}
l = {}
m = {}
n = {}
o = {}
p = {}
q = {}
r = {}
s = {}
t = {}
u = {}
v = {}
w = {}
x = {}
y = {}
z = {}
exb = {}
exj = {}

for ii in range (1, len(w1)-1):
    a[w1[ii][0]] = w1[ii][1]
for ii in range (1, len(w2)-1):
    b[w2[ii][0]] = w2[ii][1]
for ii in range (1, len(w3)-1):
    c[w3[ii][0]] = w3[ii][1]
for ii in range (1, len(w4)-1):
    d[w4[ii][0]] = w4[ii][1]
for ii in range (1, len(w5)-1):
    e[w5[ii][0]] = w5[ii][1]
for ii in range (1, len(w6)-1):
    f[w6[ii][0]] = w6[ii][1]
for ii in range (1, len(w7)-1):
    g[w7[ii][0]] = w7[ii][1]
for ii in range (1, len(w8)-1):
    h[w8[ii][0]] = w8[ii][1]
for ii in range (1, len(w9)-1):
    i[w9[ii][0]] = w9[ii][1]
for ii in range (1, len(w10)-1):
    j[w10[ii][0]] = w10[ii][1]
for ii in range (1, len(w11)-1):
    k[w11[ii][0]] = w11[ii][1]
for ii in range (1, len(w12)-1):
    l[w12[ii][0]] = w12[ii][1]
for ii in range (1, len(w13)-1):
    m[w13[ii][0]] = w13[ii][1]
for ii in range (1, len(w14)-1):
    n[w14[ii][0]] = w14[ii][1]
for ii in range (1, len(w15)-1):
    o[w15[ii][0]] = w15[ii][1]
for ii in range (1, len(w16)-1):
    p[w16[ii][0]] = w16[ii][1]
for ii in range (1, len(w17)-1):
    q[w17[ii][0]] = w17[ii][1]
for ii in range (1, len(w18)-1):
    r[w18[ii][0]] = w18[ii][1]
for ii in range (1, len(w19)-1):
    s[w19[ii][0]] = w19[ii][1]
for ii in range (1, len(w20)-1):
    t[w20[ii][0]] = w20[ii][1]
for ii in range (1, len(w21)-1):
    u[w21[ii][0]] = w21[ii][1]
for ii in range (1, len(w22)-1):
    v[w22[ii][0]] = w22[ii][1]
for ii in range (1, len(w23)-1):
    w[w23[ii][0]] = w23[ii][1]
for ii in range (1, len(w24)-1):
    x[w24[ii][0]] = w24[ii][1]
for ii in range (1, len(w25)-1):
    y[w25[ii][0]] = w25[ii][1]
for ii in range (1, len(w26)-1):
    z[w26[ii][0]] = w26[ii][1]
for ii in range (1, len(w27)-1):
    exb[w27[ii][0]] = w27[ii][1]
for ii in range (1, len(w28)-1):
    exj[w28[ii][0]] = w28[ii][1]

dtc["a"]=a
dtc["b"]=b
dtc["c"]=c
dtc["d"]=d
dtc["e"]=e
dtc["f"]=f
dtc["g"]=g
dtc["h"]=h
dtc["i"]=i
dtc["j"]=j
dtc["k"]=k
dtc["l"]=l
dtc["m"]=m
dtc["n"]=n
dtc["o"]=o
dtc["p"]=p
dtc["q"]=q
dtc["r"]=r
dtc["s"]=s
dtc["t"]=t
dtc["u"]=u
dtc["v"]=v
dtc["w"]=w
dtc["x"]=x
dtc["y"]=y
dtc["z"]=z
dtc["exb"]=exb
dtc["exj"]=exj
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
f28.close()
f29.close()
