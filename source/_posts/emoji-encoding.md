---
title: Emoji的编码以及常见问题处理
date: 2016-11-25 01:09:43
toc: true
categories:
- 其他
tags:
- emoji
- 编码
---

我在[虎嗅上](https://www.huxiu.com/article/163386.html)看过一篇关于Emoji的趣闻, 特别有意思, 在这里跟大家分享一下。里面提到了Emoji是怎么诞生的。

> 1999年前后，日本一个名叫栗田穰崇的年轻人，和许多直男一样， 给女友发的短信经常会被误解。比如，“知道了”被解读成“生气了”、“不耐烦了”，随后引发冷战。 于是少年栗田想：“如果能在文字里插入一些表情符号来表达感情，大家应该会需要吧！”
> 原始的Emoji就这么诞生了。

Emoji极大地丰富了我们的生活和通讯交流。Emoji诞生自程序员，但反过来对程序员也造成过一些困扰。
尤其对于面向C端的产品开发者, 用户越来越习惯于输入Emoji, 因此处理字符时遇到Emoji也只会越来越频繁。



### Emoji的编码

Emoji字符是Unicode字符集中一部分. 特定形象的Emoji表情符号对应到特定的Unicode字节。
常见的Emoji表情符号在Unicode字符集中的范围和具体的字节映射关系, 可通过[Emoji Unicode Tables][emojitable]查看到。

有意思的是, 在[Emoji Unicode Tables][emojitable]表中，还给出了同一个Emoji表情在不同系统中的字体(是字体没错, Emoji的样式可通过字体文件改变)。

![image](http://static.extremevision.com.cn/blogs/static/python_emoji_1.png)

关于Emoji的最权威资料, 可以在[Unicode® Emoji Charts][emojiweb]上查阅到。
截止我写这篇文章的时刻, Emoji Charts 的最新版本是v3.0, v4.0还只是处于Beta阶段。

题外话补充一点: Unicode是一种字符编码方法，它是由国际组织设计，可以容纳全世界所有语言文字的编码方案。
我们所知道的UTF-8、UTF-16等编码, 是对Unicode的不同实现方式。
如果要深入了解更多关于ASCII、Unicode、UTF-8、gb2312、gbk等编码的相关知识，在这里强烈推荐几篇文章，讲得非常好。

- [字符编码笔记：ASCII，Unicode和UTF-8][ruanyifeng]
- [程序员趣味读物：谈谈Unicode编码][chengxuyuan]



### 一些特殊的Emoji

在众多Emoji中, 有一些特殊的Emoji 并没有显示的样式, 只是起到了控制的作用。这些控制型的Emoji 与基础Emoji 出现在一起, 可以展示更多的样式。

比如 "变量选择器-15"(VARIATION SELECTOR-15, 简写VS-15): `<U+FE0E>`, 作用是让基础Emoji 变成更接近文本样式(text-style);
而 "变量选择器-16"(VARIATION SELECTOR-16, 简写VS-16): `<U+FE0F>`, 作用则是让基础Emoji 变成更接近Emoji样式(emoji-style).

VS-15 和 VS-16 加在基础Emoji字符的后面, 可以起到控制作用(前提是必须系统支持, 否则会被忽略)。

![image](http://static.extremevision.com.cn/blogs/static/python_emoji_vs_wiki.png)

用一段Python代码来演示该例子:

    # -*- coding: utf-8 -*-
    # more info to see https://en.wikipedia.org/wiki/Emoji
    # 符号分别是上图(截图自wiki)中的符号, 最后再加上一个“狗”的Emoji
    sample_list = [u'\u2139', u'\u231B', u'\u26A0', u'\u2712', u'\u2764', u'\U0001F004', u'\U0001F21A', u'\U0001f436', ]

    # 输出原样式
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

其输出如下图, 第一行是原样式，第二行是加上VS-15后的样式，第三行是加上VS-16后的样式:

![image](http://static.extremevision.com.cn/blogs/static/python_emoji_vs.png)

另外, 还有一些控制型的Emoji, 可以对人体肤色进行改变，改变对象仅限于"表示人身体部位的Emoji".
它们分别是: `<U+1F3FB>` – `<U+1F3FF>` 共五个, 分别简称为: FITZ-1-2, FITZ-3, FITZ-4, FITZ-5, FITZ-6.

![image](http://static.extremevision.com.cn/blogs/static/python_emoji_humanskin_wiki.png)

还有一个特殊的控制符: `<U+200D>` (ZERO WIDTH JOINER, 简写ZWJ), 起到了连接Emoji的作用, 从而将多个Emoji变成一个Emoji来显示. 同样，前提是必须系统支持, 否则会被忽略.

使用Python代码演示 `FITZ-*` 和 `ZWJ`:

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
    # 如果系统支持: 连接(男人 + ZWJ + 女人 + ZWJ + 女孩)
    print u'\U0001F468' + u'\u200D' + u'\U0001F469' + u'\u200D' + u'\U0001F467'
    # 如果系统不支持: 连接(狗 + ZWJ + 猫 + ZWJ + 老鼠)
    print u'\U0001f436' + u'\u200D' + u'\U0001f431' + u'\u200D' + u'\U0001f42d'

其输出如下图:

![image](http://static.extremevision.com.cn/blogs/static/python_emoji_humanskin.png)

以上内容参考自[维基百科][wikipedia]

对Emoji 的介绍到该小节结束, 下面内容是一些关于实际中可能遇到的技术问题的解决方法。



### MySQL存储Emoji

使用MySQL存储Emoji, 只需要数据表的字符集为`utf8mb4`即可, 即`CHARSET=utf8mb4`.

如果想要知道你的MySQL数据库是否支持`utf8mb4`编码, 可通过`show charset;` 输出当前安装的MySQL所支持的所有字符集, 查看输出中是否包含有`utf8mb4`.

另外, 有一些比较老的业务, 可能一开始设计时没考虑到需要支持Emoji, 那就需要修改数据库或数据表的字符集.

    查看MySQL说支持的所有字符集
    mysql> show charset;

    查看某张表当前的字符集
    mysql> show create table <table_name>;

    创建默认字符集为utf8mb4的数据库.在该数据库中,如果创建表时是不指明字符集,则默认utf8mb4.
    mysql> create database default charset utf8mb4;

    创建字符集为utf8mb4的表, 数据库的默认字符集非utf8mb4也没问题.
    mysql> create table `<table_name>` (Column定义, Column定义, ...) DEFAULT CHARSET=utf8mb4;

    修改已存在的数据库的字符集
    mysql> alter database <db_name> default charset = utf8mb4;

    修改已存在的表的字符集
    mysql> alter table <table_name> default charset = utf8mb4;



### 使用正则表达式匹配Emoji

很可惜, Emoji的范围并没有明确的定义。正如上面提到了，Emoji Charts目前最新版本是v3.0， 未来Emoji的范围还会不断扩大。而且Emoji 在Unicode的分配中并不是连续的区间。

所以, 在这里我只能给出一个可行的匹配区间, 尽可能涵盖了基本常见的Emoj。
该匹配区间中会包含一些未定义的字符, 可能在某些系统会有定义，但是在另外的系统中并没有定义。毕竟Emoji是商业的产物。

该匹配规则区间参考了[emoji-data.txt](http://unicode.org/Public/emoji/3.0/emoji-data.txt) 和 [Unicode® Technical Report #51](http://unicode.org/reports/tr51/index.html#emoji_data), 如下:

    <U+1F300> - <U+1F5FF>      # symbols & pictographs
    <U+1F600> - <U+1F64F>      # emoticons
    <U+1F680> - <U+1F6FF>      # transport & map symbols
    <U+2600>  - <U+2B55>       # other

下面使用Python代码来演示如何使用正则表达式替换(或找出)字符串中的Emoji:

    # -*- coding: utf-8 -*-
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

输出如下:

    I have a dog [Emoji] . You have a cat [Emoji] ! I smile [Emoji] to you!
    [u'\U0001f436', u'\U0001f431', u'\U0001f601']

上面例子中, 之所以使用`try...except...`来处理代码, 是考虑到 UCS-2 (Narrow UCS-2 build) 和 UCS-4 (Wide UCS-4 build) 的区别.
该Demo例子参考了[stackoverflow](http://stackoverflow.com/questions/26568722/remove-unicode-emoji-using-re-in-python)上的精彩回答, 解答了我对此的困惑。

关于UCS-2和UCS-4的区别, 在上面提到的扩展阅读[程序员趣味读物：谈谈Unicode编码][chengxuyuan]中有提到, 值得一看.

本文中使用到的示例代码，可以在[我的github](https://github.com/wolfhong/blogs/tree/master/example/python_emoji)下载到。



### 带有Emoji的字符串截取

在Python、JavaScript 这类编程语言中, 一个中文字符的长度为1，但是对大部分的Emoji(并非全部), 取长度则是2。下面使用Python做演示。

以中文的"汉"字取长度为例，取长度为1:

    >>>len(u'汉')
    1

而对于Emoji，以`<U+1f436>`(该Emoji是一只萌萌的狗)为例，取长度为2:

    >>>len(u'\U0001f436')
    2

那么, 这就存在一个隐患, 在对字符串进行截断时可能从中间截断, 导致该字符显示为乱码, 甚至引发报错。

下面例子中, 对字符串进行截取时，正好从`<U+1f436>`的中间截断了，出现了乱码:

    >>>u'这是一只可爱的狗狗\U0001f436'.__len__()
    11
    >>>u'这是一只可爱的狗狗\U0001f436'[0:10]
    这是一只可爱的狗狗???


实际场景中，对字符串进行截断是非常常见的需求，而且字符串往往可能是用户高度自由的输入内容, 那么包含Emoji的可能性其实是很高的。
一个具体的场景就是: 你正在开发了一款社交APP, 允许用户保存文字记录, 然后在应用的某个地方, 又需要显示这些文字记录的摘要，摘要只显示用户输入的前100个字符, 超出部分用省略号表示。
这种情况下，就不可避免的可能发生Emoji在中间被截断的问题。

解决方案也有多种:

- 全文进行正则匹配, 去掉大部分Emoji, 但是文本长度过长的情况消耗太大, 不值得.
- 先截取前200个字符, 匹配去掉Emoji再截取100个字符. 貌似可行. 但如果极端条件下前200个字符都是Emoji怎么办? 管他的.
- 运用上面提到的扩展阅读: [字符编码笔记：ASCII，Unicode和UTF-8][ruanyifeng]中提到的UTF-8的编码规则, 对截断后字符串的最后字符进行检查, 发现是截断的字符即进行剔除。该方案可行, 不过你需要自己去实现了。
- 允许一定概率出现乱码, 乱码就乱码吧，概率不高，不影响主要体验。将更多精力放在避免其他bug上吧。


[emojitable]: http://apps.timwhitlock.info/emoji/tables/unicode#block-6c-other-additional-symbols
[emojiweb]: http://unicode.org/emoji/charts/
[wikipedia]: https://en.wikipedia.org/wiki/Emoji
[ruanyifeng]: http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html
[chengxuyuan]: http://pcedu.pconline.com.cn/empolder/gj/other/0505/616631_all.html
