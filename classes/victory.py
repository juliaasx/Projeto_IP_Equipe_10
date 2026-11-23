import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, VIDEO_FPS
from classes.text import Text
from utils.helpers import load_video_frames, play_music, random_choice, random_float, random_int, stop_music, wave

CONFETTI_COLORS = [(255, 90, 90), (255, 220, 70), (90, 200, 255), (120, 230, 120), (255, 255, 255)]


class Victory:
    """Tela de quando o Ze chega na UPA: passa o video do Ze dancando o funk da vacina."""

    