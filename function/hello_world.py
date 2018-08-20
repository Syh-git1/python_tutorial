#print("hello world")
#coding=utf-8

import time

def test():
    now_time = time.time()
    a = 10
    a += 1
    b = 'test string'

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

def findMinAndMax(L):
    if L == []:
        return (None, None)
    else:
        max = min = L[0]
        for n in L:
            if n > max:
                max = n
            if n < min:
                min = n
        return (min,max)
def f(x):
    return x*x

def normalize(name):
    return name[0].upper()+name[1:].lower()

if __name__ == '__main__':
    if trim('hello  ') != 'hello':
        print('测试失败1!')
    elif trim('  hello') != 'hello':
        print('测试失败2!')
    elif trim('  hello  ') != 'hello':
        print('测试失败3!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败4!')
    elif trim('') != '':
        print('测试失败5!')
    elif trim('    ') != '':
        print('测试失败6!')
    else:
        print('测试成功!')

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
    a = list(range(1,11))
    print(a)

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    r = map(f, list1)
    print(list(r))


    print(map(str, list1))
    print(list(map(str,list1)))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)





