# -*- coding: utf-8 -*-
import pygame.sprite
#Copyright (C) 2011  сhubakur
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# To change this template, choose Tools | Templates
# and open the template in the editor.
#import pygame.sprite
__author__="chubakur"
__date__ ="$12.02.2011 12:11:42$"
import pygame
from pygame.locals import *
import sys
import cards
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Wizards Magic')
clock = pygame.time.Clock()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))
panels = pygame.sprite.Group()
interface = pygame.sprite.Group()
upper_interface = pygame.sprite.Group()
current_player = 1 #id игрока, который ходит
cards_of_element_shower = False #показывать или не показывать окно с выбором карты выбранной стихии
cards_of_element_shower_element = "" #какой элемент показывать
font = pygame.font.Font(None, 20)
font.set_bold(0)
#class GameParams():
    #def __init__(self):
       # self.current_player = 1
#game_params = GameParams()
class Player(): #Прототип игрока
    def __init__(self):
        pass
    def get_mana(self):
        self.water_mana = random.randint(1,6)
        self.fire_mana = random.randint(1,6)
        self.air_mana = random.randint(1,6)
        self.earth_mana = random.randint(1,6)
        self.life_mana = random.randint(1,6)
        self.death_mana = random.randint(1,6)
    def get_cards(self):
        self.water_cards = []
        self.fire_cards = []
        self.air_cards = []
        self.earth_cards = []
        self.life_cards = []
        self.death_cards = []
        for i in xrange(0,4):
             #получаем карту элемента воды
             randnum = random.randint(0,len(cards.water_cards)-1)
             self.water_cards.append(cards.water_cards[randnum])
             exec("self."+cards.water_cards[randnum].lower()+"=cards."+cards.water_cards[randnum]+"()")
             cards.water_cards.remove(cards.water_cards[randnum])
             #Элемент огня
             randnum = random.randint(0,len(cards.fire_cards)-1)
             self.fire_cards.append(cards.fire_cards[randnum])
             exec("self."+cards.fire_cards[randnum].lower()+"=cards."+cards.fire_cards[randnum]+"()")
             cards.fire_cards.remove(cards.fire_cards[randnum])
             #Элемент воздуха
             randnum = random.randint(0,len(cards.air_cards)-1)
             self.air_cards.append(cards.air_cards[randnum])
             exec("self."+cards.air_cards[randnum].lower()+"=cards."+cards.air_cards[randnum]+"()")
             cards.air_cards.remove(cards.air_cards[randnum])
             #Элемент земли
             randnum = random.randint(0,len(cards.earth_cards)-1)
             self.earth_cards.append(cards.earth_cards[randnum])
             exec("self."+cards.earth_cards[randnum].lower()+"=cards."+cards.earth_cards[randnum]+"()")
             cards.earth_cards.remove(cards.earth_cards[randnum])
             #Элемент жизни
             randnum = random.randint(0,len(cards.life_cards)-1)
             self.life_cards.append(cards.life_cards[randnum])
             exec("self."+cards.life_cards[randnum].lower()+"=cards."+cards.life_cards[randnum]+"()")
             cards.life_cards.remove(cards.life_cards[randnum])
             #Элемент смерти
             randnum = random.randint(0,len(cards.death_cards)-1)
             self.death_cards.append(cards.death_cards[randnum])
             exec("self."+cards.death_cards[randnum].lower()+"=cards."+cards.death_cards[randnum]+"()")
             cards.death_cards.remove(cards.death_cards[randnum])
class Player1(Player):
    def __init__(self):
        self.health = 50
        self.id = 1
        self.get_cards()
        self.get_mana()
class Player2(Player):
    def __init__(self):
        self.health = 50
        self.id = 2
        self.get_cards()
        self.get_mana()
