---
title: Mac下挂载远程目录到本地
date: 2016-11-16 01:06:50
categories:
- 其他
tags:
- sshfs
- mac
---

挂载远程目录到本地，目的是希望能够跟查看本地文件一样，可以方便地浏览远程目录下的文件。

sshfs就是能够满足这项需求的程序，不仅适用于ubuntu/centos等linux系统，也同样适用于Mac。

以Mac为例，使用brew安装sshfs

    brew install sshfs

brew是Mac下十分常见的套件管理工具, 如果你的电脑没有安装该程序, 请参考[Homebrew](http://brew.sh/index_zh-cn.html)进行安装。

安装过程中, 你可能会遇到如下的错误:

    sshfs: OsxfuseRequirement unsatisfied!
    Error: An unsatisfied requirement failed this build.

![image01](http://static.extremevision.com.cn/membercms/sshfs/mac_sshfs_error01.png)

只需要按照提示一步一步操作即可.

先执行`brew cask install osxfuse`. 该过程实际上是去github下载安装`osxfuse.dmg`.

安装好osxfuse后，按照提示需要重启电脑(不过我试过了，不重启电脑也是可以的)。

这时候再来重新执行`brew install sshfs`即可.

安装sshfs结束后, 就可以使用`sshfs`挂载远程目录到本地：

    sshfs -C -o reconnect <user>@<host>:<remote_dir> <local_dir>

比如,我想要将远程主机192.168.1.101上的`/mnt/images/`目录，挂载到本地`~/Desktop/images/`目录下。过程中使用root账号登陆.

    sshfs -C -o reconnect root@192.168.1.101:/mnt/images/ ~/Desktop/images/

如果ssh不是默认的22端口,则还需要带上选项: `-p <端口号>`

挂载到本地时, 请避免挂载在根目录，或者当前角色的主目录下, 会报错。比如如下的错误操作:

    mkdir ~/ImageFolder
    sshfs -C -o reconnect root@192.168.1.101:/mnt/images/ ~/ImageFolder/

会看到错误提示:

    mount_osxfuse: mount point /Users/xxxx/ImageFolder is itself on a OSXFUSE volume
    fuse: failed to mount file system: Invalid argument
