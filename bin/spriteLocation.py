#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SpriteLocation(object):
	"""Espifica la posicion de sprite dentro del sheet"""
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
