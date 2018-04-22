# -*- coding: utf-8 -*-
''' just demo for __index__ '''


class Thing(object):
    def __index__(self):
        return 1

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return hash(self) == hash(other)

thing = Thing()
list_ = ['a', 'b', 'c']
print list_[thing]  # 'b'
print list_[thing:thing]  # []

dict_ = {1: 'apple', 2: 'banana', 3: 'cat'}
print dict_[thing]  # raise KeyError
