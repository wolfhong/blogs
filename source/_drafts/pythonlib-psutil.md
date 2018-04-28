
### 简介

psutil (process and system utilities的缩写) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. It implements many functionalities offered by UNIX command line tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty,
taskset, pmap. psutil currently supports the following platforms:

是一个跨平台的库，用于检索Python中正在运行的进程和系统利用率（CPU，内存，磁盘，网络，传感器）的信息。
它主要用于系统监视，分析和限制流程资源以及运行流程的管理。 它实现了UNIX命令行工具提供的许多功能，例如：ps，top，lsof，netstat，ifconfig，who，df，kill，free，nice，ionice，iostat，iotop，uptime，pidof，tty，taskset，pmap。 psutil目前支持以下平台：

Linux
Windows
OSX,
FreeBSD, OpenBSD, NetBSD
Sun Solaris
AIX

十分成熟，facebook和google等公司的开源项目也都有使用到。

### 安装

    pip install psutil


psutil:  对CPU、磁盘、内存、网络、传感器（电池、风扇等硬件信息）等指标获取，进程信息获取和进程设置等。对多种操作系统进行封装了。


### 示例



[github]: https://github.com/giampaolo/psutil
[readthedocs]: http://psutil.readthedocs.io/en/latest/
