fo = open("E:\input.txt")
lines = fo.readlines()
fo.close()
res = 0
for l in lines:
    sides = sorted(list(map(int, l.replace("\n", "").split(" "))))
    if (sides[0]+sides[1]) > sides[2]:
        res += 1
print(res)

