with open("D:\\tcourtai\\input.txt") as f:
    content = f.readlines()
x=1
y=1
keypad=[7,8,9,4,5,6,1,2,3]
for l in content:
    for i in range(len(l)):
        if l[i]=="U" and y<2:
           y+=1
        elif l[i]=="D" and y>0:
           y-=1
        elif l[i]=="L" and x>0:
           x-=1
        elif l[i]=="R" and x<2:
           x+=1
    print(keypad[x+y*3])         
         
