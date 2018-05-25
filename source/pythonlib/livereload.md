---
layout: pythonlib
title: livereload：监视文件改动与web开发利器
toc: true
date: 2018-02-02 00:00:00
---

### 简介

[LiveReload][github]会监视指定目录下的文件变更，只要文件有变更保存，LiveReload就会执行指定的命令（比如是`make`，`build`之类的操作）。同时，LiveReload包含了一个静态服务器，默认访问 **http://localhost:5500** 即可查看。

完整的文档可参考[ReadTheDocs][readthedocs]，这里只做Python库的简单介绍。

这里举例谈一个应用场景，是我在编写[sphinx][sphinx]文档时遇到的：编辑sphinx文档时，总希望能够及时在浏览器中看到编辑后的页面效果，但是从rst文件转html文件，需要执行`make html`命令。频繁的操作很琐碎，因此需要LiveReload来替代这项工作。当工作目录中的rst文件发生变化，自动帮我执行`make html`命令。
示例如下(假设工作目录命名为*docs/*)：

``` python
    #!/usr/bin/env python

    from livereload import Server, shell
    server = Server()
    server.watch('docs/*.rst', shell('make html', cwd='docs'))
    server.serve(root='docs/_build/html')
```

`server.watch` 监视了*docs/*目录下的所有rst文件，每当文件有变更，在`cwd='docs'`指定的目录中，执行`shell('make html')`中指定的命令。

运行上述脚本，打开浏览器访问 http://localhost:5500 ，就可以实时查看到文档变更。


### 安装

    pip install livereload


### 示例

#### 命令行工具

Python-LiveReload 提供了一个命令行工具: `livereload`，提供了类似上述脚本的功能，但默认启动**35729**端口。

``` shell
    $ livereload --help
    usage: livereload [-h] [-p PORT] [-w WAIT] [directory]

    Start a `livereload` server

    positional arguments:
      directory             Directory to watch for changes

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  Port to run `livereload` server on
      -w WAIT, --wait WAIT  Time delay before reloading
```

#### Server(wsgi-app)

Python-LiveReload是为web开发者设计的，支持接入wsgi application.

``` python
    from livereload import Server, shell

    server = Server(wsgi_app)

    # run a shell command
    server.watch('static/*.stylus', 'make static')

    # run a function
    def alert():
        print('foo')
    server.watch('foo.txt', alert)

    # output stdout into a file
    server.watch('style.less', shell('lessc style.less', output='style.css'))

    server.serve()
```

#### server.watch

``server.watch`` 可以监视具体的文件路径，或者目录，或者glob pattern:

``` python
    server.watch('path/to/file.txt')
    server.watch('directory/path/')
    server.watch('glob/*.pattern')
```

你也可以使用其他的库（比如[formic][formic]，可从[GitHub][formic2]获取） 来提供更强大的功能:

``` python
    for filepath in formic.FileSet(include="**.css"):
        server.watch(filepath, 'make css')
```

``server.watch``还支持一个`delay`参数，单位为秒，表示文件变更后延迟多久才发送reload信号:

``` python
    # delay 2 seconds for reloading
    server.watch('path/to/file', delay=2)
```


#### server.serve

``server.serve`` 用于启动服务器，下面是该方法的调用示例:

``` python
    # use default settings
    server.serve()

    # livereload on another port
    server.serve(liveport=35729)

    # use custom host and port
    server.serve(port=8080, host='localhost')

    # open the web browser on startup, based on $BROWSER environment variable
    server.serve(open_url=True, debug=False)
```


#### shell

使用``shel``函数，可以帮你执行一些shell命令，配合``server.watch``一起使用:

``` python
    # you can redirect command output to a file
    server.watch('style.less', shell('lessc style.less', output='style.css'))

    # commands can be a list
    server.watch('style.less', shell(['lessc', 'style.less'], output='style.css'))

    # working with Makefile
    server.watch('assets/*.styl', shell('make assets', cwd='assets'))
```


#### 框架集成

Python-LiveReload支持与其他的web框架无缝对接，如Django、Flask、Bottle等，不过这些框架往往自带了类似LiveReload的功能，权当了解即可。
以Flask为例:

``` python
    # app is a Flask object
    app = create_app()
    # remember to use DEBUG mode for templates auto reload
    # https://github.com/lepture/python-livereload/issues/144
    app.debug = True

    server = Server(app.wsgi_app)
    # server.watch
    server.serve()
```


### More

文档与更多示例参考:
* [GitHub][github]
* [ReadTheDocs][readthedocs]


### 其他扩展

#### sphinx-autobuild

本文开始的例子中，我提到了编辑sphinx文档时遇到的麻烦，后来发现有现成的解决方案：[sphinx-autobuild][sphinx-autobuild]

你只需要安装sphinx-autobuild：

    pip install sphinx-autobuild

在工作目录*docs/*外运行:

    sphinx-autobuild docs docs/_build/html

之后打开浏览器访问： http://localhost:8000/

#### 商业的LiveReload

这是一家公司的商业化产品，并且进行了开源，与本文介绍的Python-LiveReload并无关系。
可以在其[官网](http://livereload.com/)上下载到。它提供了更加便捷的功能，有兴趣可以了解下。

![image](http://static2.extremevision.com.cn/blogimage/livereload.png)


[github]: https://github.com/lepture/python-livereload
[readthedocs]: https://livereload.readthedocs.io/en/latest/
[sphinx]: http://www.sphinx-doc.org/
[sphinx-autobuild]: https://pypi.org/project/sphinx-autobuild/

[formic]: ./formic.html
[formic2]: https://github.com/wolfhong/formic
