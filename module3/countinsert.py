s = input()
t = input()

dlin = len(t)
dlins = len(s)
pos = 0
count = 0

while s.find(t,pos) != -1:
    pos = s.find(t,pos)+1
    count += 1
    #print(i)

print("Count: ", count)

