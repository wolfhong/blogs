---
layout: pythonlib
title: prettytable/PTable：绘制表格
toc: true
date: 2018-01-31 00:00:00
---

### 简介

prettytable/PTable是一个可以在终端快速绘制出漂亮表格的python库。也支持html格式的表格绘制。

原项目prettytable托管于[Google Code][google-code]，PTable是其在[GitHub][github]的一个fork，完全兼容prettytable。
完整的文档可参考[ReadTheDocs][readthedocs]，这里只做Python库的简单介绍。

最常用的示例:

``` python
    from prettytable import PrettyTable
    x = PrettyTable([u"城市名", u"面积", u"人口", u"年降雨量"])
    x.add_row(["Adelaide", 1295, 1158259, 600.5])
    x.add_row(["Brisbane", 5905, 1857594, 1146.4])
    x.add_row(["Darwin", 112, 120900, 1714.7])
    x.add_row(["Hobart", 1357, 205556, 619.5])
    x.add_row(["Sydney", 2058, 4336374, 1214.8])
    x.add_row(["Melbourne", 1566, 3806092, 646.9])
    x.add_row(["Perth", 5386, 1554769, 869.4])
    print(x)
```

输出(有些浏览器上查看时，可能稍微有些排版错位):

    +-----------+------+---------+----------+
    |   城市名   | 面积  |   人口   | 年降雨量  |
    +-----------+------+---------+----------+
    |  Adelaide | 1295 | 1158259 |  600.5   |
    |  Brisbane | 5905 | 1857594 |  1146.4  |
    |   Darwin  | 112  |  120900 |  1714.7  |
    |   Hobart  | 1357 |  205556 |  619.5   |
    |   Sydney  | 2058 | 4336374 |  1214.8  |
    | Melbourne | 1566 | 3806092 |  646.9   |
    |   Perth   | 5386 | 1554769 |  869.4   |
    +-----------+------+---------+----------+

### 安装

    pip install prettytable

### 示例

#### 添加行/列

上面已经演示了如何通过"row by row"的方式添加一行:

    x.add_row(["Perth", 5386, 1554769, 869.4])

也可以通过"column by column"的方式来添加一列:

    x.add_column(u"气温", [11, 12, 13, 14, 15, 16, 17])

#### 删除行

删除table中的数据的方式有三种:

`del_row` 参数为一个数字index，可以删除指定row，数字从0开始算:

    x.del_row(0)  

`clear_rows` 删除所有row，但保留table的字段名:

    x.clear_rows()

`clear` 删除所有row和table的字段名，但保留table的样式:

    x.clear()

#### 从CSV文件导入数据

``` python
    from prettytable import from_csv

    with open("myfile.csv", "r") as fp:
        mytable = from_csv(fp)
```

#### 从数据库导入数据

``` python
    import sqlite3
    from prettytable import from_cursor

    connection = sqlite3.connect("mydb.db")
    cursor = connection.cursor()
    cursor.execute("SELECT field1, field2, field3 FROM my_table")
    mytable = from_cursor(cursor)
```

#### 打印输出

    print(x)

或者:

    print(x.get_string())

使用`get_string()`可以带入参数，比如只想要输出某些列:

    print(x.get_string(fields=[u"城市名", u"人口"]))

只想要输出某些行:

    print(x.get_string(start=1, end=4))

#### 输出对齐

``` python
    x.align[u"城市名"] = "l"
    x.align[u"面积"] = "c"
    x.align[u"人口"] = "r"
    x.align[u"年降雨量"] = "c"
    print(x)
```
其中，`l`表示`left`, `r`表示`right`，`c`表示`center`。默认是`c`居中的对齐方式。


#### 表格排序

``` python
    print(x.get_string(sortby=u"人口", reversesort=True))
```

输出(有些浏览器上查看时，可能稍微有些排版错位):

    +-----------+------+---------+----------+
    |   城市名   | 面积  |   人口   | 年降雨量  |
    +-----------+------+---------+----------+
    |   Sydney  | 2058 | 4336374 |  1214.8  |
    | Melbourne | 1566 | 3806092 |  646.9   |
    |  Brisbane | 5905 | 1857594 |  1146.4  |
    |   Perth   | 5386 | 1554769 |  869.4   |
    |  Adelaide | 1295 | 1158259 |  600.5   |
    |   Hobart  | 1357 |  205556 |  619.5   |
    |   Darwin  | 112  |  120900 |  1714.7  |
    +-----------+------+---------+----------+

#### 输出html

``` python
    print(x.get_html_string())
```

支持html样式（比如在邮件中插入html代码会用到）:

``` python
    print(x.get_html_string(attributes={"class":"red_table", "border": "1"}))
```

### More

文档与更多示例参考:
* [ReadTheDocs][readthedocs]
* [Python Code Example][python-code-example]
* [Pypi][pypi]
* [Google Code][google-code]
* [GitHub][github]

[google-code]: https://code.google.com/archive/p/prettytable/
[github]: https://github.com/kxxoling/PTable
[readthedocs]: https://ptable.readthedocs.io/en/latest/
[pypi]: https://pypi.org/project/PTable/
[python-code-example]: https://www.programcreek.com/python/example/58616/prettytable.PrettyTable
