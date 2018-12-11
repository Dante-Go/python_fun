
# coding: utf-8

# In[20]:


def hano(n ,a, b, c):
    if n == 1:
        print(a, "-->", c)
        return None
    if n == 2:
        print(a, '-->', b)
        print(a, '-->', c)
        print(b, '-->', c)
        return None
    hano(n-1, a, c, b)
    print(a, '-->', c)
    hano(n-1, b, a, c)

a = 'a'
b = 'b'
c = 'c'
hano(1, a, b, c)
print('-' * 20)
hano(2, a, b, c)
print('-' * 20)
hano(3, a, b, c)

