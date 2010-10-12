#!/usr/bin/env python
#coding:utf-8
# Author:  mozman --<mozman@gmx.at>
# Purpose: svg types
# Created: 30.09.2010
# Copyright (C) 2010, Manfred Moitzi
# License: GPLv3

class SVGAttribute(object):
    def __init__(self, name, anim, types, const):
        self.name = name
        self._anim = anim
        self._types = types
        self._const = const

    def get_anim(self, elementname='*'):
        return self._anim
    def get_types(self, elementname='*'):
        return self._types
    def get_const(self, elementname='*'):
        return self._const

class SVGMultiAttribute(object):
    # exmple: SVGMultiAttribute('*'=SVGAttribute(...), 'text'=SVGAttribute(...))
    def __init__(self, name, **attributes):
        self.name = name
        self._attributes = attributes

    def get_attribute(self, elementname):
        if elementname in self._attributes:
            return self._attributes[elementname]
        else:
            return self._attributes['*']

    def get_anim(self, elementname='*'):
        attribute = self.get_attribute(elementname)
        return attribute.get_anim()

    def get_types(self, elementname='*'):
        attribute = self.get_attribute(elementname)
        return attribute.get_types()

    def get_const(self, elementname='*'):
        attribute = self.get_attribute(elementname)
        return attribute.get_const()


class SVGElement(object):
    def __init__(self, name, attributes, properties, children):
        self.name = name
        s = set()
        if attributes:
            s.update(attributes)
        if properties:
            s.update(properties)
        self.valid_attributes = frozenset(s)
        s =set()
        if children:
            s.update(children)
        self.valid_children = frozenset(s)