---
layout: pythonlib
title: dateutil：datetime模块的扩展
toc: true
date: 2018-03-01 00:00:00
---

### 简介

Python中处理时间的第三方库有非常多，很多库的功能上有很大程度的重叠，我们完全没必要都掌握。
以我觉得最好用的[arrow][arrow]库来说，同类库就有:

* [Chronyk][Chronyk]
* [delorean][delorean]
* [maya][maya]
* [moment][moment]（对JavaScript的Moment.js熟练者可以考虑）
* [pendulum][pendulum]
* [PyTime][PyTime]
* [When.py][When.py]
* ...

个人观点，只需要掌握arrow即可，arrow是其中最流行、最好用的时间操作类库。

而本文中要讲的**[dateutil][dateutil]**，在功能上对arrow有所补充，提供了一些arrow不存在但有时却挺有用的功能。 事实上，arrow依赖于dateutil。
后面的例子中，也只讲一些dateutil比较有特色的功能，如果想了解更多，请移步[ReadTheDocs][readthedocs]。

另外，**[pytz][pytz]**是专注于世界时区的定义，包含了现代以及历史版本的时区数据库， 如果只是专注于时区的操作，pytz会是所有时间操作类库中的最佳选择。


### 安装

    pip install python-dateutil

### 示例

`dateutil.rrule` 模块提供了一个小而全，并且非常快速的[iCalendar RFC][icalendar]记录的重现规则的实现。

在示例的最开始，先声明几点:
* `dateutil.rrule.rrule` 方法的返回值是一个迭代器
* 周一到周日分别对应数字0-6: `byweekday=0`表示周一
* 周一到周日的简称分别是: MO, TU, WE, TH, FR, SA, SU


每年的 **母亲节** 是5月份的第二个星期天，打印2018年1月1日之后的10个母亲节:
``` python
>>> from datetime import datetime
>>> from dateutil.rrule import *
>>> list(rrule(YEARLY, count=10, bymonth=5, byweekday=SU(2),
... dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 5, 13, 0, 0), 
datetime.datetime(2019, 5, 12, 0, 0), 
datetime.datetime(2020, 5, 10, 0, 0),
......
datetime.datetime(2027, 5, 9, 0, 0)]
```


打印从2012年算起的 **美国总统选举日** ，也即每隔四年，在11月份的星期一之后的第一个周二:
``` python
>>> list(rrule(YEARLY, interval=4, count=3, bymonth=11, byweekday=TU,
... bymonthday=(2,3,4,5,6,7,8), dtstart=datetime(2012, 11, 6)))
[datetime.datetime(2012, 11, 6, 0, 0), 
datetime.datetime(2016, 11, 8, 0, 0), 
datetime.datetime(2020, 11, 3, 0, 0)]
```


从2018年1月1日开始，每隔3天，打印符合条件的3个日期:
``` python
>>> list(rrule(DAILY, interval=3, count=3, dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 1, 1, 0, 0), 
datetime.datetime(2018, 1, 4, 0, 0), 
datetime.datetime(2018, 1, 7, 0, 0)]
```


从2018年第一天开始，每隔15天，直到2018年3月1日，打印符合条件的全部日期:
``` python
>>> list(rrule(DAILY, interval=15, dtstart=datetime(2018, 1, 1),
... until=datetime(2018, 3, 1)))
[datetime.datetime(2018, 1, 1, 0, 0), 
datetime.datetime(2018, 1, 16, 0, 0), 
datetime.datetime(2018, 1, 31, 0, 0), 
datetime.datetime(2018, 2, 15, 0, 0)]
```


从2018年第一天开始，每隔两个月，每个月中的第一个和最后一个星期天，打印符合条件的10个日期:
``` python
>>> list(rrule(MONTHLY, interval=2, count=10, byweekday=(SU(1),SU(-1)),
... dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 1, 7, 0, 0), 
datetime.datetime(2018, 1, 28, 0, 0), 
......
datetime.datetime(2018, 9, 2, 0, 0), 
datetime.datetime(2018, 9, 30, 0, 0)]
```


