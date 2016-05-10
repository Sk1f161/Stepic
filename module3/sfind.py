# put your python code here
s = input()
a = input()
b = input()

i =0

while(a in s):
    if a in b:
        print("Impossible")
        break
    if i>50 :
        break
    else:
        s = s.replace(a,b)
        i = i + 1

else:
    print(i)
