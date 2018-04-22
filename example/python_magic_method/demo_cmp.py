# -*- coding: utf-8 -*-

class Word(str):
    '''存储单词的类，定义比较单词的几种方法'''
    def __new__(cls, word):
        # 注意我们必须要用到__new__方法，因为str是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')]  # 单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)


print 'foo < fool:', Word('foo') < Word('fool')
print 'foolish > fool:', Word('foolish') > Word('fool')
print 'bar >= foo:', Word('bar') >= Word('foo')
print 'bar <= foo:', Word('bar') <= Word('foo')
print 'bar == foo:', Word('bar') == Word('foo')  # 用了str内置的比较方法来进行比较
print 'bar != foo:', Word('bar') != Word('foo')
