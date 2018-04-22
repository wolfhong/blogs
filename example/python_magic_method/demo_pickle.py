# -*- coding: utf-8 -*-
from datetime import datetime
import pickle


class Distance(object):

    def __init__(self, meter):
        print 'distance __init__'
        self.meter = meter

    def get_meter(self):
        return self.meter

data = {
    'foo': [1, 2, 3],
    'bar': ('Hello', 'world!'),
    'baz': True,
    'dt': datetime(2016, 10, 01),
    'distance': Distance(1.78),
}

print 'before dump:', data

with open('data.pkl', 'wb') as jar:
    pickle.dump(data, jar)  # 将数据存储在文件中

del data
print 'data is deleted!'

with open('data.pkl', 'rb') as jar:
    data = pickle.load(jar)  # 从文件中恢复数据

print 'after load:', data
