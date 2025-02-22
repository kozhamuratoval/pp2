'''def a(n):
    for i in range(n + 1):
        yield i ** 2
n = int(input())
for i in a(n):
    print(i, end=" ")'''
'''
def a(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input())
print(",".join(map(str, a(n))))'''
'''
def a(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
print(list(a(n)))'''

'''def r(a, b):
    for i in range(a, b + 1):
        yield i ** 2
a = int(input())
b = int(input())
for i in r(a, b):
    print(i)'''

'''
def a(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for num in a(n):
    print(num, end=" ")'''

