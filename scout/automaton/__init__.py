#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : __init__.py<3>
# created at : 2013-03-27 19:06:29
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

from scout.exceptions import NotImplement

class BaseAutomata(object):
    """
    A automation used to fix issues
    """

    def __init__(self, platforms, issues):
        self.platforms = platforms
        self.issues = issues

    def appropriate(self, platform, issues):
        raise NotImplement()

    def fix(self, platform):
        raise NotImplement()

    def help(self):
        raise NotImplement()
