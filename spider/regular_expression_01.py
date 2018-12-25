import re

s = r'(\d+)'
pattern = re.compile(s)
m = pattern.search('one12two2three34')
print(m.groups())
m = pattern.search('one1123two34', 10, 50)
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))
print('-----------------------------------------------------')
s = pattern.findall('aaa 11 and 12 bb 33')
print(s)

s = pattern.finditer('aaa 11 and 22, bb 33')
print(type(s))

for i in s:
	print(i.group())

print('-----------------------------------------------------')
