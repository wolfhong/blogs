# -*- coding: utf-8 -*-


class DemoManager(object):

    def __enter__(self):
        pass

    def raise_indexerror(self):
        with self:
            data = [1, 2, 3]
            data[4]  # raise IndexError, 该异常被__exit__处理了

    def raise_typeerror(self):
        with self:
            data = [1, 2, 3]
            data['a']  # raise TypeError, 该异常没有被__exit__处理

    def __exit__(self, ex_type, ex_value, ex_tb):
        if ex_type is IndexError:
            print ex_value.__class__
            return True
        if ex_type is TypeError:
            print ex_value.__class__
            return  # return None


demo = DemoManager()
demo.raise_indexerror()
demo.raise_typeerror()
