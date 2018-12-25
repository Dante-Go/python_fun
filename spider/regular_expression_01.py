import re

s = r'(\d+)'
pattern = re.compile(s)
m = pattern.search('one12two2three34')
print(m.groups())
m = pattern.search('one1123two34', 10, 50)
print(m.group())
