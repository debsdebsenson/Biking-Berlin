"""
In this __main__.py file the main_game_loop() is called.
"""

import os
import pygame
import logging
import sys
from pygame.locals import *

from init.initial_settings import InitialSettings


def initialize_pygame():
    """
    TBD: !This is just a placeholder and need to be changed later on!
    """
    # Set up Pygame
    pygame.init()

    window = pygame.display.set_mode((1700, 800))
    pygame.display.set_caption('Biking Berlin')
    screen = pygame.display.get_surface()
    biking_berlin_placeholder_filename = os.path.join("images", "entry_point_placeholder.png")
    biking_berlin_entry_point = pygame.image.load(biking_berlin_placeholder_filename)
    screen.blit(biking_berlin_entry_point, (0, 0))
    pygame.display.flip()


def user_interrupt(running, events):
    for event in events:
        if event.type == QUIT:
            #sys.exit(0)
            print('Quit')
            running = False
        if event.type == KEYDOWN:
            if (event.key == K_q) or (event.key == K_ESCAPE):
                print('Quit')
                running = False
        else:
            print(event)
    return running


def main_game_loop() -> None:

    """main game loop: main_game_loop()"""
    print("A lot of work has to be done before this is working properly")
    try:
        InitialSettings()
    except Exception as init_exception:
        logging.exception(init_exception)
    else:
        print("Initial settings loaded")
    finally:
        pass

    # Game loop
    running = True
    while running:
        running = user_interrupt(running, pygame.event.get())
    pygame.quit()
    

'''
Calling the main game loop
'''
initialize_pygame()
main_game_loop()