2018年1月1日之后，包含有五个星期天的月份有哪些，打印符合条件的2个。从结果中可知，当年的4和7月份符合条件:
``` python
>>> list(rrule(MONTHLY, count=2, byweekday=(SU(5)), dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 4, 29, 0, 0), 
datetime.datetime(2018, 7, 29, 0, 0)]
```


每隔三年的第一天，第100天，第200天，打印符合条件的4个日期:
``` python
>>> list(rrule(YEARLY, count=4, interval=3, byyearday=(1,100,200),
... dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 1, 1, 0, 0), 
datetime.datetime(2018, 4, 10, 0, 0), 
datetime.datetime(2018, 7, 19, 0, 0), 
datetime.datetime(2021, 1, 1, 0, 0)]
```


每年的第20个星期一，打印符合条件的3个日期:
``` python
>>> list(rrule(YEARLY, count=3, byweekday=MO(20), dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 5, 14, 0, 0), 
datetime.datetime(2019, 5, 20, 0, 0), 
datetime.datetime(2020, 5, 18, 0, 0)]
```


打印2018年的所有单周的周六。有些工作是万恶的单双周，可以提前预约可约会的周六哟。其中，一年最多只能包含53个周，`range(1, 366/7+2, 2)`可以涵盖所有的单周:
``` python
>>> list(rrule(WEEKLY, byweekno=range(1, int(366/7+2), 2), byweekday=SA,
... dtstart=datetime(2018, 1, 1), until=datetime(2018, 12, 31)))
[datetime.datetime(2018, 1, 6, 0, 0), 
datetime.datetime(2018, 1, 20, 0, 0),
......
datetime.datetime(2018, 12, 8, 0, 0), 
datetime.datetime(2018, 12, 22, 0, 0)]
```


打印2018年之后，有53个周的最近3个年份:
``` python
>>> list(rrule(WEEKLY, count=3, byweekno=53, byweekday=MO, dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2020, 12, 28, 0, 0), 
datetime.datetime(2026, 12, 28, 0, 0), 
datetime.datetime(2032, 12, 27, 0, 0)]
```


2018年1月1日之后，每个月的第13天恰好是周五的4个日期:
``` python
>>> list(rrule(MONTHLY, count=4, byweekday=FR, bymonthday=13, dtstart=datetime(2018, 1, 1)))
[datetime.datetime(2018, 4, 13, 0, 0), 
datetime.datetime(2018, 7, 13, 0, 0), 
datetime.datetime(2019, 9, 13, 0, 0), 
datetime.datetime(2019, 12, 13, 0, 0)]
```


### More

更多文档和示例请参考:
* [ReadTheDocs][readthedocs]

### 其他扩展

* [arrow][arrow]: 通用的时间操作类库，但根据pendulum库在“[Why not Arrow?][why-not-arrow]”的举例对比，arrow在处理DST(夏令时)上有所缺陷。如果这对你的业务非常致命，可以考虑使用[pendulum][pendulum]库作为替代。
* [pytz][pytz]: 专注于世界时区的定义。


[readthedocs]: https://dateutil.readthedocs.io/en/stable/index.html
[arrow]: http://arrow.readthedocs.io/en/latest/#user-s-guide
[Chronyk]: https://github.com/KoffeinFlummi/Chronyk
[dateutil]: https://pypi.python.org/pypi/python-dateutil
[delorean]: https://github.com/myusuf3/delorean
[maya]: https://github.com/kennethreitz/maya
[moment]: https://github.com/zachwill/moment
[pendulum]: https://github.com/sdispater/pendulum
[PyTime]: https://github.com/shinux/PyTime
[When.py]: https://github.com/dirn/When.py
[pytz]: https://pypi.org/project/pytz/

[why-not-arrow]: https://github.com/sdispater/pendulum#why-not-arrow
[icalendar]: https://tools.ietf.org/html/rfc5545
