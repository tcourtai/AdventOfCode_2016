with open("E:\input.txt") as f:
    lines = f.readlines()
nb=0
for l in lines:
    res=''.join([item[0] for item in sorted({chr(c): l.split("[")[0].count(chr(c)) for c in range(ord('a'), ord('z')+1)}.items(), key=lambda x: (x[1], -1*ord(x[0])), reverse=True)[0:5]])
    if (res==l.split("[")[1][0:l.split("[")[1].index("]")]): nb+=[int(s) for s in l.replace("[","-").split("-") if s.isdigit()][0]
print(nb)

