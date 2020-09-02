d = {'Micheal': 95, 'Bob': 75, 'Tracy': 85}
print(d['Micheal'])

d['Adam'] = 67
print(d['Adam'])

print('Thomas' in d)
print(d.get('Thomas', -1))

d.pop('Bob')
print(d)

s = {1, 2, 3}
s.add(4)
print(s)
s.remove(4)
print(s)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

t1 = (1, 2, 3)
t2 = (1, [2, 3])
d1 = {'a': t1, 'b': t2}
print(d1)
t2[1][0] = 1
d1['a'] = t2
print(d1)

s3 = set(t1)  # t1 is fine, whereas t2 is invalid for set
print(s3)
