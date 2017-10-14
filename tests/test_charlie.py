#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest

sys.path.insert(0, os.path.join('bin', ))

from mock import Mock, MagicMock, call, NonCallableMock, patch
from charlie import Charlie
from iSoundManager import ISoundManager
from iSpriteManager import ISpriteManager
from iCollisionManager import ICollisionManager

class test_charlie(unittest.TestCase):

	def setUp(self):
		self.spriteManager = Mock(spec=ISpriteManager)
		self.soundManager = Mock(spec=ISoundManager)
		self.collisionManager = Mock(spec=ICollisionManager)

		self.target = Charlie(self.spriteManager,
			self.soundManager,
			None,
			self.collisionManager,
			None,
			None)

	@patch('charlie.GameElement')
	def test_motion(self, mock_GameElement):
		mock_GameElement._getSound.return_value = "pija2"
		cosa = self.target.motion()
		self.assertEqual("pija2", cosa)

if __name__ == "__main__":
    unittest.main()