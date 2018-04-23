---
title: 使用rsync在windows电脑上实现文件同步
date: 2016-10-20 01:04:07
toc: true
categories:
- 其他
tags:
- rsync
- windows
---

本文将在一台Linux服务器A上搭建rsync文件同步服务，然后在另一台windows电脑B上保持与A的单向同步。

## 一个具体的案例

某技术公司A的业务，会在服务器上生产pdf电子书、相册等文件，但是公司A本身不具备打印技术，需要转交给传统打印公司B来完成线下生产。那么问题来了，公司A怎么将每天生产出来几十个G的文件，以最小的成本传输给B呢？B公司是传统小企业，并不懂电脑技术,而且连接打印机的电脑是windows系统的.

一个自然而然想到的方案，就是借助第三方云盘服务C，公司A将文件上传C，然后公司B再从C上下载。这个方案可行，但是多了上传到传输节点C的步骤，增加了A上传C的这段时间成本。

一个简单的实施方案，就是在A上搭建rsync服务，然后告知B来同步。好在rsync提供的windows的版本，让这个方案可行。当然，该方案也适用于Mac/Linux,而且更简单。


## 服务端操作

以centos为例，安装rsync:

    yum -y install rsync
直接启动rsync:

    rsync --daemon --config=/etc/rsyncd.conf
执行 `ps -ef | grep rsync` 可以看到服务已经成功启动.

安装rsync时默认生成了配置文件 `/etc/rsyncd.conf` , 下面讲解一下配置文件. 完整的配置如下:

    uid = root
    gid = root
    use chroot = yes
    max connections = 4
    pid file = /var/run/rsyncd.pid
    exclude = lost+found/
    transfer logging = yes
    timeout = 900
    ignore nonreadable = yes
    dont compress   = *.gz *.tgz *.zip *.z *.Z *.rpm *.deb *.bz2

    [test01]
    path = /root/tmp/test01/
    read only = yes

    [test02]
    path = /root/tmp/test02/
    read only = yes

`[test01]`一行以上的内容，与默认的配置无异，我们采用默认的配置即可.

然后在文件的最后加上以下配置。表示我们要启动两个提供同步的目录,分别命名为test01和test02，路径分别为`/root/tmp/test01/` 和 `/root/tmp/test02/`.

这里的test01 和 test02 在文档中叫做 `module name`,我们可以理解为"别名"、"alias"的意思即可.

read only = yes 表示客户端只能下载服务端的文件而不能上传(单向同步).
这应该是大部分业务的需求,如果有上传需要,设置read only = no 即可.

有一点需要提醒, `/etc/rsyncd.conf`配置修改后,并不需要重启服务即可生效.

如果想要关闭rsync服务,执行`ps -ef | pgrep rsync | xargs kill` 即可.

为了方便测试,我们还需要创建/root/tmp/test01/ 和 /root/tmp/test02/ 两个目录,然后在目录里面创建一些文件和目录,以便能看到同步下载的效果.

如果想要了解更多的配置和启动项，可以执行以下命令查看,这里不再赘言:

- `man rsyncd.conf` 查看更多文档
- 或者`rsync --daemon --help` 查看rsync的启动参数

rsync的默认端口是873, 如果服务器有防火墙限制,需要开放873端口:

    iptables -I INPUT -p tcp --dport 873 -j ACCEPT

如果服务器是部署在阿里云等云平台上，那可能还需要在云平台上调整安全组的出入网规则。


## 客户端操作(mac/linux)

测试一下命令(假设A的IP是192.168.1.100):

    rsync -r --list-only  192.168.1.100::test01
该命令中,

    -r 参数表示要递归同步目录下的目录.
    --list-only 参数表示只输出,不执行真正的文件传输.
    192.168.1.100 是服务器的IP，你可以替换成相应的域名.
    test01 就是我们配置中指定的module name, 请记住, test01前面是两个冒号.

如果能够列出服务器上test01对应的目录内容,则表示同步已经成功.

如果发生错误 `rsync: failed to connect to [你的服务器]: Operation timed out`，在检查网络正常的情况下,可能就是我们上面提到的防火墙问题。

执行同步命令:

    rsync -avP --delete --chmod=a=rwx 192.168.1.100::test01  ./tmpfolder
解释一下参数:

    --delete 表示删除本地tmpfolder目录中跟服务器test01下不一致的所有文件和目录
    --chmod=a=rwx 表示同步下来的文件具有a=rwx的权限(所有人可读写执行)
    ./tmpfolder 表示同步到本地的该目录下
    -P 表示显示进度条
    -v 表示采用增量的方式同步文件
    -a 是 archive mode; same as -rlptgoD; 相当于简写了很多参数
另外还有一些常见的参数说明:

    -u, --update      忽略客户端上(比服务端)更加新的文件
    -r, --recursive   递归同步目录
    -z, --compress    传输时压缩文件数据

在这里,我不使用`-z`参数是因为我要传输的文件主要是pdf和图片,所以该参数作用不大。
如果数据以文本为主, 那加上`-z`会好很多, 传输过程中数据量更少。


## windows下的解决方案

windows下有软件cwRsync提供了rsync的功能. [cwRsync的下载地址](http://static.extremevision.com.cn/membercms/cwRsync_5.4.1_x86_Free.zip?attname=)

安装步骤如下:

- 下载[cwRsync][cwRsyncPath]
- 解压得到的文件夹，将该文件夹加入到环境变量Path中, 比如`D:\cwRsync_5.4.1_x86_Free`。添加环境变量的方法可参考[这里][win-add-path]
- 建立文件夹存放同步的文件，比如`D:\pdf_and_album\`。
- 在`D:\cwRsync_5.4.1_x86_Free`中, 编写批处理脚本`pdf_rsync.bat`, 脚本内容如下面的"脚本1"。
- 设置windows的定时任务，执行`pdf_rsync.bat`。windows设置定时任务的方法见[Win XP][xp-add-cron], [Win 7][win7-add-cron]

脚本1内容就是我们上面提到的命令，比如:

    rsync -avP --delete --chmod=a=rwx rsync.bala.com::test01  /cygdrive/d/pdf_and_album/


[cwRsyncPath]: http://static.extremevision.com.cn/membercms/cwRsync_5.4.1_x86_Free.zip?attname=
[win-add-path]: http://www.dngsos.com/dngsdnjc/361.html
[xp-add-cron]: http://jingyan.baidu.com/article/d5c4b52bc3a11cda560dc5a7.html
[win7-add-cron]: http://jingyan.baidu.com/article/6181c3e0435026152ef153d0.html
