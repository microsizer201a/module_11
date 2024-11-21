import inspect
import os


def introspection_info(obj):
    res = {"тип объекта:": type(obj),
           "атрибуты объекта:": [attr_name for attr_name in dir(obj) if not callable(getattr(obj, attr_name))],
           "методы объекта:": [attr_name for attr_name in dir(obj) if callable(getattr(obj, attr_name))],
           "модуль, к которому принадлежит объект": inspect.getmodule(obj)}
    return res

number_info = introspection_info(42)
print(number_info)