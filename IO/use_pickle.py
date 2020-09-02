import pickle
d = dict(name='Bob', age=20, score=99)
p = pickle.dumps(d)
print(p)

f = open('pickle_test.txt', 'wb')
pickle.dump(d,f)
f.close()

f = open('pickle_test.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

