# -*- coding: utf-8 -*-

class XClass:

    def __call__(self, a, b):
        return a + b

def add(a, b):
    return a + b

x = XClass()
print 'x(1, 2)', x(1, 2)
print 'callable(x)', callable(x)
print 'add(1, 2)', add(1, 2)
print 'callable(add)', callable(add)
