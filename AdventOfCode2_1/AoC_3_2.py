fo = open("E:\input.txt")
lines = fo.readlines()
fo.close()
res = 0
for c in range(3):
    for r in range(0,len(lines)-2,3):
        sides = []
        sides.append(int(lines[r].split(" ")[c]))
        sides.append(int(lines[r+1].split(" ")[c]))
        sides.append(int(lines[r+2].split(" ")[c]))
        sides.sort()
        if (sides[0]+sides[1]) > sides[2]:
            res += 1
print(res)
