import re
str1 = 'Hello world is awesome'
result = re.search(r'(.*) world (.*?) .*', str1, re.M|re.I)
if(result):
    print(result.group())
    print(result.group(1))
    print(result.group(2))
    print(result.group(0))
else:
    print('No result')
