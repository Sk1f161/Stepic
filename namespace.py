
a = 0
n = int(input())

def add(namespace,parent):
    d[self.name].append(self.parent)
    print(namespace,parent)

def create(namespace,var):
    d[self.namespace] = [self.var]
    print(d)

def get(namespace,var):
    #if var in namespace:
    #    print(namespace)
    #print(namespace,var)
    if d[namespace][1] == var:
        return name
    elif d[namespace][0] != 'None':
        return get(d[name][0],var)
    else:
        return 'None'


d = {'global':['None']}
while n > 0:
    c, m, v = input().split()
    n=n-1
    if c == "add":
        add(m,v)
    if c == "create":
        create(m,v)
    if c == "get:
        get(m,v)

