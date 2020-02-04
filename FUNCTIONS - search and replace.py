import re

str1 = '23144234 . 4324w34u/b2;3wy4gr'

result = re.sub(r'\D', 'CHUJ', str1)#zamienia nieDigity na chuje
print(result)
