import pygame

from constants import MAX_LIVES, SCREEN_WIDTH
from classes.text import Text
from utils.helpers import load_image

HUD_HEIGHT = 50


class Hud:
    """Barra do topo: vida, vacinas e tempo (igual a imagem de referencia)."""
