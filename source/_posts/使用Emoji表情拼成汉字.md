---
title: 使用Emoji表情拼成汉字
date: 2016-11-23 01:08:26
toc: true
categories:
- 其他
tags:
- emoji
---

这只是一个娱乐性的实现，纯属突发奇想。

使用Emoji表情组成汉字或者简笔画，在微信、QQ的传播中甚广，就会想着要不自己也试着做出来吧.

比如下图:

![image](http://static.extremevision.com.cn/membercms/zh2emoji/beer_500.png?imageMogr2/thumbnail/400x)


### 实现步骤

一开始想到的实现方案就是: 首先将汉字转化成白底黑字的图片, 然后将图片根据灰度值映射成不同的字符打印在终端。

前者文字转图片，使用常见的绘图库非常好实现(比如python的PIL库);
工作量无非只是实现过程中慢慢调整排版, 以达到自己的预期效果.

后者则是简单的映射关系而已: 将图片中像素点的灰度值, 映射成某个字符; 在该实现中, 对于黑底白字的图片只有两个映射关系, 黑字对应要替换的Emoji字符, 白底对应空白.

该部分的python实现代码如下:

    ascii_char = list('1234567890abcd ')  # 任意多个字符,灰度值的映射区间

    def select_ascii_char(r, g, b):
        ''' 在灰度图像中,灰度值最高为255,代表白色; 最低为0,代表黑色 '''
        # 把RGB转为灰度值，并且返回该灰度值对应的字符标记
        # 'RGB－灰度值'转换公式如下
        gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)
        # ascii_char中的一个字符所能表示的灰度值区间
        unit = 256.0 / len(ascii_char)
        return ascii_char[int(gray/unit)]

`select_ascii_char` 就实现了将一个像素点映射成一个具体的自定义字符char.

在本功能的实现中, `ascii_char`更简单, 只需要两个字符即可: 一个任意给定, 一个是空格.

因此将 `ascii_char` 换成 `[u'❤️ ', u'  ']`

由于需要将图片的像素点映射到可在终端打印的字符, 终端的显示空间有限, 所以需要对图片进行缩小调整.

`zh2emoji`的代码在[我的github上](https://github.com/wolfhong/zh2emoji)有对应的代码下载, 如果你有兴趣，可以fork后实现自己想要的更多自定义功能.


### 展示例子

一个"茴"字我有N多种写法:

    print image2print(word2image(u'茴'), u'❤️ ')
    print image2print(word2image(u'茴'), u'茴', width=40)

输出结果如下:

![image](http://static.extremevision.com.cn/membercms/zh2emoji/emoji_500.png?imageMogr2/thumbnail/400x)
![image](http://static.extremevision.com.cn/membercms/zh2emoji/chinese_500.png?imageMogr2/thumbnail/400x)

用😂 组成"哭"字:

![image](http://static.extremevision.com.cn/membercms/zh2emoji/ku_500.png?imageMogr2/thumbnail/400x)

### 扩展

基于zh2emoji，自己实现了一个可能有点儿用的扩展: `demo_show_animation.py`.

它可以将一句话在终端依次打印出来,使用你决定的Emoji或者其他字符.

比如你试着执行 `python ./demo_show_animation.py 喜欢就点个赞呗`, 将在终端执行一段展示文字的动画, 展示的文字就是你刚才输入的话.

如果你能够坚持看到这里, 不知道你有没有想到一些有意思的玩法不? 欢迎一起参与。编程是一种乐趣，代码是将一些头脑想法实现出来的媒介；程序员写代码，就好比作家写写文字，是一种习惯。

关于Emoji的更多知识介绍，可以阅读我的另一篇正经的博客: [Emoji的编码以及常见问题的解决方法](/posts/Emoji的编码以及常见问题的解决方法/)
