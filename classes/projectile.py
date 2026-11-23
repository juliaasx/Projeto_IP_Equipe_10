import pygame

from constants import PROJECTILE_HEIGHT, PROJECTILE_SPEED, PROJECTILE_WIDTH, SCREEN_WIDTH
from classes.game_object import GameObject
from utils.helpers import load_image


class Projectile(GameObject):
    """Vacina arremessada pelo Ze Gotinha."""
