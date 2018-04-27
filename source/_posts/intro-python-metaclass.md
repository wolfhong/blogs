---
title: 理解python的metaclass
date: 2016-10-24 00:59:41
toc: true
categories:
- python
tags:
- python
- 翻译
---

## 前言

这篇博客是我在stackoverflow上看了一个提问回复后写的,例子基本用的都是e-satis本人的例子，语言组织也基本按照翻译来。

但我并不是一个翻译者,并不会严格遵守每行每句的翻译;
有时候我会将表述换个顺序,省略一些我认为无关紧要的话，以便读者更好理解。

所以，如果你不喜欢我的语言表述，或者想要看英文原文，可以去查看[原回复][source]。

## 类也是对象

在理解metaclass之前，我们先要掌握python中的类`class`是什么。
python中类的概念，是借鉴自smalltalk语言。
在大部分语言中，类指的是"描述如何产生一个对象(object)"的一段代码，这对于python也是如此。

``` python
>>> class ObjectCreator(object):
...     pass
...
>>> my_object = ObjectCreator()
>>> print(my_object)
<__main__.ObjectCreator object at 0x8974f2c>
```

但是,在python中，类远不止如此，类同时也是对象。
当你遇到关键词`class`的时候，python就会自动执行产生一个对象。下面的代码段中:

``` python
>>> class ObjectCreator(object):
...     pass
...
```

python在内存中产生了一个名叫做"ObjectCreator"的对象。这个对象(类)自身拥有产生对象(实例instance)的能力。 这就是为什么称呼这东西(后面遇到容易混淆的地方,我们称之为:类对象)也是类的原因。同时，它也是一个对象，因此你可以对它做如下操作:

- 赋值给变量
- 复制它
- 为它增加属性(attribute)
- 作为参数传值给函数

举例：

``` python
>>> print(ObjectCreator) # 你可以打印一个类,因为它同时也是对象
<class '__main__.ObjectCreator'>

>>> def echo(o):
...     print(o)
...
>>> echo(ObjectCreator) # 作为参数传值给函数
<class '__main__.ObjectCreator'>

>>> print(hasattr(ObjectCreator, 'new_attribute'))
False
>>> ObjectCreator.new_attribute = 'foo' # you can add attributes to a class
>>> print(hasattr(ObjectCreator, 'new_attribute'))
True
>>> print(ObjectCreator.new_attribute)
foo

>>> ObjectCreatorMirror = ObjectCreator # 将类赋值给变量
>>> print(ObjectCreatorMirror.new_attribute)
foo
>>> print(ObjectCreatorMirror())
<__main__.ObjectCreator object at 0x8997b4c>
```


## 动态创建类

既然类也是对象，那么我们就可以在运行的时候创建它，跟创建对象一样自然。

首先，我们使用`class`关键字定义一个产生类的函数:

``` python
>>> def choose_class(name):
...     if name == 'foo':
...         class Foo(object):
...             pass
...         return Foo # return the class, not an instance
...     else:
...         class Bar(object):
...             pass
...         return Bar
...
>>> MyClass = choose_class('foo')
>>> print(MyClass) # the function returns a class, not an instance
<class '__main__.Foo'>
>>> print(MyClass()) # you can create an object from this class
<__main__.Foo object at 0x89c6d4c>
```

这很容易理解吧。但是，这并不那么动态啊。我们还是需要自己来写这个类的代码。

既然类也是对象，那就应该有用来产生它的东西。这东西就是`type`。

先来说说你所认识的`type`。这个古老而好用的函数，可以让我们知道一个对象的类型是什么。

``` python
>>> print(type(1))
<type 'int'>
>>> print(type("1"))
<type 'str'>
>>> print(type(ObjectCreator))
<type 'type'>
>>> print(type(ObjectCreator()))
<class '__main__.ObjectCreator'>
```

实际上，`type`还有一个完全不同的功能，它可以在运行时产生类。`type`可以传入一些参数，然后返回一个类。(好吧，必须承认，根据不同的传入参数，一个相同的函数`type`居然会有两个完全不同的作用，这很愚蠢。不过python这样做是为了保持向后兼容性。)

下面举例`type`创建类的用法。首先，对于类一般是这么定义的:

