---
layout: pythonlib
title: selenium：操作浏览器冲浪
toc: true
date: 2018-02-03 00:00:00
---

### 简介

Selenium的用处非常广泛，诸如网络监测、网页拨测、网页截屏、无需浏览器的Web测试、页面访问自动化等都可以实现。 简单概括就是，你在浏览器上能做的事情，它几乎都可以完成。它可以模拟你来操作网页，包括鼠标、键盘、触摸等事件，也支持执行JS脚本。

Selenium官方将自己定位为“浏览器自动化框架和生态系统”。

Selenium由[多个组件][wiki]组成，包括:
* Selenium IDE
* Selenium Client API
* Selenium WebDriver
* Selenium Remote Control
* Selenium Grid

#### Selenium IDE

Selenium IDE是一个用于Selenium测试的完整集成开发环境（IDE）, 它作为浏览器插件被实现出来，集成了录制、播放、编辑、调试等功能，还可以导出多种语言的Selenium脚本。 有Selenium IDE的辅助，你可以录制你在浏览器上的操作，然后导出代码，以便以后重演。
Selenium IDE目前有火狐和Chrome版本的插件，可以在[官网下载页面][seleniumhq]上下载到。

后面的"其他扩展"中还会提到一个非官方的Selenium IDE: *Katalon Recorder*，有兴趣可以了解下。

<center>**Chrome浏览器上执行录制功能**</center>
![image](/images/selenium-chrome.png)

<center>**Firefox浏览器上执行导出代码**</center>
![image](/images/selenium-firefox.png)


#### Selenium Client API

Selenium测试也可以用各种编程语言编写，这些测试通过调用Selenium Client API中的方法与Selenium进行通信。后面的"示例"，就是使用Python语言，调用Selenium Client API，从而发送指令给Selenium WebDriver，进而操作浏览器。

其他组成部分省略不讲，这里只做Python库的简单介绍。

### 安装
    pip install selenium

### 示例

#### 一个常见的示例

下面示例中，Selenium将打开火狐浏览器，访问 *http://www.python.org* 网址，断言"Python"字符串会出现在网页的标题上。接着找到 *name="q"* 的搜索框，在搜索框中输入"pycon"字符串，按下回车键，断言"No results found."不会出现在刷新的页面中。

``` python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
```

#### 运行JavaScript代码

如果需要在浏览器中执行JavaScript代码，可以使用`execute_script`方法。比如，需要将滚动条滚动到页面最下方时，可以参考如下示例:

``` python
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```

#### remote WebDriver

如果需要在远程运行WebDriver，在另一台电脑上调用Client API，可以参考如下示例。

在服务器端执行:

    java -jar selenium-server-standalone-2.x.x.jar

如果执行成功，将看到类似的输出:

    15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub

之后，客户端就可以采用如下示例来调用remote WebDriver:

``` python
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.CHROME)

    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.OPERA)

    driver = webdriver.Remote(
       command_executor='http://127.0.0.1:4444/wd/hub',
       desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
```


### More

文档与更多示例参考:
* [GitHub][github]
* [ReadTheDocs英文文档][readthedocs]
* [ReadTheDocs中文文档][readthedocs-zh](质量取决于翻译者)
* [Official Docs][official-docs]

### 其他扩展

#### PhantonJS

[PhantomJS][phantonjs]是一个基于webkit的JavaScript API。 它使用QtWebKit作为它核心浏览器的功能，使用webkit来编译解释执行JavaScript代码。 任何你可以在基于webkit浏览器做的事情，它都能做到。它是个隐形的浏览器，提供了诸如CSS选择器、支持Web标准、DOM操作、JSON、HTML5、Canvas、SVG等。
PhantomJS的应用场景与Selenium类似，有兴趣的可以了解并对比两者。

#### Katalon Recorder

Katalon Studio公司推出了自己的Selenium IDE，作为Chrome浏览器的插件实现，Firefox上暂时没有实现。
**Katalon Recorder**可以从[Chrome Store][katalon]上下载到。
Katalon Studio将其定位为最好用的Selenium IDE，实现了录制、播放、debug、快速导出到Selenium WebDriver脚本等功能。
个人觉得，**Katalon Recorder**的确比官方的**Selenium IDE**好用，有兴趣可以试试。

#### marionette-client

[marionette-client][marionette-client]允许您远程控制基于Gecko的浏览器或运行Marionette服务器的设备。  这包括Firefox桌面和Android版Firefox。


[wiki]: https://en.wikipedia.org/wiki/Selenium_(software)
[github]: https://github.com/SeleniumHQ/selenium
[readthedocs]: https://selenium-python.readthedocs.io/getting-started.html
[readthedocs-zh]: https://python-selenium-zh.readthedocs.io/zh_CN/latest/
[official-docs]: https://docs.seleniumhq.org/docs/

[seleniumhq]: https://www.seleniumhq.org/download/
[phantonjs]: http://phantomjs.org/quick-start.html
[katalon]: https://chrome.google.com/webstore/detail/katalon-recorder-selenium/ljdobmomdgdljniojadhoplhkpialdid
[marionette-client]: http://marionette-client.readthedocs.io/en/master/

[mygit]: https://github.com/wolfhong/pisces
[katalon-mygist]: https://gist.github.com/wolfhong/3a861560b56a251b3d7d4beda2faeaf6
