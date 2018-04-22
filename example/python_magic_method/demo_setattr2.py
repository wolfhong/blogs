# -*- coding: utf-8 -*-


class Access(object):

    def __getattr__(self, name):
        print '__getattr__'
        return super(Access, self).__getattr__(name)

    def __setattr__(self, name, value):
        print '__setattr__'
        return super(Access, self).__setattr__(name, value)

    def __delattr__(self, name):
        print '__delattr__'
        return super(Access, self).__delattr__(name)

    def __getattribute__(self, name):
        print '__getattribute__'
        return super(Access, self).__getattribute__(name)

access = Access()
access.attr1 = True
access.attr1
try:
    access.attr2
except AttributeError:
    pass
del access.attr1
