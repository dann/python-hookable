#!/usr/bin/python
# -*- coding: utf-8 -*-

""" pyhookable makes module hookable.

method name is trigger

Usage
    @hookable.trigger
    def before_dispatch():
        print "called before dispatching"

"""

import os
import sys

from functools import wraps

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

# TODO FIXME
def call_trigger_with_return(trigger, arg):
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


class PluginLoader(object):

    def __init__(self):
        self.plugins = []
        self.suffix = '.py'

    def load_plugins(self, plugin_dirs):
        if len(self.plugins) > 0:
            return self.plugins

        for plugin_dir in plugin_dirs:
            self.load_plugins_in(plugin_dir)

        return self.plugins

    def load_plugins_in(self, plugin_dir):
        plugins = self._find_plugins(plugin_dir)
        self._add_path_to_plugins(plugin_dir)
        self._import_plugins(plugins)
        return self.plugins

    def _find_plugins(self, plugin_dir):
        plugin_files = [f[:-3] for f in os.listdir(plugin_dir)
                        if f.endswith(self.suffix)
                        and not f.startswith('_')]
        return plugin_files

    def _add_path_to_plugins(self, plugin_dir):
        sys.path.insert(0, plugin_dir)

    def _import_plugins(self, plugin_files):
        for plugin in plugin_files:
            module = self._import_module(plugin)
            self.plugins.append(module)

    def _import_module(self, module):
        try:
            return __import__(module)
        except ImportError, e:
            print "Couldn't load %s: %s" % (module, e)

    def reload_plugins(self, plugin_dir):
        self.plugins = []
        return self.load_plugins(plugin_dir)


