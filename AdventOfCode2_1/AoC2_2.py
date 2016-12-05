with open("D:\\tcourtai\\input.txt") as f:
    content = f.readlines()
x=0
y=2
keypad=[0,0,"D",0,0,0,"A","B","C",0,5,6,7,8,9,0,2,3,4,0,0,0,1,0,0]
for l in content:
    for i in range(len(l)):
        if l[i]=="U" and y<4 and keypad[x+(y+1)*5]!=0:
           y+=1
        elif l[i]=="D" and y>0 and keypad[x+(y-1)*5]!=0:
           y-=1
        elif l[i]=="L" and x>0 and keypad[(x-1)+y*5]!=0:
           x-=1
        elif l[i]=="R" and x<4 and keypad[(x+1)+y*5]!=0:
           x+=1
    print(keypad[x+y*5])         
         
