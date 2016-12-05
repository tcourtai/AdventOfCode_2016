import hashlib
res=""
i=0
s="abbhdwsy"
while len(res)<8:
    h=hashlib.md5(str(s+str(i)).encode('utf-8')).hexdigest()
    if h[0:5]== "00000":
        res+=h[5]
    i+=1
print(res)