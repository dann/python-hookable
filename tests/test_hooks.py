#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from nose.tools import ok_
from hookable import load_plugins, call_trigger

# TODO
def test_run_hooks():
    plugin_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                     'plugins')
    load_plugins([plugin_dir])
    call_trigger('before_dispatch', 1, 2)
    ok_(1)
