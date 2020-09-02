from io import StringIO

f = StringIO()
f.write('hello')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!\n')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
