import pygame

from constants import GROUND_Y, OBSTACLE_COLOR
from classes.game_object import GameObject
from utils.helpers import load_image


class Obstacle(GameObject):
    """Bloco no chao. Da pra pular por cima dele; bater de lado tira vida."""

