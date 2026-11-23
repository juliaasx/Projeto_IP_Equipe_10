import pygame

from constants import BLOCK_SIZE, OBSTACLE_COLOR
from classes.game_object import GameObject
from utils.helpers import load_image


class Platform(GameObject):
    """Bloco suspenso. Da pra subir em cima e bater a cabeca por baixo.
    O bloco '?' solta uma vacina na primeira cabecada."""

