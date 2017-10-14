#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GameElement(object):

	def __init__(self,
			spriteManager,
			soundManager,
			screenCords,
			collisionManager,
			speed,
			measure):
		self._collisionManager = collisionManager
		self._spriteManager = spriteManager
		self._soundManager = soundManager
		self._measure = measure
		self._speed = speed
		self.__screenCords = screenCords

	def getSound(self, path):
		return self._soundManager.getSound(path)

	def getSprite(self):
		return self._spriteManager.getSprite()

	def createSprite(self, position):
		self._spriteManager.createSprite(position.X, position.Y, 
			self._measure.X, self._measure.Y)

	def _flipSpriteImage(self):
		return self._spriteManager.flipSpriteImage()

	def updateImage(self, imagePath, isGoingLeft):
		self.__updateSpriteImage(imagePath)
		if(not isGoingLeft):
			self._flipSpriteImage()

	def updateSpritePosition(self, position):
		return self._spriteManager.updateSprite(position.X, position.Y)
		
	def __updateSpriteImage(self, imagePath):
		return self._spriteManager.updateSpriteImage(imagePath)
