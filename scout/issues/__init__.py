#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filename   : __init__.py<2>
# created at : 2013-03-27 18:55:11
# author     : Jianing Yang <jianingy.yang AT gmail DOT com>

__author__ = 'Jianing Yang <jianingy.yang AT gmail DOT com>'

class BaseIssue(Exception):
    """
    Declare an issue
    """

    # unique identifier of this issue.
    # it should be a string.
    identifier = None

    # people who are resposible for this issue.
    # it should be a list of strings.
    contacts = None

    # documentation on details of this issue
    # it may contains a cause, a solution or a joke.
    # it should be a string
    detail = None

    # accessors go here
    def get_detail(self):
        return self.detail

    def get_contacts(self):
        return self.contacts

    def get_identifier(self):
        return self.identifier
