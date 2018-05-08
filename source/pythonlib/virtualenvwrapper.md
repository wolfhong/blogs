---
layout: pythonlib
title: virtualenvwrapper/virtualenv：隔离的虚拟环境
date: 2018-02-03 00:00:00
---

讲virtualenvwrapper/virtualenv 的文章已经很多了，也讲的很详细，我觉得没有必要重复造轮子。

这里提供一些学习资料（按顺序阅读）:

* [某博客](http://www.cnblogs.com/technologylife/p/6635631.html)
* [虚拟环境管理](http://pythonguidecn.readthedocs.io/zh/latest/dev/virtualenvs.html#virtualenv)
* [pip与virtualenv更多配置](http://pythonguidecn.readthedocs.io/zh/latest/dev/pip-virtualenv.html)


#### 我的总结

首次使用虚拟环境时，执行安装:

    pip install virtualenv
    pip install virtualenvwrapper
    # for windows, use virtualenvwrapper-win instand of virtualenvwrapper
    # pip install virtualenvwrapper-win

配置 `~/.bashrc`:

    export PIP_REQUIRE_VIRTUALENV=true
    export PIP_DOWNLOAD_CACHE=$HOME/.pip/cache
    export WORKON_HOME=$HOME/.virtualenvs
    # export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
    source /usr/bin/virtualenvwrapper.sh

常见的命令:

* 创建: `mkvirtualenv <my-env>`
* 创建指定环境: `mkvirtualenv -p /usr/local/bin/python3.5 <my-env>`
* 进入: `workon <my-env>`
* 退出: `deactivate`
* 删除: `rmvirtualenv <my-env>`
* 复制: `cpvirtualenv <old-env> <new-env>`
* 快速导航到虚拟环境目录: `cdvirtualenv`
* 快速导航到虚拟环境的site-packages: `cdsitepackages`
* 快速列出site-packages: `lssitepackages`
