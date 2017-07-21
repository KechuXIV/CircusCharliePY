#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
import sys

pygame.init()

def createNewSprite(xPosition, yPosition, width, height, imagePath, imageX, imageY, imageWidth, imageHeigth):
	newSprite = pygame.sprite.Sprite()
	newSprite.image = pygame.transform.scale(pygame.image.load(imagePath), (width, height))
	newSprite.rect = pygame.Rect((xPosition, yPosition), (width, height))

	return newSprite

screen = pygame.display.set_mode((600, 360))
pygame.display.set_caption("CircusCharliePY")

__resourcePath = os.path.join('CircusCharliePY', 'bin', 'resources')
path = os.path.join(__resourcePath, 'CircusCharlieSprite.gif')

sheet = pygame.image.load(path) #Load the sheet

sheet.set_clip(pygame.Rect(76, 7, 16, 22)) #Locate the sprite you want
draw_me = sheet.subsurface(sheet.get_clip()) #Extract the sprite you want

backdrop = pygame.Rect(0, 0, 0, 0) #Create the whole screen so you can draw on it

screen.blit(draw_me,backdrop) #'Blit' on the backdrop

allSprites = pygame.sprite.Group()

clock = pygame.time.Clock()

r = 0

FPS = 120

def checkQuitEvent():
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()

def draw():
	clearScreen()
	global r
	if r == 1:
		r = 0
		sheet.set_clip(pygame.Rect(76, 7, 16, 22)) #Locate the sprite you want
		draw_me = sheet.subsurface(sheet.get_clip()) #Extract the sprite you want
	else:
		r = r + 1
		sheet.set_clip(pygame.Rect(97, 5, 16, 24)) #Locate the sprite you want
		draw_me = sheet.subsurface(sheet.get_clip()) #Extract the sprite you want

	screen.blit(draw_me,backdrop) #'Blit' on the backdrop
	updateWindow()

def clearScreen():
	screen.fill((0,0,0))

def updateWindow():
	pygame.display.flip()

def logic():
	pass

while True:
	checkQuitEvent()
	logic()
	draw()
	clock.tick(FPS)
