print("Hello,  %s" % "world")

listA = ['a', 'b', 'c']
print(len(listA))
print(listA[-1])
listA.append('d')
listA.insert(1, 'e')
listA.pop()
listA.pop(1)
listA[1] = 'k'
print(listA)

# 请用索引取出下面list的指定元素：

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# Apple:
print(L[0][0])
# Python:
print(L[1][1])
# Lisa:
print(L[2][2])

tupleA = ()  # tuple可以是空集
tupleB = (1,)  # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
tupleC = ('a','b',['A','B'])
tupleC[2][0] = 'X'
tupleC[2][1] = 'Y'
print(tupleC)  # tuple中的list可变，尽管tuple内的元素不可变，但是tuple内list的元素可变。

#  Which are valid tuples in these options?
#  A. a = () B. b = (1) C. c = [2] D. d = (1,) E. e = (1,2,3)
#  The correct answers are A, D and E.
