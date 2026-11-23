import pygame

from constants import GROUND_Y
from classes.game_object import GameObject
from classes.text import Text
from utils.helpers import load_image


class Goal(GameObject):
    """UPA 24h: chegar nela termina a fase."""