``` python
>>> class MyShinyClass(object):
...     pass

在下面，MyShinyClass也可以这样子被创建出来,并且跟上面的创建方法有一样的表现:

>>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # create an instance with the class
<__main__.MyShinyClass object at 0x8997cec>
```

`type`创建类需要传入三个参数,分别为:

- 类的名字
- 一组"类的父类"的元组(tuple) (这个会实现继承,也可以为空)
- 字典 (类的属性名与值,key-value的形式，不传相当于为空，如一般写法中的pass).

下面来点复杂的，来更好的理解`type`传入的三个参数:

``` python
class Foo(object):
    bar = True

    def echo_bar(self):
        print(self.bar)
```

等价于:

``` python
def echo_bar(self):
    print(self.bar)

Foo = type('Foo', (), {'bar':True, 'echo_bar': echo_bar})
```

想要看点有继承关系的类的实现,来:

``` python
class FooChild(Foo):
    pass
```

等价于:

``` python
FooChild = type('FooChild', (Foo, ), {})
```

回顾一下我们学到哪了: 在python中，类就是对象，并且你可以在运行的时候动态创建类.

## 那到底什么是metaclass(元类)

metaclass 就是创建类的那家伙。(事实上，`type`就是一个metaclass)

我们知道,我们定义了class就是为了能够创建object的，没错吧?

我们也学习了，python中类也是对象。

那么，metaclass就是用来创造“类对象”的类.它是“类对象”的“类”。

可以这样子来理解:

