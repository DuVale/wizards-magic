# -*- coding: utf-8 -*-
import pygame
import globals
pygame.font.init()
class ElementShower(pygame.sprite.Sprite):
    def __init__(self):
        self.type = 'outer'
        self.font = pygame.font.Font("misc/Domestic_Manners.ttf", 12)
        self.init_text = self.font.render('',False,(0,0,0))
        pygame.sprite.Sprite.__init__(self)
    def draw(self):
        #self.image = self.surface_backup.copy()
        exec("text = self.font.render(str(globals.player.enemy" + "." + self.element + "_mana),True,(255,255,255))")
        #self.image.blit(text, (2, 9))
        globals.background.blit(text, self.rect)
    def update(self):
        self.draw()
class WaterElementShower(ElementShower):
    def __init__(self, rect):
        ElementShower.__init__(self)
        self.element = 'water'
        self.rect = self.init_text.get_rect().move((rect[0], rect[1]))
        globals.interface.add(self)
class FireElementShower(ElementShower):
    def __init__(self, rect):
        ElementShower.__init__(self)
        self.element = 'fire'
        self.rect = self.init_text.get_rect().move((rect[0], rect[1]))
        ElementShower.__init__(self)
        globals.interface.add(self)
class AirElementShower(ElementShower):
    def __init__(self, rect):
        ElementShower.__init__(self)
        self.element = 'air'
        self.rect = self.init_text.get_rect().move((rect[0], rect[1]))
        ElementShower.__init__(self)
        globals.interface.add(self)
class EarthElementShower(ElementShower):
    def __init__(self, rect):
        ElementShower.__init__(self)
        self.element = 'earth'
        self.rect = self.init_text.get_rect().move((rect[0], rect[1]))
        ElementShower.__init__(self)
        globals.interface.add(self)
class LifeElementShower(ElementShower):
    def __init__(self, rect):
        ElementShower.__init__(self)
        self.element = 'life'
        self.rect = self.init_text.get_rect().move((rect[0], rect[1]))
        ElementShower.__init__(self)
        globals.interface.add(self)
class DeathElementShower(ElementShower):
    def __init__(self, rect):
        ElementShower.__init__(self)
        self.element = 'death'
        self.rect = self.init_text.get_rect().move((rect[0], rect[1]))
        ElementShower.__init__(self)
        globals.interface.add(self)
class ElementButton(pygame.sprite.Sprite):
    def __init__(self):
        #Это прототип!
        self.type = 'button'
        self.surface_backup = self.image.copy()
        self.font = pygame.font.Font("misc/Domestic_Manners.ttf", 15)
        pygame.sprite.Sprite.__init__(self)
    def draw(self):
        self.image = self.surface_backup.copy()
        exec("text = self.font.render(str(globals.player" + "." + self.element + "_mana),True,"+self.color+")")
        self.image.blit(text, (2, 9))
        globals.background.blit(self.image, self.rect)
    def update(self):
        self.draw()
    def onmouse(self):
        pass
    def onmouseout(self):
        pass
    def onmousedown(self):
        exec('globals.'+globals.cards_of_element_shower_element+'_element_button.default()')
        globals.cards_in_deck.empty()
        globals.cards_of_element_shower_element = self.element
        self.image = self.image_pressed
        self.surface_backup = self.image.copy()
    def onmouseup(self):
        pass
    def default(self):
        self.image = self.image_normal
        self.surface_backup = self.image.copy()
class WaterElementButton(ElementButton):
    def __init__(self, rect):
        self.element = 'water'
        self.image_normal = pygame.image.load('misc/water_icon_big.gif').convert_alpha()
        self.image_pressed = pygame.image.load('misc/water_icon_big_selected.gif').convert_alpha()
        self.image = self.image_pressed
        self.color = '(255,255,255)'
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        ElementButton.__init__(self)
        globals.interface.add(self)
class FireElementButton(ElementButton):
    def __init__(self, rect):
        self.element = 'fire'
        self.image_normal = pygame.image.load('misc/fire_icon_big.gif').convert_alpha()
        self.image_pressed = pygame.image.load('misc/fire_icon_big_selected.gif').convert_alpha()
        self.image = self.image_normal
        self.color = '(255,255,255)'
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        ElementButton.__init__(self)
        globals.interface.add(self)
class AirElementButton(ElementButton):
    def __init__(self, rect):
        self.element = 'air'
        self.image_normal = pygame.image.load('misc/air_icon_big.gif').convert_alpha()
        self.image_pressed = pygame.image.load('misc/air_icon_big_selected.gif').convert_alpha()
        self.image = self.image_normal
        self.color = '(0,0,0)'
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        ElementButton.__init__(self)
        globals.interface.add(self)
class EarthElementButton(ElementButton):
    def __init__(self, rect):
        self.element = 'earth'
        self.image_normal = pygame.image.load('misc/earth_icon_big.gif').convert_alpha()
        self.image_pressed = pygame.image.load('misc/earth_icon_big_selected.gif').convert_alpha()
        self.image = self.image_normal
        self.color = '(0,0,0)'
        self.surface_backup = self.image.copy()
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        ElementButton.__init__(self)
        globals.interface.add(self)
class LifeElementButton(ElementButton):
    def __init__(self, rect):
        self.element = 'life'
        self.image_normal = pygame.image.load('misc/life_icon_big.gif').convert_alpha()
        self.image_pressed = pygame.image.load('misc/life_icon_big_selected.gif').convert_alpha()
        self.image = self.image_normal
        self.color = '(0,0,0)'
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        ElementButton.__init__(self)
        globals.interface.add(self)
class DeathElementButton(ElementButton):
    def __init__(self, rect):
        self.element = 'death'
        self.image_normal = pygame.image.load('misc/death_icon_big.gif').convert_alpha()
        self.image_pressed = pygame.image.load('misc/death_icon_big_selected.gif').convert_alpha()
        self.image = self.image_normal
        self.color = '(255,255,255)'
        self.rect = self.image.get_rect().move((rect[0], rect[1]))
        ElementButton.__init__(self)
        globals.interface.add(self)