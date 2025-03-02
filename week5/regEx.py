import re

'''def m(s):
    return bool(re.fullmatch(r'a*b*', s))
s = 'a'
e = 'ab'
r = 'aw'
print(m(s))
print(m(e))
print(m(r))'''

'''def m(s):
    return bool(re.fullmatch(r'ab{2,3}', s))
s = 'abb'
e = 'abbb'
print(m(s))
print(m(e))'''

'''def m(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)
a = input()
print(m(a))'''

'''def m(s):
    return re.findall(r'[A-Z][a-z]+', s)
s = input()
print(m(s))'''

'''def m(s):
    return bool(re.fullmatch(r'a.*b', s))
s = input()
print(m(s))'''

'''def m(s):
    return re.sub(r'[ ,.]', ':', s)
s= input()
print(m(s))'''

'''def m(s):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))
s = input()
print(m(s))'''

'''def m(s):
    return re.split(r'(?=[A-Z])', s)
s = input()
print(m(s))

def a(e):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
e = input()
print(a(e))

def l(p):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
p = input()
print(l(p))'''




