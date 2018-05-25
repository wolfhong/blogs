---
title: Python每日一库哟
categories:
  - 其他
date: 2018-05-02 22:53:17
---

<br>
本专题"Python每日一库哟"，每天介绍一个好用的Python库，包括标准库和第三方库。
本专题适合那些有一定Python基础的人，可通过该专题，涉猎更多Python能做的事。
希望你在无聊之余阅读后，能在以后的工作中遇到相关问题时，会突然蹦出解决问题的灵感。

专题中，每篇文章只是做简单的介绍，并非文档；有些甚至只是网络资源的链接。
这里仅仅做了科普入门，如果有需要深入了解，还是需要参考相应的文档，或者搜索其他人的文章。

专题中，默认你是在Linux或者Mac下编程，如果你使用Windows编程，安装时如果遇到问题，一般可参考文章中的GitHub或者ReadTheDocs链接，会得到解答。

* [prettytable/PTable](./prettytable.html): 在终端绘制表格
* [psutil](./psutil.html): 系统监测与进程管理
* [livereload](./livereload.html): 监视文件改动与web开发利器
* [selenium](./selenium.html): 操作浏览器冲浪与web自动化测试
* [virtualenvwrapper/virtualenv](./virtualenvwrapper.html): 隔离的虚拟环境
* [requests][requests]: 最好用的HTTP库
* [pycodestyle/pep8](./pycodestyle.html): Python代码风格检查器, 类比: flake8, pylint, pylama
* [autopep8/yapf](./autopep8.html): Python代码的格式化工具, 类比: yapf, pep8ify
* [tablib](./tablib.html): 导出表格数据, 支持excel, yaml, json, pandas等
* [formic](./formic.html): 快速查找文件, 类比: glob, fnmatch
* [anaconda](./anaconda.html): 数据科学领域的开发工具, 类比: pip, virtualenv
* [python-magic](./python-magic.html): 文件类型识别, 类比: imghdr
* [watchdog](./watchdog.html): 监视文件/目录变化, 类比: livereload
* [arrow][arrow]: 节省脑力的时间库，其他第三方时间操作类库都可以不用再看了
* [dateutil](./dateutil.html): datetime模块的扩展, 补充arrow没有的功能
* [chardet][chardet]: 检测字符编码
* [ftfy](./ftfy.html): Unicode的转化(如恢复乱码，全角符转半角符等)

* [fuzzywuzzy][fuzzywuzzy]: 模糊字符串匹配，匹配有多种模式，如`ratio`，`partial_ratio`，`token_sort_ratio`，`token_set_ratio`
  使用了[Levenshtein Distance](https://en.wikipedia.org/wiki/Levenshtein_distance)算法。
  使用`pip install fuzzywuzzy[speedup]`安装时会安装python-Levenshtein依赖，可以优化性能。
* [python-Levenshtein][python-Levenshtein]: 字符串相似度计算。[文档](https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html)
* [shortuuid][shortuuid]: 生成简洁明了，URL安全的UUID
* [Unidecode][Unidecode]: Unicode文本的ASCII转换形式，如URL的slug化，全角转半角，中文转拼音等。
* [pypinyin](https://github.com/mozillazg/python-pinyin): 汉字转拼音
* [xpinyin](https://github.com/lxneng/xpinyin): 也是将汉字转拼音，但是更新不活跃了，不比pypinyin库。
* [pyfiglet](https://github.com/pwaller/pyfiglet): 在终端用字符拼成单词
  [所有字体的展示效果](https://gist.github.com/wolfhong/2bf308ba727cfbc92f8edaee30cb9eef)
  [所有字体文件](https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts)
* [python-phonenumbers][phonenumbers]: 解析，格式化，验证多国家电话号码。可获取所在地，代理商，时区等信息
* [python-user-agents](https://github.com/selwin/python-user-agents): 浏览器UserAgent解析器，可判断pc/tablet/mobile/robot，是否可触屏。

* [PLY](http://www.dabeaz.com/ply/): lex(词法分析) 和 yacc(语法分析) 解析工具的Python实现。官网上链接了其他Python实现的语法工具。
* [pyparsing](http://pyparsing.wikispaces.com/): 可以生成通用的语法解析器的框架。
* [Pygments](http://pygments.org/): 基于html的通用语法高亮工具，支持很多种语言。

* [openpyxl][openpyxl]: 支持Microsoft Excel 2010的读写。支持图标、只读只写、样式、单元格验证、文件保护等Excel功能。
* [xlwt, xlrd, xlutils][python-excel-all]: xlwt(只写)和xlrd(只读)和xlutils(封装前两者)在使用上过时了，只支持到了Excel 2003。推荐使用openpyxl。
* [python-docx](https://github.com/python-openxml/python-docx): 对Microsoft Word documents的读写。
* [PDFMiner](https://github.com/euske/pdfminer): 一个用于从 PDF 文档中抽取信息的工具。
* [PyPDF2](https://github.com/mstamy2/PyPDF2): 一个可以分割，合并和转换 PDF 页面的库。
* [ReportLab](http://www.reportlab.com/opensource/)：快速创建富文本 PDF 文档。

* [mistune](https://github.com/lepture/mistune): Markdown 解析器。类比[pandoc][https://github.com/jgm/pandoc]
* [csvkit](https://github.com/wireservice/csvkit): 用于转换和操作 CSV 的工具，对 CSV 执行 SQL 查询


* [unp](https://github.com/mitsuhiko/unp): 整合各种解压归档文件的命令行工具
* [click](https://github.com/pallets/click): 可组合的命令行工具
* [pint](https://github.com/hgrecco/pint): 物理量的转换，类比[units](https://pypi.org/project/units/), [quantities](https://github.com/python-quantities/python-quantities)
* [langid](https://github.com/saffsd/langid.py): 独立的语言识别系统




[requests]: http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
[arrow]: http://arrow.readthedocs.io/en/latest/#user-s-guide
[chardet]: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001510905171877ca6fdf08614e446e835ea5d9bce75cf5000
[fuzzywuzzy]: https://github.com/seatgeek/fuzzywuzzy
[python-Levenshtein]: https://pypi.org/project/python-Levenshtein/
[shortuuid]: https://github.com/skorokithakis/shortuuid
[Unidecode]: https://pypi.org/project/Unidecode/
[phonenumbers]: https://zhuanlan.zhihu.com/p/24852734

[openpyxl]: https://openpyxl.readthedocs.io/en/latest/
[xlwt]: https://github.com/python-excel/xlwt
[xlrd]: https://github.com/python-excel/xlrd
[xlutils]: https://github.com/python-excel/xlutils
[python-excel-all]: https://github.com/python-excel/
