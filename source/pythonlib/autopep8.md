---
layout: pythonlib
title: autopep8/yapf：Python代码的格式化工具
toc: true
date: 2018-02-05 00:00:00
---

### 简介

[autopep8][github] 可以自动格式化Python代码，使其符合[PEP-8][pep8]规范。 它是基于pycodestyle（[见另一篇文章][pycodestyle]）来判断哪部分代码需要进行格式化的。


### 安装

    pip install autopep8

### 示例

为了演示autopep8的作用，我们先写一段非常丑陋、不符合PEP-8标准的代码。
比如下面这段代码，请复制保存为文件:

``` python
import math, sys;

def example1():
    ####This is a long comment. This should be wrapped to fit within 72 characters.
    some_tuple=(   1,2, 3,'a'  );
    some_variable={'long':'Long code lines should be wrapped within 79 characters.',
    'other':[math.pi, 100,200,300,9876543210,'This is a long string that goes on'],
    'more':{'inner':'This whole logical line should be wrapped.',some_tuple:[1,
    20,300,40000,500000000,60000000000000000]}}
    return (some_tuple, some_variable)
def example2(): return {'has_key() is deprecated':True}.has_key({'f':2}.has_key(''));
class Example3(   object ):
    def __init__    ( self, bar ):
     #Comments should have a space after the hash.
     if bar == None:
         bar = 0
     if bar == True:
         bar = 0
     if bar : bar+=1;  bar=bar* bar   ; return bar
     else:
                    some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
                    return (sys.path, some_string)
```

现在来看看autopep8能够做些什么。请在命令行中执行:

    autopep8 -aa <filename>

可以看到输出如下。先不看输出，暂且来看看上面的命令，有几个命令行选项值得关注下。

`-aa` 是`--aggressive --aggressive`的缩写，表示格式化时，代码侵入性级别2。这里解释一下侵入性`aggressive`。

* 当不使用`--aggressive`选项时，autopep8 **只会对空格进行格式化** ，不会修改你的其他语法。
* 当使用1个`--aggressive`时，表示侵入性级别1，会修改一些不推荐的语法。比如`x == None`会被修改为`x is None`。但这有一定的风险，可能会改变原来程序的语义，比如例子中，`x`如果改写了`__eq__`方法，就会有问题。
* 当使用2个`--aggressive`时，侵入性级别增加1，`if x == True:`之类的代码会被改为`if x:`。

侵入性级别越高，格式化后的代码语义改变的风险越大。如例子中的`Example3`，实际上程序的语义已经发生了改变（请读者自己思考为什么）。

个人建议，在自己的编辑器中使用flake8(也使用了pycodestyle)等插件进行提示即可，不要依赖于autopep8来修改源码。当然，坚持Pythonic地写Python才是根本。

如果autopep8使用选项`--in-place`(缩写`-i`)，那么就不会输入格式化后的代码，而是将格式化直接应用到源文件上，改动源文件。此时，命令就要改为:
    
    autopep8 --in-place --aggressive --aggressive <filename>

选项`--max-line-length=n` 可以设置每行代码的最长字符限制，默认是79。社区中很多人反映79个字符的长度限制应该放宽，毕竟这是历史原因导致的。

上面提到的`autopep8 -aa <filename>`的输出:

``` python
import math
import sys


def example1():
    # This is a long comment. This should be wrapped to fit within 72
    # characters.
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        'long': 'Long code lines should be wrapped within 79 characters.',
        'other': [
            math.pi,
            100,
            200,
            300,
            9876543210,
            'This is a long string that goes on'],
        'more': {
            'inner': 'This whole logical line should be wrapped.',
            some_tuple: [
                1,
                20,
                300,
                40000,
                500000000,
                60000000000000000]}}
    return (some_tuple, some_variable)


def example2(): return ('' in {'f': 2}) in {'has_key() is deprecated': True};


class Example3(object):
    def __init__(self, bar):
        # Comments should have a space after the hash.
        if bar is None:
            bar = 0
        if bar:
            bar = 0
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
            return (sys.path, some_string)
```

再次强调，侵入性级别越高，格式化后的代码语义改变的风险越大。不要滥用`--aggressive`选项。坚持Pythonic地写Python才是根本。

### More

文档与更多示例参考:
* [GitHub][github]

### 其他扩展

#### YAPF

个人推荐使用[yapf][yapf]来取代autopep8。本文介绍autopep8，仅仅是因为它应用更加广泛，方便解释。

不同于autopep8、pep8ify之类的Python代码格式化程序: 它们的目的是消除Python代码中不符合PEP-8规范的错误。符合规范的代码不会被修改。然而，符合PEP-8规范的代码，不一定是好看的代码。
yapf使用clang-format算法来实现代码的重新排版，即便代码本来就符合规范。
**yapf不具侵入性**。

你可以通过pip安装yapf:

    pip install yapf

安装后，你可以试着使用`yapf <filename>`来格式化前面例子中的丑陋代码。或者直接在[online demo][yapf-online]中体验一番吧。

#### docformatter

[docformatter][docformatter]，正如其名，格式化Python文档的，用法很类似。挺小众的功能，稍微提一下就行了。


[pycodestyle]: ./pycodestyle.html
[pep8]: https://www.python.org/dev/peps/pep-0008/
[github]: https://github.com/hhatto/autopep8
[yapf]: https://github.com/google/yapf
[yapf-online]: https://yapf.now.sh/
[docformatter]: https://github.com/myint/docformatter
