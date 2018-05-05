---
layout: pythonlib
title: tablib
toc: true
date: 2018-02-06 08:00:00
---

### 简介

对于经常要处理表格数据的开发者而言，[Tablib][github]一定会是你的福音。
Tablib是`a format-agnostic tabular dataset library`，由于翻译很拗口，简单来说，Tablib可以在内存中处理表格数据，然后导出成各式各样的文件格式。
支持导出的文件格式包括:

* Excel (Sets + Books)
* JSON (Sets + Books)
* YAML (Sets + Books)
* Pandas DataFrames (Sets)
* HTML (Sets)
* TSV (Sets)【[Tab-separated values][tsv-wiki]】
* ODS (Sets)【ODS is a spreadsheet file format used by OpenOffice/StarOffice】
* CSV (Sets)
* DBF (Sets)【.dbf后缀的文件是dBase database file】

### 安装

    pip install tablib[pandas]

### 示例

Tablie有两种数据类型: `tablib.Dataset()` 和 `tablib.Databook()`。
Dataset可以理解为table表，表头可以省略。
Databook可以理解为一系列的Dataset，类比为一个Excel文件可以包含多个Sheets。

#### 代码示例

``` python
    headers = ('first_name', 'last_name')

    data = [
        ('John', 'Adams'),
        ('George', 'Washington')
    ]

    data = tablib.Dataset(*data, headers=headers)
    data.append(('Henry', 'Ford'))  # add row
    data.append_col((90, 67, 83), header='age')  # add column

    print(data[:2])
    # output: [('John', 'Adams', 90), ('George', 'Washington', 67)]

    print(data['first_name'])
    # output: ['John', 'George', 'Henry']

    del data[1]  # delete rows
```

#### 导出JSON

``` python
>>> print(data.export('json'))
[
  {
    "last_name": "Adams",
    "age": 90,
    "first_name": "John"
  },
  {
    "last_name": "Ford",
    "age": 83,
    "first_name": "Henry"
  }
]
```

#### 导出YAML

``` python
>>> print(data.export('yaml'))
- {age: 90, first_name: John, last_name: Adams}
- {age: 83, first_name: Henry, last_name: Ford}
```

#### 导出CSV

``` python
>>> print(data.export('csv'))
first_name,last_name,age
John,Adams,90
Henry,Ford,83
```

#### 导出Excel

支持XLS和XLSX格式。

``` python
>>> with open('people.xls', 'wb') as f:
...     f.write(data.export('xls'))
```

``` python
>>> with open('people.xlsx', 'wb') as f:
...     f.write(data.export('xlsx'))
```
如果导出xlsx格式时发生诸如`TypeError: cell() missing 1 required positional argument: 'column'`的错误，可参考[issue#324][issue324] 和[stackoverflow上的回答][stackoverflow]。

#### 导出DBF

``` python
>>> with open('people.dbf', 'wb') as f:
...     f.write(data.export('dbf'))
```

#### 导出Pandas DataFrames

``` python
>>> print(data.export('df'))
      first_name last_name  age
0       John     Adams   90
1      Henry      Ford   83
```

#### 导出ODS

``` python
>>> with open('people.ods', 'wb') as f:
...     f.write(data.export('ods'))
```

### More

文档与更多示例参考:
* [GitHub][github]
* [Official Docs][official-docs]


[github]: https://github.com/kennethreitz/tablib
[official-docs]: http://python-tablib.org/
[issue324]: https://github.com/kennethreitz/tablib/issues/324
[stackoverflow]: https://stackoverflow.com/questions/48598092/python-3-5-3-6-tablib-typeerror-cell-missing-1-required-positional-argumen

[tsv-wiki]: https://en.wikipedia.org/wiki/Tab-separated_values
[issue330]: https://github.com/kennethreitz/tablib/issues/330
