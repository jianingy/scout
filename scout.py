#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : scout.py
# created at : 2013-03-27 20:47:48
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

import sys

if __name__ == '__main__':
    from time import sleep
    from scout import Scout

    s = Scout(verbose=True, colorful=True)
    n, last_remain = 0, -1

    s.inspect()
    remain = len(s.issues)

    while True:
        n = n + 1
        print "Round %s" % n



        remain = len(s.issues)
        if last_remain == remain:
            print "There's something can be solved automatically."
            sys.exit(0)

        if remain == 0:
            print "Everything is OK now"
            break

        s.fix()

        last_remain = remain

        sleep(1)
