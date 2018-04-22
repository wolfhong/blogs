# -*- coding: utf-8 -*-
# more info to see https://en.wikipedia.org/wiki/Emoji

# 符号分别是上图(截图自wiki)中的符号, 最后再加上一个“狗”的Emoji
sample_list = [u'\u2139', u'\u231B', u'\u26A0', u'\u2712', u'\u2764', u'\U0001F004', u'\U0001F21A', u'\U0001f436', ]

for code in sample_list:
    print code,

print
print '-' * 20

# 后面加上VS-15
for code in sample_list:
    print (code + u'\uFE0E'),

print
print '-' * 20

# 后面加上VS-16
for code in sample_list:
    print (code + u'\uFE0F'),
