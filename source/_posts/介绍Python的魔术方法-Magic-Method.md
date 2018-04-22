---
title: 介绍Python的魔术方法 - Magic Method
date: 2016-10-24 01:01:37
toc: true
categories:
- python
tags:
- python
- 翻译
---

## 前言

在Python中，所有以`__`双下划线包起来的方法，都统称为"魔术方法"。比如我们接触最多的`__init__`.

有些魔术方法,我们可能以后一辈子都不会再遇到了,这里也就只是简单介绍下;

而有些魔术方法,巧妙使用它可以构造出非常优美的代码,比如将复杂的逻辑封装成简单的API。

本文编辑的思路借鉴自Rafe Kettler的这篇博客: [A Guide to Python Magic Methods](http://www.rafekettler.com/magicmethods.html)，并补充了一些代码示例。

介绍的顺序大概是：常见的先介绍，越少见的越靠后讲。

本文中用到的代码示例，可以在我的[github](https://github.com/wolfhong/blogs/tree/master/example/python_magic_method)下载到。


## 构造和初始化

`__init__`我们很熟悉了,它在对象初始化的时候调用,我们一般将它理解为"构造函数".

实际上, 当我们调用`x = SomeClass()`的时候调用,`__init__`并不是第一个执行的, `__new__`才是。所以准确来说,是`__new__`和`__init__`共同构成了"构造函数".

`__new__`是用来创建类并返回这个类的实例, 而`__init__`只是将传入的参数来初始化该实例.

`__new__`在创建一个实例的过程中必定会被调用,但`__init__`就不一定，比如通过`pickle.load`的方式反序列化一个实例时就不会调用`__init__`。

`__new__`方法总是需要返回该类的一个实例，而`__init__`不能返回除了None的任何值。比如下面例子:

    class Foo(object):

        def __init__(self):
            print 'foo __init__'
            return None  # 必须返回None,否则抛TypeError

        def __del__(self):
            print 'foo __del__'

实际中,你很少会用到`__new__`，除非你希望能够控制类的创建。
如果要讲解`__new__`，往往需要牵扯到`metaclass`(元类)的介绍。
如果你有兴趣深入,可以参考我的另一篇博客: [理解Python的metaclass](/posts/理解python的metaclass/)

对于`__new__`的重载，[Python文档中](https://www.python.org/download/releases/2.2/descrintro/#__new__)也有了详细的介绍。

在对象的生命周期结束时, `__del__`会被调用,可以将`__del__`理解为"析构函数".
`__del__`定义的是当一个对象进行垃圾回收时候的行为。

有一点容易被人误解, 实际上，`x.__del__()` 并不是对于`del x`的实现,但是往往执行`del x`时会调用`x.__del__()`.

怎么来理解这句话呢? 继续用上面的Foo类的代码为例:

    foo = Foo()
    foo.__del__()
    print foo
    del foo
    print foo  # NameError, foo is not defined

如果调用了`foo.__del__()`，对象本身仍然存在. 但是调用了`del foo`, 就再也没有foo这个对象了.

请注意，如果解释器退出的时候对象还存在，就不能保证 `__del__` 被确切的执行了。所以`__del__`并不能替代良好的编程习惯。
比如，在处理socket时，及时关闭结束的连接。


## 属性访问控制

总有人要吐槽Python缺少对于类的封装,比如希望Python能够定义私有属性，然后提供公共可访问的getter和 setter。Python其实可以通过魔术方法来实现封装。

`__getattr__(self, name)`

该方法定义了你试图访问一个不存在的属性时的行为。因此，重载该方法可以实现捕获错误拼写然后进行重定向, 或者对一些废弃的属性进行警告。

`__setattr__(self, name, value)`

`__setattr__` 是实现封装的解决方案，它定义了你对属性进行赋值和修改操作时的行为。
不管对象的某个属性是否存在,它都允许你为该属性进行赋值,因此你可以为属性的值进行自定义操作。有一点需要注意，实现`__setattr__`时要避免"无限递归"的错误，下面的代码示例中会提到。

`__delattr__(self, name)`

`__delattr__`与`__setattr__`很像，只是它定义的是你删除属性时的行为。实现`__delattr__`是同时要避免"无限递归"的错误。

`__getattribute__(self, name)`

`__getattribute__`定义了你的属性被访问时的行为，相比较，`__getattr__`只有该属性不存在时才会起作用。
因此，在支持`__getattribute__`的Python版本,调用`__getattr__`前必定会调用 `__getattribute__`。`__getattribute__`同样要避免"无限递归"的错误。
需要提醒的是，最好不要尝试去实现`__getattribute__`,因为很少见到这种做法，而且很容易出bug。

例子说明`__setattr__`的无限递归错误:

    def __setattr__(self, name, value):
        self.name = value
        # 每一次属性赋值时, __setattr__都会被调用，因此不断调用自身导致无限递归了。

因此正确的写法应该是:

    def __setattr__(self, name, value):
        self.__dict__[name] = value

`__delattr__`如果在其实现中出现`del self.name` 这样的代码也会出现"无限递归"错误，这是一样的原因。

下面的例子很好的说明了上面介绍的4个魔术方法的调用情况:

    class Access(object):

        def __getattr__(self, name):
            print '__getattr__'
            return super(Access, self).__getattr__(name)

        def __setattr__(self, name, value):
            print '__setattr__'
            return super(Access, self).__setattr__(name, value)

        def __delattr__(self, name):
            print '__delattr__'
            return super(Access, self).__delattr__(name)

        def __getattribute__(self, name):
            print '__getattribute__'
            return super(Access, self).__getattribute__(name)

    access = Access()
    access.attr1 = True  # __setattr__调用
    access.attr1  # 属性存在,只有__getattribute__调用
    try:
        access.attr2  # 属性不存在, 先调用__getattribute__, 后调用__getattr__
    except AttributeError:
        pass
    del access.attr1  # __delattr__调用


## 描述器对象

我们从一个例子来入手,介绍什么是描述符,并介绍`__get__`, `__set__`, `__delete__` 的使用。(放在这里介绍是为了跟上一小节介绍的魔术方法作对比)

我们知道，距离既可以用单位"米"表示,也可以用单位"英尺"表示。
现在我们定义一个类来表示距离,它有两个属性: 米和英尺。

    class Meter(object):
        '''Descriptor for a meter.'''
        def __init__(self, value=0.0):
            self.value = float(value)
        def __get__(self, instance, owner):
            return self.value
        def __set__(self, instance, value):
            self.value = float(value)

    class Foot(object):
        '''Descriptor for a foot.'''
        def __get__(self, instance, owner):
            return instance.meter * 3.2808
        def __set__(self, instance, value):
            instance.meter = float(value) / 3.2808

    class Distance(object):
        meter = Meter()
        foot = Foot()

    d = Distance()
    print d.meter, d.foot  # 0.0, 0.0
    d.meter = 1
    print d.meter, d.foot  # 1.0 3.2808
    d.meter = 2
    print d.meter, d.foot  # 2.0 6.5616

在上面例子中,在还没有对Distance的实例赋值前, 我们认为meter和foot应该是各自类的实例对象, 但是输出却是数值。这是因为`__get__`发挥了作用.

我们只是修改了meter,并且将其赋值成为int，但foot也修改了。这是`__set__`发挥了作用.

描述器对象(Meter、Foot)不能独立存在, 它需要被另一个所有者类(Distance)所持有。
描述器对象可以访问到其拥有者实例的属性，比如例子中Foot的`instance.meter`。

在面向对象编程时，如果一个类的属性有相互依赖的关系时，使用描述器来编写代码可以很巧妙的组织逻辑。
在Django的ORM中, models.Model中的IntegerField等, 就是通过描述器来实现功能的。

一个类要成为描述器，必须实现`__get__`, `__set__`, `__delete__` 中的至少一个方法。下面简单介绍下:

`__get__(self, instance, owner)`

参数instance是拥有者类的实例。参数owner是拥有者类本身。`__get__`在其拥有者对其读值的时候调用。

`__set__(self, instance, value)`

`__set__`在其拥有者对其进行修改值的时候调用。

`__delete__(self, instance)`

`__delete__`在其拥有者对其进行删除的时候调用。


## 构造自定义容器(Container)

在Python中，常见的容器类型有: dict, tuple, list, string。
其中tuple, string是不可变容器，dict, list是可变容器。
可变容器和不可变容器的区别在于，不可变容器一旦赋值后，不可对其中的某个元素进行修改。
比如定义了`l = [1, 2, 3]`和`t = (1, 2, 3)`后, 执行`l[0] = 0`是可以的，但执行`t[0] = 0`则会报错。

如果我们要自定义一些数据结构，使之能够跟以上的容器类型表现一样，那就需要去实现某些协议。

这里的协议跟其他语言中所谓的"接口"概念很像，一样的需要你去实现才行，只不过没那么正式而已。

如果要自定义不可变容器类型，只需要定义`__len__` 和 `__getitem__`方法;
如果要自定义可变容器类型，还需要在不可变容器类型的基础上增加定义`__setitem__` 和 `__delitem__`。
如果你希望你的自定义数据结构还支持"可迭代", 那就还需要定义`__iter__`。

`__len__(self)`

需要返回数值类型，以表示容器的长度。该方法在可变容器和不可变容器中必须实现。

`__getitem__(self, key)`

当你执行`self[key]`的时候，调用的就是该方法。该方法在可变容器和不可变容器中也都必须实现。
调用的时候,如果key的类型错误，该方法应该抛出TypeError；
如果没法返回key对应的数值时,该方法应该抛出ValueError。

`__setitem__(self, key, value)`

当你执行`self[key] = value`时，调用的是该方法。

`__delitem__(self, key)`

当你执行`del self[key]`的时候，调用的是该方法。

`__iter__(self)`

该方法需要返回一个迭代器(iterator)。当你执行`for x in container:` 或者使用`iter(container)`时，该方法被调用。

`__reversed__(self)`

如果想要该数据结构被內建函数`reversed()`支持,就还需要实现该方法。

`__contains__(self, item)`

如果定义了该方法，那么在执行`item in container` 或者 `item not in container`时该方法就会被调用。
如果没有定义，那么Python会迭代容器中的元素来一个一个比较，从而决定返回True或者False。

`__missing__(self, key)`

`dict`字典类型会有该方法，它定义了key如果在容器中找不到时触发的行为。
比如`d = {'a': 1}`, 当你执行`d[notexist]`时，`d.__missing__('notexist')`就会被调用。

下面举例，使用上面讲的魔术方法来实现Haskell语言中的一个数据结构。

    # -*- coding: utf-8 -*-
    class FunctionalList:
        ''' 实现了内置类型list的功能,并丰富了一些其他方法: head, tail, init, last, drop, take'''

        def __init__(self, values=None):
            if values is None:
                self.values = []
            else:
                self.values = values

        def __len__(self):
            return len(self.values)

        def __getitem__(self, key):
            return self.values[key]

        def __setitem__(self, key, value):
            self.values[key] = value

        def __delitem__(self, key):
            del self.values[key]

        def __iter__(self):
            return iter(self.values)

        def __reversed__(self):
            return FunctionalList(reversed(self.values))

        def append(self, value):
            self.values.append(value)
        def head(self):
            # 获取第一个元素
            return self.values[0]
        def tail(self):
            # 获取第一个元素之后的所有元素
            return self.values[1:]
        def init(self):
            # 获取最后一个元素之前的所有元素
            return self.values[:-1]
        def last(self):
            # 获取最后一个元素
            return self.values[-1]
        def drop(self, n):
            # 获取所有元素，除了前N个
            return self.values[n:]
        def take(self, n):
            # 获取前N个元素
            return self.values[:n]

我们再举个例子，实现Perl语言的AutoVivification,它会在你每次引用一个值未定义的属性时为你自动创建数组或者字典。

    class AutoVivification(dict):
        """Implementation of perl's autovivification feature."""
        def __missing__(self, key):
            value = self[key] = type(self)()
            return value

    weather = AutoVivification()
    weather['china']['guangdong']['shenzhen'] = 'sunny'
    weather['china']['hubei']['wuhan'] = 'windy'
    weather['USA']['California']['Los Angeles'] = 'sunny'
    print weather

    结果输出:{'china': {'hubei': {'wuhan': 'windy'}, 'guangdong': {'shenzhen': 'sunny'}}, 'USA':    {'California': {'Los Angeles': 'sunny'}}}

在Python中，关于自定义容器的实现还有更多实用的例子，但只有很少一部分能够集成在Python标准库中，比如[Counter, OrderedDict等](https://docs.python.org/2/library/collections.html)


## 上下文管理

`with`声明是从Python2.5开始引进的关键词。你应该遇过这样子的代码:

    with open('foo.txt') as bar:
        # do something with bar

在with声明的代码段中，我们可以做一些对象的开始操作和清除操作,还能对异常进行处理。
这需要实现两个魔术方法: `__enter__` 和 `__exit__`。

`__enter__(self)`

`__enter__`会返回一个值，并赋值给`as`关键词之后的变量。在这里，你可以定义代码段开始的一些操作。

`__exit__(self, exception_type, exception_value, traceback)`

`__exit__`定义了代码段结束后的一些操作，可以这里执行一些清除操作，或者做一些代码段结束后需要立即执行的命令，比如文件的关闭，socket断开等。如果代码段成功结束，那么exception_type, exception_value, traceback 三个参数传进来时都将为None。如果代码段抛出异常，那么传进来的三个参数将分别为: 异常的类型，异常的值，异常的追踪栈。
如果`__exit__`返回True, 那么with声明下的代码段的一切异常将会被屏蔽。
如果`__exit__`返回None, 那么如果有异常，异常将正常抛出，这时候with的作用将不会显现出来。

举例说明：

这该示例中，IndexError始终会被隐藏，而TypeError始终会抛出。

    class DemoManager(object):

        def __enter__(self):
            pass

        def __exit__(self, ex_type, ex_value, ex_tb):
            if ex_type is IndexError:
                print ex_value.__class__
                return True
            if ex_type is TypeError:
                print ex_value.__class__
                return  # return None

    with DemoManager() as nothing:
        data = [1, 2, 3]
        data[4]  # raise IndexError, 该异常被__exit__处理了

    with DemoManager() as nothing:
        data = [1, 2, 3]
        data['a']  # raise TypeError, 该异常没有被__exit__处理

    输出:
    <type 'exceptions.IndexError'>
    <type 'exceptions.TypeError'>
    Traceback (most recent call last):
      ...


## 对象的序列化

Python对象的序列化操作是pickling进行的。pickling非常的重要，以至于Python对此有单独的模块`pickle`，还有一些相关的魔术方法。使用pickling, 你可以将数据存储在文件中，之后又从文件中进行恢复。

下面举例来描述pickle的操作。从该例子中也可以看出,如果通过pickle.load 初始化一个对象, 并不会调用`__init__`方法。

    # -*- coding: utf-8 -*-
    from datetime import datetime
    import pickle

    class Distance(object):

        def __init__(self, meter):
            print 'distance __init__'
            self.meter = meter

    data = {
        'foo': [1, 2, 3],
        'bar': ('Hello', 'world!'),
        'baz': True,
        'dt': datetime(2016, 10, 01),
        'distance': Distance(1.78),
    }
    print 'before dump:', data
    with open('data.pkl', 'wb') as jar:
        pickle.dump(data, jar)  # 将数据存储在文件中

    del data
    print 'data is deleted!'

    with open('data.pkl', 'rb') as jar:
        data = pickle.load(jar)  # 从文件中恢复数据
    print 'after load:', data

值得一提，从其他文件进行pickle.load操作时，需要注意有恶意代码的可能性。另外，Python的各个版本之间,pickle文件可能是互不兼容的。

pickling并不是Python的內建类型，它支持所有实现pickle协议(可理解为接口)的类。pickle协议有以下几个可选方法来自定义Python对象的行为。

`__getinitargs__(self)`

如果你希望unpickle时，`__init__`方法能够调用，那么就需要定义`__getinitargs__`, 该方法需要返回一系列参数的元组，这些参数就是传给`__init__`的参数。

该方法只对`old-style class`有效。所谓`old-style class`,指的是不继承自任何对象的类，往往定义时这样表示: `class A:`, 而非`class A(object):`

`__getnewargs__(self)`

跟`__getinitargs__`很类似，只不过返回的参数元组将传值给`__new__`

`__getstate__(self)`

在调用`pickle.dump`时，默认是对象的`__dict__`属性被存储，如果你要修改这种行为，可以在`__getstate__`方法中返回一个state。state将在调用`pickle.load`时传值给`__setstate__`

`__setstate__(self, state)`

一般来说,定义了`__getstate__`,就需要相应地定义`__setstate__`来对`__getstate__`返回的state进行处理。

`__reduce__(self)`

如果pickle的数据包含了自定义的扩展类（比如使用C语言实现的Python扩展类）时，就需要通过实现`__reduce__`方法来控制行为了。由于使用过于生僻，这里就不展开继续讲解了。

令人容易混淆的是，我们知道, `reduce()`是Python的一个內建函数, 需要指出`__reduce__`并非定义了`reduce()`的行为，二者没有关系。

`__reduce_ex__(self)`

`__reduce_ex__` 是为了兼容性而存在的, 如果定义了`__reduce_ex__`, 它将代替`__reduce__` 执行。

下面的代码示例很有意思，我们定义了一个类Slate(中文是板岩的意思)。这个类能够记录历史上每次写入给它的值,但每次`pickle.dump`时当前值就会被清空，仅保留了历史。

    # -*- coding: utf-8 -*-
    import pickle
    import time

    class Slate:
        '''Class to store a string and a changelog, and forget its value when pickled.'''
        def __init__(self, value):
            self.value = value
            self.last_change = time.time()
            self.history = []

        def change(self, new_value):
            # 修改value, 将上次的valeu记录在history
            self.history.append((self.last_change, self.value))
            self.value = new_value
            self.last_change = time.time()

        def print_changes(self):
            print 'Changelog for Slate object:'
            for k, v in self.history:
                print '%s    %s' % (k, v)

        def __getstate__(self):
            # 故意不返回self.value和self.last_change,
            # 以便每次unpickle时清空当前的状态，仅仅保留history
            return self.history

        def __setstate__(self, state):
            self.history = state
            self.value, self.last_change = None, None

    slate = Slate(0)
    time.sleep(0.5)
    slate.change(100)
    time.sleep(0.5)
    slate.change(200)
    slate.change(300)
    slate.print_changes()  # 与下面的输出历史对比
    with open('slate.pkl', 'wb') as jar:
        pickle.dump(slate, jar)
    del slate  # delete it
    with open('slate.pkl', 'rb') as jar:
        slate = pickle.load(jar)
    print 'current value:', slate.value  # None
    print slate.print_changes()  # 输出历史记录与上面一致


## 运算符相关的魔术方法

运算符相关的魔术方法实在太多了，也很好理解，不打算多讲。在其他语言里，也有重载运算符的操作，所以我们对这些魔术方法已经很了解了。

### 比较运算符

`__cmp__(self, other)`

如果该方法返回负数，说明`self < other`; 返回正数，说明`self > other`; 返回0说明`self == other`。
强烈不推荐来定义`__cmp__`, 取而代之, 最好分别定义`__lt__`等方法从而实现比较功能。
`__cmp__`在Python3中被废弃了。

`__eq__(self, other)`

定义了比较操作符`==`的行为.

`__ne__(self, other)`

定义了比较操作符`!=`的行为.

`__lt__(self, other)`

定义了比较操作符`<`的行为.

`__gt__(self, other)`

定义了比较操作符`>`的行为.

`__le__(self, other)`

定义了比较操作符`<=`的行为.

`__ge__(self, other)`

定义了比较操作符`>=`的行为.

下面我们定义一种类型Word, 它会使用单词的长度来进行大小的比较, 而不是采用str的比较方式。
但是为了避免 `Word('bar') == Word('foo')` 这种违背直觉的情况出现,并没有定义`__eq__`, 因此Word会使用它的父类(str)中的`__eq__`来进行比较。

下面的例子中也可以看出: 在编程语言中, 如果`a >=b and a <= b`, 并不能推导出`a == b`这样的结论。

    # -*- coding: utf-8 -*-
    class Word(str):
        '''存储单词的类，定义比较单词的几种方法'''
        def __new__(cls, word):
            # 注意我们必须要用到__new__方法，因为str是不可变类型
            # 所以我们必须在创建的时候将它初始化
            if ' ' in word:
                print "Value contains spaces. Truncating to first space."
                word = word[:word.index(' ')]  # 单词是第一个空格之前的所有字符
            return str.__new__(cls, word)

        def __gt__(self, other):
            return len(self) > len(other)
        def __lt__(self, other):
            return len(self) < len(other)
        def __ge__(self, other):
            return len(self) >= len(other)
        def __le__(self, other):
            return len(self) <= len(other)

    print 'foo < fool:', Word('foo') < Word('fool')  # True
    print 'foolish > fool:', Word('foolish') > Word('fool')  # True
    print 'bar >= foo:', Word('bar') >= Word('foo')  # True
    print 'bar <= foo:', Word('bar') <= Word('foo')  # True
    print 'bar == foo:', Word('bar') == Word('foo')  # False, 用了str内置的比较方法来进行比较
    print 'bar != foo:', Word('bar') != Word('foo')  # True

### 一元运算符和函数

`__pos__(self)`

实现了'+'号一元运算符(比如`+some_object`)

`__neg__(self)`

实现了'-'号一元运算符(比如`-some_object`)

`__invert__(self)`

实现了`~`号(波浪号)一元运算符(比如`~some_object`)

`__abs__(self)`

实现了`abs()`內建函数.

`__round__(self, n)`

实现了`round()`内建函数. 参数n表示四舍五进的精度.

`__floor__(self)`

实现了`math.floor()`, 向下取整.

`__ceil__(self)`

实现了`math.ceil()`, 向上取整.

`__trunc__(self)`

实现了`math.trunc()`, 向0取整.

### 算术运算符

`__add__(self, other)`

实现了加号运算.

`__sub__(self, other)`

实现了减号运算.

`__mul__(self, other)`

实现了乘法运算.

`__floordiv__(self, other)`

实现了`//`运算符.

`__div__(self, other)`

实现了`/`运算符. 该方法在Python3中废弃. 原因是Python3中，division默认就是true division.

`__truediv__`(self, other)

实现了true division. 只有你声明了`from __future__ import division`该方法才会生效.

`__mod__(self, other)`

实现了`%`运算符, 取余运算.

`__divmod__(self, other)`

实现了`divmod()`內建函数.

`__pow__(self, other)`

实现了`**`操作. N次方操作.

`__lshift__(self, other)`

实现了位操作`<<`.

`__rshift__(self, other)`

实现了位操作`>>`.

`__and__(self, other)`

实现了位操作`&`.

`__or__(self, other)`

实现了位操作`|`

`__xor__(self, other)`

实现了位操作`^`

### 反算术运算符

这里只需要解释一下概念即可。
假设针对some_object这个对象:

    some_object + other

上面的代码非常正常地实现了some_object的`__add__`方法。那么如果遇到相反的情况呢?

    other + some_object

这时候，如果other没有定义`__add__`方法，但是some_object定义了`__radd__`, 那么上面的代码照样可以运行。
这里的`__radd__(self, other)`就是`__add__(self, other)`的反算术运算符。

所以，类比的，我们就知道了更多的反算术运算符, 就不一一展开了:

- `__rsub__(self, other)`
- `__rmul__(self, other)`
- `__rmul__(self, other)`
- `__rfloordiv__(self, other)`
- `__rdiv__(self, other)`
- `__rtruediv__(self, other)`
- `__rmod__(self, other)`
- `__rdivmod__(self, other)`
- `__rpow__(self, other)`
- `__rlshift__(self, other)`
- `__rrshift__(self, other)`
- `__rand__(self, other)`
- `__ror__(self, other)`
- `__rxor__(self, other)`

### 增量赋值

这也是只要理解了概念就容易掌握的运算。举个例子:

    x = 5
    x += 1  # 这里的+=就是增量赋值，将x+1赋值给了x

因此对于`a += b`, `__iadd__` 将返回`a + b`, 并赋值给a。
所以很容易理解下面的魔术方法了:

- `__iadd__(self, other)`
- `__isub__(self, other)`
- `__imul__(self, other)`
- `__ifloordiv__(self, other)`
- `__idiv__(self, other)`
- `__itruediv__(self, other)`
- `__imod__(self, other)`
- `__ipow__(self, other)`
- `__ilshift__(self, other)`
- `__irshift__(self, other)`
- `__iand__(self, other)`
- `__ior__(self, other)`
- `__ixor__(self, other)`

### 类型转化

`__int__(self)`

实现了类型转化为int的行为.

`__long__(self)`

实现了类型转化为long的行为.

`__float__(self)`

实现了类型转化为float的行为.

`__complex__(self)`

实现了类型转化为complex(复数, 也即1+2j这样的虚数)的行为.

`__oct__(self)`

实现了类型转化为八进制数的行为.

`__hex__(self)`

实现了类型转化为十六进制数的行为.

`__index__(self)`

在切片运算中将对象转化为int, 因此该方法的返回值必须是int。用一个例子来解释这个用法。

    class Thing(object):
        def __index__(self):
            return 1

    thing = Thing()
    list_ = ['a', 'b', 'c']
    print list_[thing]  # 'b'
    print list_[thing:thing]  # []

上面例子中, `list_[thing]`的表现跟`list_[1]`一致，正是因为Thing实现了`__index__`方法。

可能有的人会想，`list_[thing]`为什么不是相当于`list_[int(thing)]`呢? 通过实现Thing的`__int__`方法能否达到这个目的呢?

显然不能。如果真的是这样的话，那么`list_[1.1:2.2]`这样的写法也应该是通过的。
而实际上，该写法会抛出TypeError: `slice indices must be integers or None or have an __index__ method`

下面我们再做个例子,如果对一个dict对象执行`dict_[thing]`会怎么样呢?

    dict_ = {1: 'apple', 2: 'banana', 3: 'cat'}
    print dict_[thing]  # raise KeyError

这个时候就不是调用`__index__`了。虽然`list`和`dict`都实现了`__getitem__`方法, 但是它们的实现方式是不一样的。
如果希望上面例子能够正常执行, 需要实现Thing的`__hash__` 和 `__eq__`方法.

    class Thing(object):
        def __hash__(self):
            return 1
        def __eq__(self, other):
            return hash(self) == hash(other)

    dict_ = {1: 'apple', 2: 'banana', 3: 'cat'}
    print dict_[thing]  # apple

`__coerce__(self, other)`

实现了混合模式运算。

要了解这个方法,需要先了解`coerce()`内建函数: [官方文档](https://docs.python.org/2/library/functions.html#coerce)上的解释是, coerce(x, y)返回一组数字类型的参数, 它们被转化为同一种类型，以便它们可以使用相同的算术运算符进行操作。如果过程中转化失败，抛出TypeError。

比如对于`coerce(10, 10.1)`, 因为10和10.1在进行算术运算时，会先将10转为10.0再来运算。因此`coerce(10, 10.1)`返回值是(10.0, 10.1).

`__coerce__`在Python3中废弃了。

## 其他魔术方法

还没讲到的魔术方法还有很多，但有些我觉得很简单，或者很少见，就不再累赘展开说明了。

`__str__(self)`

对实例使用`str()`时调用。

`__repr__(self)`

对实例使用`repr()`时调用。`str()`和`repr()`都是返回一个代表该实例的字符串，
主要区别在于: str()的返回值要方便人来看,而repr()的返回值要方便计算机看。

`__unicode__(self)`

对实例使用`unicode()`时调用。`unicode()`与`str()`的区别在于: 前者返回值是unicode, 后者返回值是str。unicode和str都是`basestring`的子类。

当你对一个类只定义了`__str__`但没定义`__unicode__`时,`__unicode__`会根据`__str__`的返回值自动实现,即`return unicode(self.__str__())`;
但返回来则不成立。

    class StrDemo2:
        def __str__(self):
            return 'StrDemo2'

    class StrDemo3:
        def __unicode__(self):
            return u'StrDemo3'

    demo2 = StrDemo2()
    print str(demo2)  # StrDemo2
    print unicode(demo2)  # StrDemo2

    demo3 = StrDemo3()
    print str(demo3)  # <__main__.StrDemo3 instance>
    print unicode(demo3)  # StrDemo3

`__format__(self, formatstr)`

`"Hello, {0:abc}".format(a)`等价于`format(a, "abc")`, 等价于`a.__format__("abc")`。

这在需要格式化展示对象的时候非常有用，比如格式化时间对象。

`__hash__(self)`

对实例使用`hash()`时调用, 返回值是数值类型。

`__nonzero__(self)`

对实例使用`bool()`时调用, 返回True或者False。
你可能会问, 为什么不是命名为`__bool__`? 我也不知道。
我只知道该方法在Python3中改名为`__bool__`了。

`__dir__(self)`

对实例使用`dir()`时调用。通常实现该方法是没必要的。

`__sizeof__(self)`

对实例使用`sys.getsizeof()`时调用。返回对象的大小，单位是bytes。

`__instancecheck__(self, instance)`

对实例调用`isinstance(instance, class)`时调用。 返回值是布尔值。它会判断instance是否是该类的实例。

`__subclasscheck__(self, subclass)`

对实例使用`issubclass(subclass, class)`时调用。返回值是布尔值。它会判断subclass否是该类的子类。

`__copy__(self)`

对实例使用`copy.copy()`时调用。返回"浅复制"的对象。

`__deepcopy__(self, memodict={})`

对实例使用`copy.deepcopy()`时调用。返回"深复制"的对象。

`__call__(self, [args...])`

该方法允许类的实例跟函数一样表现:

    class XClass:
        def __call__(self, a, b):
            return a + b

    def add(a, b):
        return a + b

    x = XClass()
    print 'x(1, 2)', x(1, 2)
    print 'callable(x)', callable(x)  # True
    print 'add(1, 2)', add(1, 2)
    print 'callable(add)', callable(add)  # True


## Python3中的差异

- Python3中，str与unicode的区别被废除了,因而`__unicode__`没有了，取而代之地出现了`__bytes__`.
- Python3中，division默认就是true division, 因而`__div__`废弃.
- `__coerce__`因存在冗余而废弃.
- `__cmp__`因存在冗余而废弃.
- `__nonzero__`改名为`__bool__`.
