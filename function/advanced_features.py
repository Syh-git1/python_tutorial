# coding=utf-8


# -----------------------切片-------------------------#
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取list数据笨方法
print([L[0], L[1], L[2]])
# 扩展使用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 切片取值  省略前部表示从0开始 省略后部表示取到最后
print(L[0:3])
print(L[:3])
print(L[3:])

# 支持倒数切片 -1表示倒数第一个数的索引
print(L[-2:])

# 建立新列表
L = list(range(100))
print(L)
# 取前10个数 每隔两个取一个
print(L[:10:2])
# 复制一个list
R = L
print(R)
r = L[:]
print(r)

# 元组也可以使用切片 返回一个元组
print((0,1,2,3,4)[:3])

# 字符串也可以看成list 使用切片 操作结果仍是字符串
# 对字符串的截取可以用切片进行操作
print('ABCDE'[:3])


# 利用切片操作 实现一个trim()函数 去除字符串首尾的空格 注意不要调用str的strip()方法：
def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while s[-1:] == " ":
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# ------------------------迭代-------------------------#
# 无论数据结构是否有下标 python均可以对其进行迭代
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

# 由于dict不是顺序存储 所以运行结果可能不一样
# 默认情况 dict迭代的是key 如果迭代value使用
for value in d.values():
    print(value)

# 同时迭代键和值
for k,v in d.items():
    print(k,v)

# 字符串也可迭代
for ch in 'ABC':
    print(ch)

# 只要为可迭代对象 for都可以正常运行
# 判断其是否为可迭代对象：
from collections import Iterable
print(isinstance('abc', Iterable))

print(isinstance([1,3,4,5], Iterable))

print(isinstance(123,Iterable))


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        min = max = L[0]
        for i in L:
            if max < i:
                max = i
            if min > i:
                min = i
        return (min, max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

