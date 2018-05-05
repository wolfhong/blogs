---
layout: pythonlib
title: psutil：系统监测与进程管理
toc: true
date: 2018-02-01 00:00:00
---

### 简介

[psutil][github] (process and system utilities的缩写) 是一个跨平台的Python库，可以获取到运行中的进程信息和系统状态（比如CPU，内存，磁盘，网络，传感器），主要用于系统监测，进程资源的分析和限制，进程管理等。

**psutil** 实现了很多UNIX命令工具的功能，诸如: ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap.

**psutil** 支持的操作系统涵盖了现在的主流: Linux, Windows, OSX, FreeBSD, OpenBSD, NetBSD, Sun Solaris, AIX. **psutil** 实现了对多种操作系统的统一接口封装，但有些方法和属性仅对特定操作系统有意义。

完整的文档可参考[ReadTheDocs][readthedocs]，这里只做Python库的简单介绍。

### 安装

    pip install psutil

### 示例

诸如CPU，内存，磁盘，网络，硬件信息等常见的系统状态，**psutil**通通都可以监测到。下面是一些代码示例，仅仅展示了全部功能中的一部分。

#### CPU

``` python
# -*- coding: utf-8 -*-
import psutil

print(psutil.cpu_times())
print(psutil.cpu_times(percpu=True))
'''
各模式的cpu时间消耗: 
scputimes(user=26364.73, nice=0.0, system=14061.69, idle=261071.34)
每个cpu,各模式的cpu时间消耗: 
[scputimes(user=10182.09, nice=0.0, system=6139.7, idle=59054.21), ...]
'''

print(psutil.cpu_times_percent(interval=1))
print(psutil.cpu_times_percent(interval=1, percpu=True))
'''
各模式cpu时间占比: 
scputimes(user=2.2, nice=0.0, system=0.7, idle=97.0)
每个cpu,各模式的cpu占比: 
[scputimes(user=5.0, nice=0.0, system=3.0, idle=92.0), ...]
'''

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
'''
CPU的个数(逻辑上的): 4
CPU的个数(物理上的): 2
'''

print(psutil.cpu_stats())
'''
上下文切换,硬件中断,软件中断,系统调用次数: 
scpustats(ctx_switches=7943, interrupts=189022, soft_interrupts=141954044, syscalls=292696)
'''

print(psutil.cpu_freq())
'''
cpu频率(当前/最大/最小)，仅Linux, OSX, Windows支持:
scpufreq(current=1300, min=1300, max=1300)
'''
```

#### Memory

``` python
# -*- coding: utf-8 -*-
import psutil

print(psutil.virtual_memory())
'''
内存使用状况: 
svmem(total=10367352832, available=6472179712, percent=37.6, used=8186245120, free=2181107712,
active=4748992512, inactive=2758115328, buffers=790724608, cached=3500347392, shared=787554304)
'''

print(psutil.swap_memory())
'''
swap使用状况: 
sswap(total=2097147904, used=296128512, free=1801019392, percent=14.1, sin=304193536, sout=677842944)
'''
```

#### 磁盘

``` python
# -*- coding: utf-8 -*-
import psutil

print(psutil.disk_partitions())
'''
磁盘分区信息: 
[sdiskpart(device='/dev/sda1', mountpoint='/', fstype='ext4', opts='rw,nosuid'),
sdiskpart(device='/dev/sda2', mountpoint='/home', fstype='ext, opts='rw')]
'''

print(psutil.disk_usage('/'))
'''
磁盘使用状况: 
sdiskusage(total=21378641920, used=4809781248, free=15482871808, percent=22.5)
'''

print(psutil.disk_io_counters(perdisk=False))
'''
磁盘I/O: 
sdiskio(read_count=719566, write_count=1082197, read_bytes=18626220032,
write_bytes=24081764352, read_time=5023392, write_time=63199568, read_merged_count=619166,
write_merged_count=812396, busy_time=4523412)
'''
```

#### 网络

