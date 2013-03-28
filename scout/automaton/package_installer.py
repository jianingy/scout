#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : package_installer.py
# created at : 2013-03-28 10:27:51
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'


from scout.automaton import BaseAutomata


class Automaton(BaseAutomata):

    def appropriate(self):

        from scout.issues.binary import MissingBinaryIssue

        issues = filter(lambda x: isinstance(x, MissingBinaryIssue), self.issues)
        myissue = filter(lambda x: x.binary.find('rsync') > -1, issues)

        if myissue:
            return True

        return False


    def fix(self):
        from os import system
        retval = -1

        if 'rpm' in self.platforms:
            retval = system('yum install -y rsync')
        elif 'deb' in self.platforms:
            retval = system('apt-get -y install rsync')
        elif 'archlinux' in self.platforms:
            retval = system('sudo pacman -Sy rsync --noconfirm')

        if retval >> 8 == 0:
            return True

        return False


    def help(self):
        return "/usr/bin/rsync should be installed. But I don't how to"
