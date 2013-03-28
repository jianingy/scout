#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : apsara-rsync.py
# created at : 2013-03-27 18:34:25
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

from scout.inspectors import BaseInspector
from scout.issues.binary import MissingBinaryIssue

class Inspector(BaseInspector):

    def appropriate(self, platforms):
        return True

    def detect(self):
        from os.path import isfile
        from os import access, X_OK
        for target in ['/usr/bin/rsync', '/usr/local/bin/rsync']:
            if isfile(target) and access(target, X_OK):
                return True

        raise MissingBinaryIssue(binary='/usr/bin/rsync')
