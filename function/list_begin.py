#coding=utf-8

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取list数据笨方法
print([L[0], L[1], L[2]])
#扩展使用循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
#切片取值  省略前部表示从0开始 省略后部表示取到最后
print(L[0:3])
print(L[:3])
print(L[3:])

# 支持倒数切片 -1表示倒数第一个数的索引
print(L[-2:])

#  建立新列表
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
