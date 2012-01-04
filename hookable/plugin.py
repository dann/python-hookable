# -*- coding: utf-8 -*-

import os
import sys


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


