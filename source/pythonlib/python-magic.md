---
layout: pythonlib
toc: true
title: python-magic：文件类型识别
date: 2018-02-24 00:00:00
---

### 简介

[python-magic][github]是libmagic文件类型识别库的python接口。
libmagic识别文件类型的方式，是通过检查文件头部的一些字节，然后与预设的文件类型列表进行比对。这比简单地检查文件后缀名的方式靠谱多了。
Unix命令行中的`file <文件路径>`命令，就是通过该方式实现功能的。

### 安装

Linux下安装:

    pip install python-magic

OSX下安装(需要先安装libmagic依赖项):

    brew install libmagic
    pip install python-magic

Windows下安装:

    pip install python-magic-bin 0.4.14

### 示例

```python
>>> import magic
>>> magic.from_file("testdata/test.pdf")
'PDF document, version 1.2'
>>> magic.from_file("testdata/test.pdf", mime=True)
'application/pdf'
>>> magic.from_buffer(open("testdata/test.pdf", "rb").read(1024))
'PDF document, version 1.2'
>>> magic.from_file('index.md')
'UTF-8 Unicode text'
```

可以从URL中直接判断资源类型:

``` python
>>> import requests
>>> import magic
>>> magic.from_buffer(requests.get('https://www.baidu.com/img/bd_logo1.png?where=super', stream=True).raw.read(1024))
'PNG image data, 540 x 258, 8-bit colormap, non-interlaced'
>>> magic.from_buffer(requests.get('https://www.baidu.com/img/bd_logo1.png?where=super', stream=True).raw.read(1024), mime=True)
'image/png'
```

上面的例子中可以看到，通过读取图片流的一小段字节，就可以判断图片的尺寸，不需要下载整张图片。

### More

文档与更多示例参考:
* [GitHub][github]

### 其他扩展

Python的标准库中，[imghdr][imghdr]可以识别图片文件的类型。

``` python
>>> import imghdr
>>> imghdr.what('bass.gif')
'gif'
>>> imghdr.what(None, h=open('bass.gif', 'rb').read(1024))
'gif'
```

[github]: https://github.com/ahupp/python-magic
[imghdr]: https://docs.python.org/3/library/imghdr.html
