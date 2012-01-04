#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from nose.tools import ok_
from hookable import load_plugins


def test_load_plugins():
    plugin_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                     'plugins')
    plugins = load_plugins([plugin_dir])
    ok_(len(plugins) == 2)


