# -*- coding: utf-8 -*-
# more info to see: http://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python
import re

try:
    # Wide UCS-4 build
    myre = re.compile(u'['
        u'\U0001F300-\U0001F64F'
        u'\U0001F680-\U0001F6FF'
        u'\u2600-\u2B55]+',
        re.UNICODE)
except re.error:
    # Narrow UCS-2 build
    myre = re.compile(u'('
        u'\ud83c[\udf00-\udfff]|'
        u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
        u'[\u2600-\u2B55])+',
        re.UNICODE)

sss = u'I have a dog \U0001f436 . You have a cat \U0001f431 ! I smile \U0001f601 to you!'
print myre.sub('[Emoji]', sss)  # 替换字符串中的Emoji
print myre.findall(sss)         # 找出字符串中的Emoji