![图片](http://static.extremevision.com.cn/membercms/python_metaclass_img1.png)

``` python
    MyClass = MetaClass()
    MyObject = MyClass()
```

也可以用我们上面学到的`type`来表示:

``` python
    MyClass = type('MyClass', (), {})
```

说白了,函数`type`就是一个特殊的metaclass.
python在背后使用`type`创造了所有的类。`type`是所有类的metaclass.

我们可以使用`__class__`属性来验证这个说法.

在python中，一切皆为对象：整数、字符串、函数、类.所有这些对象，都是通过类来创造的.

``` python
    >>> age = 35
    >>> age.__class__
    <type 'int'>

    >>> name = 'bob'
    >>> name.__class__
    <type 'str'>

    >>> def foo(): pass
    >>> foo.__class__
    <type 'function'>

    >>> class Bar(object): pass
    >>> b = Bar()
    >>> b.__class__
    <class '__main__.Bar'>
```

那么，`__class__`的`__class__`又是什么呢?

``` python
    >>> age.__class__.__class__
    <type 'type'>
    >>> name.__class__.__class__
    <type 'type'>
    >>> foo.__class__.__class__
    <type 'type'>
    >>> b.__class__.__class__
    <type 'type'>
```

metaclass就是创造类对象的工具.如果你喜欢，你也可以称之为"类的工厂".

type是python內置的metaclass。不过，你也可以编写自己的metaclass.


## `__metaclass__` 属性

我们可以在一个类中加入 `__metaclass__` 属性.

``` python
    class Foo(object):
        __metaclass__ = something...
        ......  # 省略
```

当你这么做了，python就会使用metaclass来创造类:Foo。

注意啦，这里有些技巧的。

当你写下`class Foo(object)`的时候，类对象Foo还没有在内存中生成。

python会在类定义中寻找`__metaclass__` 。如果找到了，python就会使用这个`__metaclass__` 来创造类对象: Foo。如果没找到，python就使用type来创造Foo。

请把下面的几段话重复几遍：

当你写如下代码的时候:

``` python
    class Foo(Bar):
        pass
```

python做了以下事情:

Foo中有`__metaclass__`这个属性吗？
如果有，python会在内存中通过`__metaclass__`创建一个名字为Foo的类对象。
如果python没有在Foo中找到`__metaclass__`，它会继续在Bar（父类）中寻找`__metaclass__`，并尝试做和前面同样的操作。
如果python由下往上遍历父类也都没有找不到`__metaclass__`，它就会在模块(module)中去寻找`__metaclass__`，并尝试做同样的操作。
如果还是没有找不到`__metaclass__`， python才会用内置的type(这也是一个metaclass)来创建这个类对象。

现在问题来了,我们要怎么用代码来实现`__metaclass__`呢?  写一些可以用来产生类(class)的东西就行。

那什么可以产生类？无疑就是`type`，或者`type`的任何子类,或者任何使用到`type`的东西都行.


## 自定义metaclass

使用metaclass的主要目的，是为了能够在创建类的时候，自动地修改类。

一个很傻的需求，我们决定要将该模块中的所有类的属性，改为大写。

有几种方法可以做到，这里使用`__metaclass__`来实现.

在模块的层次定义metaclass,模块中的所有类都会使用它来创造类。我们只需要告诉metaclass,将所有的属性转化为大写。

``` python
    # type也是一个类，我们可以继承它.
    class UpperAttrMetaclass(type):
        # __new__ 是在__init__之前被调用的特殊方法
        # __new__是用来创建对象并返回这个对象
        # 而__init__只是将传入的参数初始化给对象
        # 实际中,你很少会用到__new__，除非你希望能够控制对象的创建
        # 在这里，类是我们要创建的对象，我们希望能够自定义它，所以我们改写了__new__
        # 如果你希望的话，你也可以在__init__中做些事情
        # 还有一些高级的用法会涉及到改写__call__，但这里我们就先不这样.

        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents, future_class_attr):

            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
            return type(future_class_name, future_class_parents, uppercase_attr)
```

这里的方式其实不是OOP(面向对象编程).因为我们直接调用了type,而不是改写父类的`__type__`方法.

所以我们也可以这样子处理:

``` python
    class UpperAttrMetaclass(type):

        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents, future_class_attr):

            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
            return type.__new__(upperattr_metaclass, future_class_name,
                                future_class_parents, uppercase_attr)
```

这样子看,我们只是复用了 `type.__new__`方法,这就是我们熟悉的基本的OOP编程，没什么魔法可言.

你可能注意到,`__new__`方法相比于

``` python
    type(future_class_name, future_class_parents, future_class_attr)
```

多了一个参数: upperattr_metaclass, 请别在意,这没什么特别的: `__new__`总是将"它要定义的类"作为第一个参数。

这就好比是 self 在类的一般方法(method)中一样,也是被作为第一个参数传入。

当然啦，这里的名字的确是我起的太长了。就像self一样，所有的参数都有它们传统的名称。
因此，在实际的代码中,一个metaclass应该是写成下面样子的:

(我们同时使用常见的super来让代码更清晰)

``` python
    class UpperAttrMetaclass(type):

        def __new__(cls, clsname, bases, attrs):
            uppercase_attr = {}
            for name, val in attrs.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val
            return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, attrs)
```

使用了 metaclass 的代码是比较复杂，但我们使用它的原因并不是为了复杂, 而是因为我们通常会使用 metaclass  去做一些晦涩的事情,比如, 依赖于自省，控制继承等等。

确实，用 metaclass 来搞些“黑魔法”是特别有用的，因而会复杂化代码。

但就metaclass本身而言，它们其实是很简单的：中断类的默认创建、修改类、最后返回修改后的类.


## 到底为什么要使用metaclass

现在我们面临一个问题: 为什么要使用metaclass? 它容易出错且晦涩难懂.

好吧，一般来说，我们根本就用不上它, 99%的用户应该根本不必为此操心。

实际用到metaclass的人，很清楚他们到底需要做什么,根本不用解释为什么要用.

metaclass 的一个主要用途就是构建API。Django(一个python写的web框架)的ORM 就是一个例子。

用Django先定义了以下Model:

``` python
    class Person(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField()
```

然后执行下面代码:

``` python
    guy = Person.objects.get(name='bob')
    print guy.age  # result is 35
```

这里打印的输出并不是`IntegerField`，而是一个`int`，`int`是从数据库中获取的.

这是因为 `models.Model` 使用 `__metaclass__`来实现了复杂的数据库查询。但对于你看来,这就是简单的API而已,不用关心背后的复杂工作。


## 结语

复习一下,我们知道了,类是能够创造对象实例的对象，同时也是metaclass的对象实例(因为metaclass创造了它们).

在python中，一切皆为对象。它们要么是类的实例，要么是metaclass的实例, 除了type。

type是它自身的metaclass。至于是怎么实现的，总之纯python语言是不可能实现的,这需要在实现层面上耍一些小手段才能做到的。

metaclass用起来比较复杂, 如果需要对非常简单的类进行修改, 你可能不会使用它。有以下两个技术可以供你选择:

- [猴子修补 Monkey patch](https://en.wikipedia.org/wiki/Monkey_patch)
- 类修饰器

[source]: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
