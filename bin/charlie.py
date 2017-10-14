#!/usr/bin/env python
# -*- coding: utf-8 -*-


from gameElement import GameElement
from point import Point

class Charlie(GameElement):

	def __init__(self,
		spriteManager,
		soundManager,
		screenCords,
		collisionManager,
		speed,
		measure):
		GameElement.__init__(self,
			spriteManager,
			soundManager,
			screenCords,
			collisionManager,
			speed = Point(4, 6),
			measure = Point(30, 30))

	def motion(self):
		cosa = GameElement._getSound("asd")
		#print("asd")
		#print(GameElement.Cosa())
		#print("rjt")
		return cosa