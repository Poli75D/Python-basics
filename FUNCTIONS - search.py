import re
pattern = re.compile('ell')
print(pattern.search('hello world',1))#match
print(pattern.search('hello world',2))#none
