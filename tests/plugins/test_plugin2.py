#!/usr/bin/python
# -*- coding: utf-8 -*-

import hookable

@hookable.trigger
def before_dispatch(arg1, arg2):
    print "called test_plugin1:before_dispatch"
    print "arg1"
    print arg1
    print "arg2"
    print arg2


@hookable.trigger
def after_dispatch(arg1, arg2):
    print "called test_plugin1:after_dispatch"

