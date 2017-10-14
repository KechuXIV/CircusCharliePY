#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys


class ICollisionManager(object):

	def getCollisions(self):
		raise NotImplementedError("Should have implemented this")
