#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : arch.py
# created at : 2013-03-28 09:12:41
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'


def detect():

    from os.path import isfile
    if isfile('/etc/redhat-release'):
        return ['rhel', 'rpm']
    elif isfile('/etc/arch-release'):
        return ['archlinux']

    return []
