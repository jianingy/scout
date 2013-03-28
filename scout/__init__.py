#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : __init__.py<4>
# created at : 2013-03-27 20:47:37
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

from scout.exceptions import InvalidPlugin, NotImplement
from scout.issues import BaseIssue

class Scout(object):

    platforms = []
    issues = []

    def __init__(self, verbose=False, colorful=False):
        self.root = self.locate_root()
        self.verbose_ = verbose
        self.colorful = colorful

    def color(self, s, color):
        if self.colorful:
            content = dict(start='\033[%sm' % color,
                           content=s,
                           end='\033[0m')
            return "%(start)s%(content)s%(end)s" % content
        else:
            return s

    def verbose(self, s):
        if self.verbose_:
            print self.color('INFO:', 33), s

    def info(self, s):
        print self.color('INFO:', 32), s

    def warn(self, s):
        print self.color('WARN:', 31), s

    def fatal(self, s):
        print self.color('FATAL:', 41), s

    def locate_root(self):
        from os.path import dirname, abspath
        from sys import argv as ARGV
        return abspath(dirname(ARGV[0]))

    def list_plugins(self, class_):
        from os import listdir
        from os.path import join as path_join, splitext

        sub = self.__class__.__name__.lower()

        def _cond(x):
            return x not in ['__init__.py'] and x.endswith('.py')

        plugins = filter(_cond, listdir(path_join(self.root, sub, class_)))
        return map(lambda x: splitext(x)[0], plugins)

    def import_(self, name):
        mod = __import__(name)
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    def get_platforms(self):
        for plugin in self.list_plugins('platforms'):
            plugin = '.'.join(['scout', 'platforms', plugin])
            try:
                p = self.import_(plugin)
                platform = p.detect()
                if platform and isinstance(platform, list):
                    self.platforms.extend(platform)
                elif platform:
                    raise InvalidPlugin('plugin %s should return a list of string' % plugin)
            except NotImplement:
                self.error('%s is immature' % plugin)
            except Exception:
                raise

        return self.platforms

    def inspect(self):
        for plugin in self.list_plugins('inspectors'):
            plugin = '.'.join(['scout', 'inspectors', plugin])
            try:
                p = self.import_(plugin)
                inspector = p.Inspector()
                if inspector.appropriate(self.platforms):
                    self.verbose('%s: started' % plugin)
                    inspector.detect()
                    self.verbose('%s: check ok' % plugin)
            except BaseIssue as e:
                self.issues.append(e)
            except NotImplement:
                self.error('%s is immature' % plugin)
            except Exception:
                raise

        return self.platforms


    def fix(self):
        for plugin in self.list_plugins('automaton'):
            plugin = '.'.join(['scout', 'automaton', plugin])
            try:
                p = self.import_(plugin)
                automata = p.Automaton(self.platforms, self.issues)
                if automata.appropriate():
                    self.verbose('%s: started' % plugin)
                    if automata.fix():
                        self.verbose('%s: fixed' % plugin)
                    else:
                        self.warn('%s: %s' % (plugin, automata.help()))
            except BaseIssue as e:
                self.issues.append(e)
            except NotImplement:
                self.error('%s is immature' % plugin)
            except Exception:
                raise

        return self.platforms
