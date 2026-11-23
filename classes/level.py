import pygame

from constants import (BLOCK_SIZE, ENEMY_KINDS, ITEM_KINDS, GROUND_Y, ITEM_SIZE, LEVEL_TIME, LEVELS, PLAYER_X,
                       PLATFORM_Y, QUESTION_CHANCE, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED_GAIN)
from classes.coin import Item
from classes.enemy import Enemy
from classes.goal import Goal
from classes.obstacle import Obstacle
from classes.platform import Platform
from classes.popup import Popup
from classes.projectile import Projectile
from classes.player import Player
from utils.collision import check_collision
from utils.helpers import load_image, random_choice, random_float, random_int, seed_random

ITEM_CHOICES = ["vaccine", "syringe", "drop"]


class Level:
    """Uma fase: gera blocos, obstaculos, virus e itens, e controla tempo e UPA."""
