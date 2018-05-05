---
layout: pythonlib
title: pycodestyle/pep8：Python代码风格检查器
toc: true
date: 2018-02-04 00:00:00
---

### 简介

[pycodestyle][github]是一个Python代码风格检查器，用于检查你的Python代码是否符合[PEP-8][pep8]规范。PEP-8 是Python社区给出的Python编程风格指导手册。

虽然Python代码不符合该规范也是可以运行的，但遵循相同的代码风格非常重要，特别是需要与其他开发者一起维护同一个项目。因此需要这样的一些工具，能够检查Python代码是否违反PEP-8 规范，并对违反PEP-8 规范的地方给出相应的提示信息。

pycodestyle项目以前名字为`pep8`，“但Python之父认为这个工具并没有完全遵循PEP-0008标准，没有完整地体现标准的精神”，因此改名。这里有一个[小故事][fun-story]。

### 安装

    pip install pycodestyle

### 示例

pycodestyle可以作用命令行工具被使用。（如果需要的话，项目中采用`import pycodestyle`的方式导入也是可行的）

pycodestyle 后面的参数，既可以是Python代码的文件路径，也可以是目录。
下面示例中，会提示pycodestyle检查文件时遇到的每种违反PEP-8 规范的第一个警告或错误。

    $ pycodestyle --first optparse.py
    optparse.py:69:11: E401 multiple imports on one line
    optparse.py:77:1: E302 expected 2 blank lines, found 1
    optparse.py:88:5: E301 expected 1 blank line, found 0
    optparse.py:222:34: W602 deprecated form of raising exception
    optparse.py:347:31: E211 whitespace before '('
    optparse.py:357:17: E201 whitespace after '{'
    optparse.py:472:29: E221 multiple spaces before operator
    optparse.py:544:21: W601 .has_key() is deprecated, use 'in'

需要显示更多信息时:

    $ pycodestyle --show-source --show-pep8 testsuite/E40.py
    testsuite/E40.py:2:10: E401 multiple imports on one line
    import os, sys
             ^
        Imports should usually be on separate lines.

        Okay: import os\nimport sys
        E401: import sys, os

统计警告和错误信息:

    $ pycodestyle --statistics -qq Python-2.5/Lib
    232     E201 whitespace after '['
    599     E202 whitespace before ')'
    631     E203 whitespace before ','
    842     E211 whitespace before '('
    2531    E221 multiple spaces before operator
    4473    E301 expected 1 blank line, found 0
    4006    E302 expected 2 blank lines, found 1
    165     E303 too many blank lines (4)
    325     E401 multiple imports on one line
    3615    E501 line too long (82 characters)
    612     W601 .has_key() is deprecated, use 'in'
    1188    W602 deprecated form of raising exception

### More

文档与更多示例参考:
* [GitHub][github]
* [ReadTheDocs][readthedocs]

### 其他扩展

一般情况下，我们不会如示例中使用pycodestyle那样使用。我们会依赖于编辑器的一些插件来提醒自己的代码风格符合PEP-8 的规范。比较著名常用的插件有[pylint][pylint]、[flake8][flake8]、[pylama][pylama]等，vim、sublime、pycharm等编辑器都有提供。

pycodestyle是代码风格检查器，只会给出提示而不修改代码。
还有另一类工具是Python代码的格式化程序，会依照PEP-8 规范格式化Python代码，这部分可参考[Python代码的格式化](./autopep8.html)。


[fun-story]: http://www.10tiao.com/html/262/201603/403312003/1.html
[pep8]: https://www.python.org/dev/peps/pep-0008/
[github]: https://github.com/PyCQA/pycodestyle
[readthedocs]: https://pycodestyle.readthedocs.io/en/latest/

[flake8]: https://github.com/PyCQA/flake8
[pylint]: https://github.com/PyCQA/pylint
[pylama]: https://github.com/klen/pylama
