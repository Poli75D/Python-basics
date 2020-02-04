import re
pattern = re.compile('ell')
print(pattern.match('hello world'))#none
print(pattern.match('hello world', 1))#match
result = pattern.match('hello world',1)
print(result)
