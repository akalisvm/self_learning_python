def f(x):
    return x*x
r = map(f,[x for x in range(10)])
print(list(r))

r = map(str,[x for x in range(10)])
print(list(r))

def normalize(name):
    upper = name[:1].upper()
    lower = name[1:].lower()
    return upper + lower

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
