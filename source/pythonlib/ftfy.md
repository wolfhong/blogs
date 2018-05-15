---
layout: pythonlib
title: ftfy：转化不好的Unicode字符
toc: true
date: 2018-03-02 00:00:00
---

### 简介

[ftfy][github]的目标是将不好的Unicode字符转为好的Unicode字符。
所谓的不好的Unicode字符的产生，可能有多种原因:

* 比如，用一种标准编码Unicode后错误的使用另一种标准对其进行解码， 会产生无意义的字符，也即常说的"变为乱码"(mojibake)。 这可以使用`ftfy.fix_encoding()` 进行修复。
* 又比如，用户错误输入，使用了[全角符号][wiki]"ＱＱ１２３４５６" 代替了半角符号"QQ123456"，"Ｎａｍｅ"代替了"Name"。这可以使用`ftfy.fix_text()` 进行修复。
* 又比如，从PDF文件复制内容粘贴时，有时候会复制出"ﬂ o p"这种样子的字符串， 实际上应该要转化为"flop"才对。
* 又比如，文本中因为各种原因的错误，不小心带上了html的"`&amp;`"，或者bash的"`\033[31m`"，诸如此类的符号。

这里提到的应用场景只是文档中列举的一部分，可以移步[ReadTheDocs][readthedocs]查看更多。本文只是简单介绍ftfy库而已。

ftfy之所以可以将乱码恢复原样，是因为UTF-8 是一种设计良好的编码，它在误用时很明显，并且一串mojibake通常包含恢复原始字符串所需的全部信息。 当使用Twitter上的多语言数据对ftfy进行测试时，它的误报率低于百万分之一。


### 安装

    pip install ftfy

如果你还在使用Python2，需要安装低版本的ftfy，新版本的ftfy不再支持Python2:

    pip install 'ftfy<5'


### 示例

``` python
>>> print(fix_encoding('This â€” should be an em dash'))
This — should be an em dash
>>> print(fix_encoding('This text is sad .â\x81”.'))
This text is sad .⁔.
>>> print(fix_encoding('The more you know ðŸŒ '))
The more you know 🌠
```

``` python
>>> print(fix_text('ＬＯＵＤ　ＮＯＩＳＥＳ'))
LOUD NOISES
>>> print(fix_text('Broken text&hellip; it&#x2019;s ﬂubberiﬁc! it&#x2019;s...', normalization='NFKC'))
Broken text... it's flubberific! it's...
>>> print(fix_text("&macr;\\_(ã\x83\x84)_/&macr;"))
¯\\_(ツ)_/¯
>>> print(fix_text("they hit the ground with a ﬂ o p；"))
they hit the ground with a fl o p;
```

### More

* [GitHub][github]
* [ReadTheDocs][readthedocs]
* [python实现全角半角的相互转换][full2half]

[github]: https://github.com/LuminosoInsight/python-ftfy
[readthedocs]: http://ftfy.readthedocs.io/en/latest/
[wiki]: https://zh.wikipedia.org/wiki/%E5%85%A8%E5%BD%A2%E5%92%8C%E5%8D%8A%E5%BD%A2
[full2half]: http://www.cnblogs.com/kaituorensheng/p/3554571.htm
