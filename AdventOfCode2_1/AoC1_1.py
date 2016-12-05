with open("D:\\tcourtai\\input1.txt") as f:
    content = f.readline()

dir="U"
x=0
y=0
for it in content.split(', '):
    mv=int(it[1:])
    if it[0]=="L" and dir=="L":
        dir="D"
        y-=mv
    elif it[0]=="L" and dir=="R":
        dir="U"
        y+=mv
    elif it[0]=="L" and dir=="U":
        dir="L"
        x-=mv
    elif it[0]=="L" and dir=="D":
        dir="R"
        x+=mv
    elif it[0]=="R" and dir=="L":
        dir="U"
        y+=mv
    elif it[0]=="R" and dir=="R":
        dir="D"
        y-=mv
    elif it[0]=="R" and dir=="U":
        dir="R"
        x+=mv
    elif it[0]=="R" and dir=="D":
        dir="L"
        x-=mv
print(str(abs(x)+abs(y)))