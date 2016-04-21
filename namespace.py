
a = 0
n = int(input())

def add(namespace,parent):
    stess
    print(namespace,parent)

def create(namespace,var):
    print(namespace,var)

def get(namespace,var):
    if var in namespace:
        print(namespace)
    print(namespace,var)

while n > 0:
    c, m, v = input().split()
    n=n-1
    if c == "add":
        add(m,v)
    if c == "create":
        create(m,v)
    if c == "get:
        get(m,v)
