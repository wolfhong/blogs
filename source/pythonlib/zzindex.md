---
title: 一些有关Pythonlib的笔记
layout: pythonlib
toc: true
date: 2018-05-02 22:53:17
---

记录一些涉猎的Python库，但是感觉没必要整理进入专题。当做自己的一个私人笔记吧。

* [howdoi](https://github.com/gleitz/howdoi):
  即时的代码搜索库，刚接触还觉得挺新鲜的，但在国内环境联网失败，而且还是更习惯使用Google来搜索。
* [sphinx-autobuild](https://github.com/GaretJax/sphinx-autobuild):
  配合sphinx使用，监视目录，文档更新时自动编译，是提高生产力的工具。
* [mkdocs](http://www.mkdocs.org/):
  markdown文档生成器，可搭建静态网站，但现在主流是sphinx，没必要使用冷门的东西。
* [pycco](https://pycco-docs.github.io/pycco/):
  [文学编程](http://www.literateprogramming.com/)风格的文档生成器，它将代码生成为一个并排显示的文档网站:一边是注释与文档，一边是源代码。
* [ronn](https://github.com/rtomayko/ronn):
  roff的反过程，可用于构建Unix手册(即ManPages)，将人类可读的文本文件转换为终端显示的roff文件。
* [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy):
  模糊字符串匹配，匹配有多种模式，如`ratio`，`partial_ratio`，`token_sort_ratio`，`token_set_ratio`。
  使用了[Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)算法。
  使用`pip install fuzzywuzzy[speedup]`安装时会安装python-Levenshtein依赖，可以优化性能。
* [python-Levenshtein](https://pypi.org/project/python-Levenshtein/):
  字符串相似度计算。[文档](https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html)
* [shortuuid](https://github.com/skorokithakis/shortuuid):
  生成简洁明了，URL安全的UUID。
* [unidecode](https://pypi.org/project/Unidecode/):
  Unicode文本的ASCII转换形式，如URL的slug化，全角转半角，中文转拼音等。
  安装该库依赖于"wide" Unicode Characters(UCS-4 BUILD)，验证方法如下:

``` python
>>> import sys
>>> sys.maxunicode > 0xffff
True
```

* [pypinyin](https://github.com/mozillazg/python-pinyin):
  汉字转拼音
* [xpinyin](https://github.com/lxneng/xpinyin):
  也是将汉字转拼音，但是已经不活跃了，不比pypinyin库。
* [pyfiglet](https://github.com/pwaller/pyfiglet):
  [所有字体的展示效果](https://gist.github.com/wolfhong/2bf308ba727cfbc92f8edaee30cb9eef)
  [所有字体文件](https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts)
