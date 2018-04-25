---
title: crontab执行失败的多种原因
date: 2016-10-24 23:32:58
toc: true
categories:
- devops
tags:
- linux
---

crontab是Linux下执行定时任务的常见方法。
这里总结一下自己遇到的或者被问到的相关问题, 诸如"为什么crontab执行失败", "为什么crontab没有执行"。

在分析之前, 我们先确认一个前提: 操作命令本身的执行并没有问题, 在shell下可正常运行;
不存在权限问题, 更没有参数缺少的问题。
也即是说，使用`crontab -l`输出该命令时，直接复制到shell中是可以正常执行的，但是在crontab中事与愿违。

在以上的前提下，可能是如下的几个原因，导致了crontab不能正常执行。



### crontab中包含非法字符

比如这个命令:

    echo `date +%Y%m%d`

该命令在shell下直接执行是没问题的，但是在crontab中就有问题. 原因是crontab中不能出现非法字符```%```.
```%```字符如果没有跟在转义字符```\```之后，将会被当做换行符，第一个```%```字符之后的内容将会视为该行命令的标准输入。

通过 `man 5 crontab` 查看到该问题的说明, 如下图:
![非法字符的说明](http://static.extremevision.com.cn/membercms/crontab_error_img2.png)

解决方法也很简单:
* 既可以将命令写在另一个sh文件中,然后再来执行该文件
* 也可以使用```\```符号对非法字符进行转义



### /etc/crontab 与 contab -e 两种格式混淆

定时任务有两种编辑方法，一种是root用户下编辑/etc/crontab文件: `vi /etc/crontab`;
一种是在特定用户身份下(可能是root,可能非root)，执行`crontab -e` 进行编辑.

前者的格式相比于后者, 多了一个表示执行命令的“用户身份”的字段.如下图:
![前者的格式](http://static.extremevision.com.cn/membercms/crontab_error_img1.png)

这很好理解, /etc/crontab 对所有用户都是同一个文件,当然需要指明是以哪个用户来执行命令了.

以 `echo "right" >> /tmp/output_right.txt` 命令为例:
在编辑`/etc/crontab`时需要写成:

    */1 * * * * root echo "right" >> /tmp/output_right.txt

在`crontab -e`的情况下则要写成:

    */1 * * * * echo "right" >> /tmp/output_right.txt



### crond服务未启动

这个就太好检查了, 执行`service crond status` 查看该服务的运行状态.
如果进程已经dead，重启一下即可:

    service crond start



### 标准/错误输出中包含不支持字符(比如中文)

这仅仅是一个可能的原因, 不同环境上的表现可能不一样, 跟操作系统支持的编码有关.

比如下面一段简单的python代码:

    # -*- coding: utf-8 -*-
    print(u'中文')

将以上代码保存为文件demo.py. 在shell中执行 `python demo.py` 是没问题的, 但是在crontab就可能出现问题.

总之避免在日志输出中包含中文吧。



### 缺少环境变量或者未使用绝对路径

环境变量在/etc/crontab 顶部的`PATH`中指定了。默认情况下，`PATH=/sbin:/bin:/usr/sbin:/usr/bin`

假设你安装了`supervisorctl`(一个守护进程的软件)到路径`/usr/local/bin/supervisorctl`, 然后定义了每天一次的定时任务:

    0 1 * * * supervisorctl restart all
    
该定时任务并不会生效。

原因在于，`PATH`中并没有将`/usr/local/bin`加入环境变量。执行`supervisorctl`时找不到该文件。
解决方法有：

* 将`/usr/local/bin`加入`PATH`
* 或者使用绝对路径 `0 1 * * * /usr/local/bin/supervisorctl restart all`
