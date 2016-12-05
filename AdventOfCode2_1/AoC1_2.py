
def check():
    global res
    pos=str(x)+":"+str(y)
    if pos in visited:
            if res=="":
                res=str(abs(x)+abs(y)) 
    else:
        visited.append(pos) 
        
    return

with open("D:\\tcourtai\\input1.txt") as f:
    content = f.readline()

res=""
dir="U"
x=0
y=0
visited=["0:0"]
for it in content.split(', '):
    mv=int(it[1:])
    if (it[0]=="L" and dir=="L") or (it[0]=="R" and dir=="R"):
        dir="D"
        for i in range(mv):
            y-=1
            check()

    elif (it[0]=="L" and dir=="R") or (it[0]=="R" and dir=="L"):
        dir="U"
        for i in range(mv):
            y+=1
            check()

    elif (it[0]=="L" and dir=="U") or  (it[0]=="R" and dir=="D"):
        dir="L"
        for i in range(mv):
            x-=1
            check()

    elif (it[0]=="L" and dir=="D") or ( it[0]=="R" and dir=="U"):
        dir="R"
        for i in range(mv):
            x+=1
            check()
print(res)

