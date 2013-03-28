#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : missingbinary.py
# created at : 2013-03-28 10:18:13
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

from scout.issues import BaseIssue

class MissingBinaryIssue(BaseIssue):

    identifier = 'rsync'

    contacts = 'admin@localhost'

    detail = 'rsync is important to our transportation infrastructure'

    def __init__(self, binary):
        self.binary = binary
