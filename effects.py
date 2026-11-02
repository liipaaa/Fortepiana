from pygame import * 
from settings import *


def draw_key_effects(screen,rect,it_pressed=False):
    if not it_pressed:
        base_color=GREEN
    else:
        base_color=GREEN_DARK

    border_color = PURPLE
    draw.rect(screen< base_color, rect, border_radius=8)
    draw.rect(screen, border_color, rect, 2, border_radius=8)