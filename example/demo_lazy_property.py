# -*- coding: utf-8 -*-
class LazyProperty(object):
    '''类属性的延迟计算, 访问的时候才开始计算，一旦计算完成，会将结果缓存起来，下次直接返回'''

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, ownercls):
        if instance is None:
            return None
        value = self.func(instance)  # func(self)
        setattr(instance, self.func.__name__, value)  # 用新的属性名覆盖方法
        return value


class Foo(object):

    @LazyProperty
    def bar(self):
        print 'long time to compute...'
        return 1

foo = Foo()
print foo.bar  # 只有第一次会执行print,之后就不会了
print foo.bar
print foo.bar
