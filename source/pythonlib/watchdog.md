---
layout: pythonlib
toc: true
title: watchdog：监视文件/目录变化
date: 2018-02-27 00:00:00
---

### 简介

[Watchdog][github]是一个用来监视文件系统事件的Python库。它可以监视指定目录或文件的变化(添加、删除、修改、重命名)，每种变化都会产生一个事件，然后由事件处理类处理与之对应的事件。

本文只做Python库的简单介绍，更多API请参考[官方API文档][docs-api]。

### 安装

    pip install watchdog

### 示例

#### 代码例子

下面的例子中，指定目录发生的任何变化都会打印消息到终端。
由于`watchdog.observers.Observer`类继承自`threading.Thread`， 在不阻塞主线程的情况下，Observer线程负责处理文件目录发生变化产生的事件。


``` python
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

当一个目录或文件变化时，就会产生一个特定事件，所有的事件类以及其继承关系，功能如其名:

    watchdog.events.FileSystemEvent(src_path)
    |---watchdog.events.FileSystemMovedEvent(src_path, dest_path)
    |   |---watchdog.events.FileMovedEvent(src_path, dest_path)
    |   |---watchdog.events.DirMovedEvent(src_path, dest_path)
    |---watchdog.events.FileModifiedEvent(src_path)
    |---watchdog.events.DirModifiedEvent(src_path)
    |---watchdog.events.FileCreatedEvent(src_path)
    |---watchdog.events.DirCreatedEvent(src_path)
    |---watchdog.events.FileDeletedEvent(src_path)
    |---watchdog.events.DirDeletedEvent(src_path)

事件处理类以及其继承关系，功能如其名:

    watchdog.events.FileSystemEventHandler
    |---watchdog.events.PatternMatchingEventHandler(patterns=None, ignore_patterns=None, ignore_directories=False, case_sensitive=False)
    |---watchdog.events.RegexMatchingEventHandler(regexes=['.*'], ignore_regexes=[], ignore_directories=False, case_sensitive=False)
    |---watchdog.events.LoggingEventHandler

下面示例中，我们自定义了事件处理类FirstHandler，只处理文件名或目录名包含特定字符串的modified事件，并演示了如何添加多个事件处理类:

``` python
# -*- coding: utf-8 -*-
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FirstHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.find("demo") >= 0:
            print("only modified events can be recorded: {} changed!".format(event.src_path))


class SecondHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print("second handler for {}".format(event.src_path))


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    first_handler = FirstHandler()
    second_handler = SecondHandler()
    observer = Observer(timeout=1)
    watch = observer.schedule(first_handler, path=path, recursive=False)
    observer.add_handler_for_watch(second_handler, watch)
    # 调用另一次schedule也可达到相同目的
    # watch = observer.schedule(second_handler, path=path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

#### 命令行工具

Watchdog提供了一个命令行工具watchmedo，可以实现一些简单的处理文件系统事件的功能:
比如当某些文件改动时，打印日志:

    watchmedo log \
        --patterns="*.py;*.txt" \
        --ignore-directories \
        --recursive \
        .


比如当某些文件改动时，执行自定义命令:

    watchmedo shell-command \
        --patterns="*.py;*.txt" \
        --recursive \
        --command='echo "${watch_src_path}"' \
        ./

### More

* [一篇不错的中文博客][chinese-guide]
* [GitHub][github]
* [官方文档][docs]


[github]: https://github.com/gorakhargosh/watchdog
[docs]: https://pythonhosted.org/watchdog/quickstart.html
[docs-api]: https://pythonhosted.org/watchdog/api.html
[chinese-guide]: https://blog.csdn.net/chdhust/article/details/50514391
