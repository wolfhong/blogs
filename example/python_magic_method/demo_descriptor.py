# -*- coding: utf-8 -*-

class Meter(object):
    '''Descriptor for a meter.'''
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    '''Descriptor for a foot.'''
    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    meter = Meter()
    foot = Foot()

d = Distance()
print d.meter, d.foot
d.meter = 1
print d.meter, d.foot
d.meter = 2
print d.meter, d.foot
