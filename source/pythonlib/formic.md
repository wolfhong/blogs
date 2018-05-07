---
layout: pythonlib
title: formic：快速查找文件
toc: true
date: 2018-02-10 00:00:00
---

### 简介

[formic][bitbucket]是[Ant FileSet and Globs][fileset-globs]的Python版实现，它可以快速查找文件。
formic既可以作为查找文件的命令行工具使用，也可以作为Python库导入到你的应用中。
查找文件时，formic可以使用通配符: `?`匹配任何**一个符号**, `*`匹配任何**一串字符**，`**`匹配任意深度的目录。

举个例子，命令行公式为`formic [目录] [-i 多个includes条件] [-e 多个excludes条件]`:

* `formic /usr/bin -i "pytho?"` 将会找到/usr/bin/python
* `formic myapp -i "*.py"` 将找出myapp目录下(包括所有子目录)所有的.py结尾的文件
* `formic -i "src/**/*.py" -e "test*"` 将找出当前目录（缺省参数）中，src目录下(包括所有子目录)所有的.py结尾的文件，排除以test开头的文件。这里src目录可以是已经嵌套很深的目录。

`-i`参数表示includes，后面接多个条件，条件使用空格分开。将查找出符合这些条件的文件。
`-e`参数表示excludes，后面接多个条件，条件使用空格分开。将排除掉符合这些条件的文件。

注意一点，formic查找文件时，会默认忽略VCS（Version Control System）的目录，比如: .git, .hg, .svn等。这个特性在作为Python库使用时也是如此。

`formic.FileSet` 在查找文件进行了优化时，includes(由`-i`参数指定)和excludes(由`-e`参数指定)是同时进行，因此即使对于深度嵌套的目录树，查找指定文件速度也很快。

### 安装

有一点很可惜，在我写这篇文章时，formic还不支持Python3。

    pip install formic

### 示例

#### 命令行

    formic [目录,缺省值为当前目录] [-i 多个includes条件] [-e 多个excludes条件]

例如下面命令，将找出当前目录中，所有的Python文件和txt文件，但是排除`__init__.py`文件和`test_`开头的文件:

    formic -i "*.py" "*.txt" -e "__init__.py" "test_*"

利用Unix管道可以实现更多功能，比如下面命令，将删除当前目录中，所有.bak结尾的文件。注意，VCS目录不受影响。

    formic -i "**/*.bak" | xargs rm

#### 作为Python库引入

用法与命令行类似，调用`formic.FileSet`即可。

``` python
import formic
fileset = formic.FileSet(include="**.py",
                         exclude=["**/*test*/**", "test_*"],
                         directory="/some/where/myapp")
for filepath in fileset:
    ......
```

更多API可参考[官方文档API][api-doc]。

这里只是做Python库的简单介绍，真正使用时，翻阅官方文档非常重要。API如何调用，参数含义，一目了然:

``` python
    class formic.formic.FileSet(include, exclude=None, directory=None, default_excludes=True, walk=<function walk at 0x1002dba28>, symlinks=True)
        Base class: object
        ......
```

### More

* 源码托管于[BitBucket][bitbucket]
* [PYPI][pypi]
* [官方文档][official-doc]


[bitbucket]: https://bitbucket.org/aviser/formic
[pypi]: https://pypi.org/project/formic/

[fileset-globs]: http://ant.apache.org/manual/dirtasks.html#patterns
[official-doc]: http://www.aviser.asia/formic/doc/index.html
[api-doc]: http://www.aviser.asia/formic/doc/api.html
