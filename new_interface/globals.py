# -*- coding: utf-8 -*-
import pygame

pygame.font.init()
panels = pygame.sprite.Group() #Нижний уровень
interface = pygame.sprite.Group() #Уровень кнопок
cards_in_deck = pygame.sprite.Group() #Уровень дополнительный
ccards_1 = pygame.sprite.Group() #  Карты, которые вывел первый игрок
ccards_2 = pygame.sprite.Group() # Карты, которые вывел второй игрок
magic_cards = pygame.sprite.Group() #Использующаяся магия
card_info_group = pygame.sprite.Group() #  Группа, которая содержит спрайт, содержащий панель вывода информации о карте
information_group = pygame.sprite.Group() #Группа, содержащая панель вывода игровой информации
menu_group = pygame.sprite.Group() # menu items
font = pygame.font.Font("misc/Domestic_Manners.ttf", 15)
#print pygame.font.match_font('Arial')
cards_of_element_shower_element = "water" #какой элемент показывать
selected_card = False #Выбранная карта
screen = None
player = None
player1 = None
player2 = None
#Каст с выбором цели
cast_focus = False #включен ли режим
cast_focus_wizard = None # ссылка на кастующий объект ( не цель ! )
#cast_focus_filter = None
stage=0 # 0=Menu 1=Single player game 2=network game
question=False # when true disable all events but key stroke
answer="" #buffer to store key strokes
answer_maxchar=0 # max number of characters we are waiting for
answer_cmd="" #function to execute when stoke ENTER
def clean():
	cards_of_element_shower_element = "water" #какой элемент показывать
	selected_card = False #Выбранная карта
	screen = None
	player = None
	player1 = None
	player2 = None
	#Каст с выбором цели
	cast_focus = False #включен ли режим
	cast_focus_wizard = None # ссылка на кастующий объект ( не цель ! )
	question=False # when true disable all events but key stroke
	answer="" #buffer to store key strokes
	answer_cmd="" #function to execute when stoke ENTER

	panels.empty()
	interface.empty()
	cards_in_deck.empty()
	ccards_1.empty()
	ccards_2.empty()
	magic_cards.empty()
	card_info_group.empty()
	#information_group.empty()
	menu_group.empty()

