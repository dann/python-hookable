#!/usr/bin/python
# -*- coding: utf-8 -*-

""" pyhookable makes module hookable.

method name is trigger

Usage
    @hookable.trigger
    def before_dispatch():
        print "called before dispatching"

"""

from functools import wraps
from hookable.plugin import PluginLoader

__hookable_triggers__ = {}


def trigger(func):
    trigger_name = func.__name__
    register_trigger(trigger_name, func)

    @wraps(func)
    def _trigger(*args, **kwargs):
        return func(*args, **kwargs)

    return _trigger


def call_trigger(trigger, *args):
    trigger = __hookable_triggers__.get(trigger, None)
    if trigger:
        for func in trigger:
            func(*args)


def call_trigger_with_return(trigger, arg):

    # TODO FIXME

    trigger = __hookable_triggers__.get(trigger, None)
    if trigger:
        for func in trigger:
            arg = func(arg)
    return arg


def register_trigger(trigger, func):
    if func not in __hookable_triggers__.setdefault(trigger, []):
        __hookable_triggers__[trigger].append(func)


def remove_trigger(trigger, func):
    trigger = __hookable_triggers__.get(trigger, [])
    if func in trigger:
        trigger.remove(func)


def load_plugins(plugin_dirs):
    loader = PluginLoader()
    return loader.load_plugins(plugin_dirs)


