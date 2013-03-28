#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : __init__.py
# created at : 2013-03-27 18:34:31
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

from scout.exceptions import NotImplement


class BaseInspector(object):

    def appropriate(self, platform):
        """
        Return true if this inspector is appropriate in current environment.
        Use platform, and use it well, to determine if this inspector fits
        current environment. E.g, if there is already a network issue don't
        check for HTTP as it must fail with a network failure.
        """

        raise NotImplement()

    def detect(self):
        """
        Do real detection thing here. Raise an exception of
        scout.Issue derives, if something doesn't right.
        """

        raise NotImplement()
