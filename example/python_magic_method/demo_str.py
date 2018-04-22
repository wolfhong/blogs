# -*- coding: utf-8 -*-

class StrDemo1:
    def __str__(self):
        return 'StrDemo1'

class StrDemo2:
    def __str__(self):
        return 'StrDemo2'

class StrDemo3:
    def __unicode__(self):
        return u'StrDemo3'

demo1 = StrDemo1()
print str(demo1)
print unicode(demo1)

demo2 = StrDemo2()
print str(demo2)
print unicode(demo2)

demo3 = StrDemo3()
print str(demo3)
print unicode(demo3)
