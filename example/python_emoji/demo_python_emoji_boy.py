# -*- coding: utf-8 -*-
# more info to see https://en.wikipedia.org/wiki/Emoji


# man_list 分别是: 男孩  女孩  男人  女人
man_list = [u'\U0001F466', u'\U0001F467', u'\U0001F468', u'\U0001F469']

# skin_color_list 分别是: 空字符串,表示默认  白种人 -->(不断加深肤色)  黑种人
skin_color_list = ['', u'\U0001F3FB', u'\U0001F3FC', u'\U0001F3FD', u'\U0001F3FE', u'\U0001F3FF', ]

for man in man_list:
    for color in skin_color_list:
        print (man + color),
    print
    print '-' * 20


# Emoji的连接符<U+200D>  (英文名为: ZERO WIDTH JOINER, 简写ZWJ )
# 如果系统支持: 连接(男人 + 女人 + 女孩)
print u'\U0001F468' + u'\u200D' + u'\U0001F469' + u'\u200D' + u'\U0001F467'

# 如果系统不支持: 连接(狗 + 猫 + 老鼠)
print u'\U0001f436' + u'\u200D' + u'\U0001f431' + u'\u200D' + u'\U0001f42d'
