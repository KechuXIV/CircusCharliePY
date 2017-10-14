#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import unittest
import uuid

sys.path.insert(0, os.path.join('bin', ))

from mock import Mock, MagicMock, call, NonCallableMock, patch
from gameElement import GameElement
from iSoundManager import ISoundManager
from iSpriteManager import ISpriteManager
from iCollisionManager import ICollisionManager

class test_gameElement(unittest.TestCase):

    def setUp(self):
		self.spriteManager = Mock(spec=ISpriteManager)
		self.soundManager = Mock(spec=ISoundManager)
		self.collisionManager = Mock(spec=ICollisionManager)
		self.target = GameElement(self.spriteManager, 
            self.soundManager,
            None,
            self.collisionManager,
            None,
            None)

    def test_getSound(self):
        expect = uuid.uuid4()
        self.soundManager.getSound.return_value = expect
        result = self.target.getSound(uuid.uuid4())
        self.assertEqual(expect, result)

    def test_getSprite(self):
        expect = uuid.uuid4()

if __name__ == "__main__":
    unittest.main()