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
print((0, 1, 2, 3, 4)[:3])

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
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 由于dict不是顺序存储 所以运行结果可能不一样
# 默认情况 dict迭代的是key 如果迭代value使用
for value in d.values():
    print(value)

# 同时迭代键和值
for k, v in d.items():
    print(k, v)

# 字符串也可迭代
for ch in 'ABC':
    print(ch)

# 只要为可迭代对象 for都可以正常运行
# 判断其是否为可迭代对象：
from collections import Iterable

print(isinstance('abc', Iterable))

print(isinstance([1, 3, 4, 5], Iterable))

print(isinstance(123, Iterable))


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

# ------------------------列表生成式-------------------------#

# 生成列表1-10可以使用
print(list(range(1, 11)))

# 生成1-10的平方可以使用迭代
L = []
for i in range(1, 11):
    L.append(i * i)

print(L)

# 或者直接使用语句（强大）
print([i * i for i in range(1, 11)])

# for语句后可以加上if判断 方便我们进行筛选
print([i * i for i in range(1, 11) if i % 2 == 0])

# 两层循环生成排列
print([m + n for m in 'ABC' for n in 'XYZ'])

# 运用列表生成式 写出简洁代码 例如列出当前目录下所有的文件和目录名
import os

print([d for d in os.listdir('.')])

# 类似于for循环可以使用两个以上变量 生成列表也可以使用多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

# 把list中所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 练习 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# >>> L = ['Hello', 'World', 18, 'Apple', None]
# >>> [s.lower() for s in L]
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'
# 请修改列表生成式 通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# ------------------------生成器-------------------------#
# 一边循环一边计算的机制 被成为生成器：generator
# 将列表生成式[]改成() 就创建了generator
g = (x * x for x in range(10))  # g即为生成器
print(g)
# 通过next(g)可以获得generator下一个返回值 当没有下一个元素的时候 抛出StopIteration的错误
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('------')
# (注意 next之后 g的指针就指向了下一个 不会从头开始 所以下边的for是16之后的输出)
# 使用for循环
for n in g:
    print(n)


# 如果推算算法复杂 类似列表生成式的for循环无法实现的时候 可以用函数实现 例如 Fibonacci数列 1 1 2 3 5 8 13 21 34
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b  # 相当于a = b b = a + b
        n = n + 1
    return 'done'


print(fib(6))


# 将上边的函数转换成generator 只需要将 print(b) 改成 yield b即可

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b  # 相当于a = b b = a + b
        n = n + 1
    return 'done'


# (如果函数定义中包含 yield关键字 函数就成为了generator)
f = fib(6)
print(f)
for s in f:
    print(s)


# 变成generator的函数 在每次调用next()的时候执行 遇到yield语句返回 再次执行时从上次返回的yield语句处继续执行
# 例如
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


o = odd()
print(next(o))
print(next(o))
print(next(o))

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值
# 必须捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 练习
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

def triangles():
    row = [1]
    while True:
        yield (row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
    pass


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

# ------------------------迭代器-------------------------#

# 生成器
# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值
from collections import Iterable

print(isinstance([], Iterable))  # true

print(isinstance({}, Iterable))  # true

print(isinstance('abc', Iterable))  # true

print(isinstance((x for x in range(10)), Iterable))

print(isinstance(100, Iterable))

# 而可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterator

print(isinstance((x for x in range(10)), Iterator))  # true

print(isinstance([], Iterator))  # false

print(isinstance({}, Iterator))  # false

print(isinstance('abc', Iterator))  # false

# 可以看出list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))

print(isinstance(iter('abc'), Iterator))

# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列 但我们却不能提前知道序列的长度
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 小结： 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# 集合数据类型如list、dict、str等是Iterable但不是Iterator 不过可以通过iter()函数获得一个Iterator对象