player1 = Player1()
player2 = Player2()
#class ElementsWindow(pygame.sprite.Sprite):
#    def __init__(self,rect,panel):
#        pygame.sprite.Sprite.__init__(self)
#        self.panel = panel
#        self.type = 'elementswindow'
#        self.player = panel.player
#        self.image = pygame.image.load('misc/elements.gif').convert_alpha()
#        self.relative_rect = self.image.get_rect().move((rect[0],rect[1])) #Координаты относительные к поверхности-родителю
#        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
#        interface.add(self)
#    def draw(self):
#        self.panel.image.blit(self.image,self.relative_rect)
#    def update(self):
#        self.draw()
class CardsOfElementShower(pygame.sprite.Sprite):
    #Не прототип!
    def __init__(self,rect,player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.type = 'cardsofelementshower'
        self.image = pygame.image.load('misc/cards_box.gif').convert_alpha()
        self.rect = self.image.get_rect().move((rect[0],rect[1]))
        self.cards = 0
        self.shift = 32
        interface.add(self)
    def draw(self):
        background.blit(self.image,self.rect)
    def update(self):
        if not cards_of_element_shower:
            upper_interface.empty()
            return
        if self.player != current_player:
            return
        self.cards = 0
        if self.player == 1:
            if cards_of_element_shower_element == "water":
                for card in player1.water_cards:
                    exec( "upper_interface.add(player1."+card.lower()+")")
                    #shift+=192
            elif cards_of_element_shower_element == "fire":
                for card in player1.fire_cards:
                    exec( "upper_interface.add(player1."+card.lower()+")")
            elif cards_of_element_shower_element == "air":
                for card in player1.air_cards:
                    exec( "upper_interface.add(player1."+card.lower()+")")
            elif cards_of_element_shower_element == "earth":
                for card in player1.earth_cards:
                    exec( "upper_interface.add(player1."+card.lower()+")")
            elif cards_of_element_shower_element == "life":
                for card in player1.life_cards:
                    exec( "upper_interface.add(player1."+card.lower()+")")
            else:
                for card in player1.death_cards:
                    exec( "upper_interface.add(player1."+card.lower()+")")
        else:
            if cards_of_element_shower_element == "water":
                for card in player2.water_cards:
                    exec( "upper_interface.add(player2."+card.lower()+")")
            elif cards_of_element_shower_element == "fire":
                for card in player2.fire_cards:
                    exec( "upper_interface.add(player2."+card.lower()+")")
            elif cards_of_element_shower_element == "air":
                for card in player2.air_cards:
                    exec( "upper_interface.add(player2."+card.lower()+")")
            elif cards_of_element_shower_element == "earth":
                for card in player2.earth_cards:
                    exec( "upper_interface.add(player2."+card.lower()+")")
            elif cards_of_element_shower_element == "life":
                for card in player2.life_cards:
                    exec( "upper_interface.add(player2."+card.lower()+")")
            else:
                for card in player2.death_cards:
                    exec( "upper_interface.add(player2."+card.lower()+")")
        self.draw()
class CompleteTheCourseButton(pygame.sprite.Sprite):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'completethecoursebutton'
        self.player = panel.player
        self.image = pygame.image.load('misc/complete_the_course.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
    def draw(self):
        if not self.player == current_player:
            return
        self.panel.image.blit(self.image,self.relative_rect)
    def update(self):
        self.draw()
class ElementButton(pygame.sprite.Sprite):
    def __init__(self):
        #Это прототип!
        pass
    def draw(self):
        self.panel.image.blit(self.image,self.relative_rect)
        font.set_bold(0)
        exec("text = font.render(str(player"+str(self.player)+"."+self.element+"_mana),True,(255,255,255))")
        self.image.blit(text,(5,16))
    def update(self):
        self.draw()
class WaterElementButton(ElementButton):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'water'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_water.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
class FireElementButton(ElementButton):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'fire'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_fire.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
class AirElementButton(ElementButton):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'air'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_air.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
class EarthElementButton(ElementButton):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'earth'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_earth.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
class LifeElementButton(ElementButton):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'life'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_life.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
class DeathElementButton(ElementButton):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'elementbutton'
        self.element = 'death'
        self.player = panel.player
        self.image = pygame.image.load('misc/elements_death.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
class HealthWindow(pygame.sprite.Sprite):
    def __init__(self,rect,panel):
        pygame.sprite.Sprite.__init__(self)
        self.panel = panel
        self.type = 'healthwindow'
        self.player = panel.player
        self.image = pygame.image.load('misc/health_window.gif').convert_alpha()
        self.relative_rect = self.image.get_rect().move((rect[0],rect[1]))
        self.rect = self.relative_rect.move(self.panel.rect[0],self.panel.rect[1])
        interface.add(self)
        self.font = pygame.font.Font(None, 22)
    def draw(self):
        self.panel.image.blit(self.image,self.relative_rect)
        if self.player == 1:
            text = self.font.render(str(player1.health),True,(255,255,255))
        else:
            text = self.font.render(str(player2.health),True,(255,255,255))
        self.image.blit(text, (25,5))
    def update(self):
        self.draw()
class Cardbox(pygame.sprite.Sprite):
    def __init__(self,rect,player):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'cardbox'
        self.player = player #первый или второй
        self.image = pygame.image.load('misc/cardbox_bg.gif').convert()
        self.rect = self.image.get_rect().move((rect[0],rect[1]))
        panels.add(self)
    def draw(self):
        background.blit(self.image,self.rect)
    def update(self):
        self.draw()
class Infopanel(pygame.sprite.Sprite):
    def __init__(self,rect,player):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'infopanel'
        self.player = player
        #self.image = pygame.Surface((screen.get_size()[0],screen.get_size()[1]/25))
        self.image = pygame.image.load('misc/infopanel_bg.gif').convert_alpha()
        #self.image.convert()
        #self.image.fill((0,0,255))
        self.rect = self.image.get_rect().move((rect[0],rect[1]))
        panels.add(self)
    def draw(self):
        background.blit(self.image,self.rect)
    def update(self):
        self.draw()
class Actionpanel(pygame.sprite.Sprite):
    def __init__(self,rect,player):
        pygame.sprite.Sprite.__init__(self)
        self.type = 'actionpanel'
        self.player = player
        #self.image = pygame.Surface((screen.get_size()[0],screen.get_size()[1]/20))
        self.image = pygame.image.load('misc/actionpanel_bg.gif').convert()
        #self.image.convert()
        #self.image.fill((0,255,0))
        self.rect = self.image.get_rect().move((rect[0],rect[1]))
        panels.add(self)
    def draw(self):
        background.blit(self.image,self.rect)
    def update(self):
        self.draw()
class Point(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('misc/point_alpha.gif').convert_alpha()
        self.rect = self.image.get_rect()
    def draw(self,rect):
        background.blit(self.image,rect)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(rect)
point = Point()
#test = pygame.image.load('misc/cards/1.gif').convert_alpha()
class Event_handler():
    def __init__(self):
        pass
    def event(self,event):
        if event.type == QUIT:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            global cards_of_element_shower
            if event.button == 1:
                global current_player
                #self.point.rect = self.point.get_rect()
                point.draw(event.pos)
                #collided = pygame.sprite.spritecollide(point, interface_up_layer, 0)
                #if not collided:
                    #collided = pygame.sprite.spritecollide(point, interface, 0)
                    #if not collided:
                        #return
                collided = pygame.sprite.spritecollide(point, upper_interface, 0)
                if not collided:
                    collided = pygame.sprite.spritecollide(point, interface, 0)
                if not collided:
                    return
                item = collided[len(collided)-1]
                print item
                if item.type == "card":
                    return
                if item.player!=current_player:
                    return
                if item.type == 'elementbutton':
                    global cards_of_element_shower_element
                    cards_of_element_shower = 1
                    if item.element == 'water':
                        cards_of_element_shower_element = "water"
                    elif item.element == 'fire':
                        cards_of_element_shower_element = "fire"
                    elif item.element == 'air':
                        cards_of_element_shower_element = "air"
                    elif item.element == 'earth':
                        cards_of_element_shower_element = "earth"
                    elif item.element == 'life':
                        cards_of_element_shower_element = "life"
                    elif item.element == 'death':
                        cards_of_element_shower_element = "death"
                elif item.type == 'completethecoursebutton':
                    cards_of_element_shower = 0
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
            elif event.button == 3:
                point.draw(event.pos)
                collided = pygame.sprite.spritecollide(point,upper_interface,0)
                if not collided:
                    collided = pygame.sprite.spritecollide(point, interface, 0)
                if not collided:
                    return
                item = collided[len(collided)-1]
                if item.type == 'cardsofelementshower':
                    cards_of_element_shower = 0
                #print current_player
                #elif item.type == 'completethecoursebutton':
                    #if current_player == 1:
                        #current_player = 2
                    #else:
                        #current_player = 1
                #print collided[len(collided)-1]
                #if collided[len(collided)-1].type == "cardbox":
                    #pass
                    #collided[len(collided)-1].image.blit(test,(0,0))
                #for elem in pygame.sprite.spritecollide(point, interface, 0):
                 #print  elem,elem.player
                #print event
event_handler = Event_handler()
infopanel1 = Infopanel((0,0),1) #Инициализация панели верхнего игрока
infopanel2 = Infopanel((0,545),2) #Инициализация панели нижнего игрока
actionpanel1 = Actionpanel((0,25),1) #Панель с кнопками верхнего игрока
actionpanel2 = Actionpanel((0,570),2) #Панель с кнопками нижнего игрока
# 0 1 2 3 4   //Расположение
# 5 6 7 8 9
Cardbox((0,55),1) #0 место на поле
Cardbox((160,55),1) #1 место на поле
Cardbox((320,55),1) #2 место на поле
Cardbox((480,55),1) #3 место на поле
Cardbox((640,55),1) #4 место на поле
Cardbox((0,301),2) #5 место на поле
Cardbox((160,301),2) #6 место на поле
Cardbox((320,301),2) #7 место на поле
Cardbox((480,301),2) #8 место на поле
Cardbox((640,301),2) #9 место на поле
#exec('Cardbox((640,301),2)')
#ElementsWindow((0,0),actionpanel1)
#ElementsWindow((0,0),actionpanel2)
HealthWindow((0,0),infopanel1) #Окошко здоровья верхнего игрока
HealthWindow((0,0),infopanel2) #Окошко здоровья нижнего игрока
# Кнопки колод стихий первого игрока
WaterElementButton((0,0),actionpanel1)
FireElementButton((31,0),actionpanel1)
AirElementButton((62,0),actionpanel1)
EarthElementButton((93,0),actionpanel1)
LifeElementButton((124,0),actionpanel1)
DeathElementButton((155,0),actionpanel1)
# Кнопки колод стихий второго игрока
WaterElementButton((0,0),actionpanel2)
FireElementButton((31,0),actionpanel2)
AirElementButton((62,0),actionpanel2)
EarthElementButton((93,0),actionpanel2)
LifeElementButton((124,0),actionpanel2)
DeathElementButton((155,0),actionpanel2)
#Кнопки завершения хода первого и второго игрока.
CompleteTheCourseButton((760,0),actionpanel1)
CompleteTheCourseButton((760,0),actionpanel2)
#Окна выбора карты стихии
cardsofelementshower1 = CardsOfElementShower((0,301),1)
cardsofelementshower2 = CardsOfElementShower((0,55),2)
#********************************************************************************
screen.blit(background,(0,0))
panels.update()
interface.update()
#interface_up_layer.update()
#for elem in interface.sprites():
    #print elem.type
    #print elem.type,elem.rect,elem.rect[0]+elem.image.get_size()[0],elem.rect[1]+elem.image.get_size()[1]
pygame.display.flip()
while 1:
    for event in pygame.event.get():
        event_handler.event(event)
    panels.update()
    interface.update()
    if current_player == 1:
        upper_interface.update(cardsofelementshower1)
    else:
        upper_interface.update(cardsofelementshower2)
    #interface_up_layer.update()
    screen.blit(background,(0,0))
    background.fill((0,0,0))
    pygame.display.flip()
    clock.tick(20)