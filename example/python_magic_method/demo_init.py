# -*- coding: utf-8 -*-


class Foo(object):

    def __init__(self):
        print 'foo __init__'
        return None  # 必须返回None,否则TypeError

    def __del__(self):
        print 'foo __del__'


foo = Foo()
foo.__del__()
print foo
del foo
print foo  # NameError, foo is not defined