``` python
# -*- coding: utf-8 -*-
import psutil

print(psutil.net_io_counters(pernic=True))
'''
每个网卡的I/O统计信息:
{'eth0': netio(bytes_sent=485291293, bytes_recv=6004858642, packets_sent=3251564,
 packets_recv=4787798, errin=0, errout=0, dropin=0, dropout=0),
'lo': netio(bytes_sent=2838627, bytes_recv=2838627, packets_sent=30567,
 packets_recv=30567, errin=0, errout=0, dropin=0, dropout=0)}
'''

print(psutil.net_connections())
'''
网络连接情况(主要是TCP连接):
[sconn(fd=115, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>,
 laddr=addr(ip='10.0.0.1', port=48776), raddr=addr(ip='93.186.135.91',
 port=80), status='ESTABLISHED', pid=1254),
sconn(fd=117, family=<AddressFamily.AF_INET: 2>, type=<SocketType.SOCK_STREAM: 1>,
 laddr=addr(ip='10.0.0.1', port=43761), raddr=addr(ip='72.14.234.100', port=80),
 status='CLOSING', pid=2987),
 ...]
'''

print(psutil.net_if_addrs())
'''
网络地址信息:
{'wlan0': [snic(family=<AddressFamily.AF_INET: 2>, address='192.168.1.3', netmask='255.255.255.0', broadcast='192.168.1.255', ptp=None),
 snic(family=<AddressFamily.AF_INET6: 10>, address='fe80::c685:8ff:fe45:641%wlan0', netmask='ffff:ffff:ffff:ffff::', broadcast=None, ptp=None),
 snic(family=<AddressFamily.AF_LINK: 17>, address='c4:85:08:45:06:41', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}
'''

print(psutil.net_if_stats())
'''
网卡状态:
{'eth0': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500),
 'lo': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_UNKNOWN: 0>, speed=0, mtu=65536)}
'''
```

#### 传感器(硬件信息)

``` python
# -*- coding: utf-8 -*-
import psutil

print(psutil.sensors_temperatures())
'''
各硬件温度,仅Linux支持:
{'acpitz': [shwtemp(label='', current=47.0, high=103.0, critical=103.0)],
 'asus': [shwtemp(label='', current=47.0, high=None, critical=None)],
 'coretemp': [shwtemp(label='Physical id 0', current=52.0, high=100.0, critical=100.0),
              shwtemp(label='Core 0', current=45.0, high=100.0, critical=100.0),
              shwtemp(label='Core 1', current=52.0, high=100.0, critical=100.0),
              shwtemp(label='Core 2', current=45.0, high=100.0, critical=100.0),
              shwtemp(label='Core 3', current=47.0, high=100.0, critical=100.0)]}
'''

print(psutil.sensors_fans())
'''
硬件风扇信息,仅Linux支持:
{'asus': [sfan(label='cpu_fan', current=3200)]}
'''

print(psutil.sensors_battery())
'''
电池信息,仅Linux, Windows, FreeBSD支持:
sbattery(percent=93, secsleft=16628, power_plugged=False)
'''
```

#### 其他系统信息

``` python
# -*- coding: utf-8 -*-
import psutil

print(psutil.users())
'''
登录用户:
[suser(name='giampaolo', terminal='pts/2', host='localhost', started=1340737536.0, pid=1352),
 suser(name='giampaolo', terminal='pts/3', host='localhost', started=1340737792.0, pid=1788)]
'''

print(psutil.boot_time())
'''
开机时间: 1365519115.0
'''
```

#### 进程管理

对进程的管理是**psutil**的一大模块，这里只挑选了极少数的例子。更多例子请参考[GitHub][github]上的例子。

``` python
# -*- coding: utf-8 -*-
import psutil

p = psutil.Process(7055)
print(p.name())
print(p.exe())
print(p.cmdline())
print(p.status())
print(p.cpu_times())

'''
对应输出:
'python'
'/usr/bin/python'
['/usr/bin/python', 'main.py']
'running'
pcputimes(user=1.02, system=0.31, children_user=0.32, children_system=0.1)
'''

print(p.nice())  # get进程优先级
p.nice(10)  # set进程优先级

```


### More 

文档与更多示例参考:
* [ReadTheDocs][readthedocs]
* [更多示例][examples]
* [GitHub][github]

### 其他扩展

[Diamond][diamond]是一个python写的守护程序，它可以收集系统指标（cpu, 内存, 网络，I/O, 负载, 硬盘指标）, 并把它们发送至Graphite或其它后端。此外，通过它可以实现自定义的收集器，采集你想要的任何资源指标。
考虑到现在有[Prometheus][prometheus]等更加大众的解决方案，这里就稍微提及而已。


[github]: https://github.com/giampaolo/psutil
[readthedocs]: https://psutil.readthedocs.io/en/latest/
[examples]: https://psutil.readthedocs.io/en/latest/#recipes
[diamond]: https://github.com/python-diamond/Diamond
[prometheus]: https://prometheus.io/
