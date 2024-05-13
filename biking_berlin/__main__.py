"""
In this __main__.py file the main_game_loop() is called.
"""

import os
import pygame
import json
import logging
import sys
from pygame.locals import *

from init.initial_settings import InitialSettings


def initialize_pygame():
    """
    TODO: !This is just a placeholder and need to be changed later on!
    """
    # Set up Pygame
    pygame.init()

    #TODO: Load gameplay information

    #TODO: Load images
    #screen = pygame.display.get_surface()
    #biking_berlin_image_base_path = os.path.join('biking_berlin', 'images')
    #biking_berlin_placeholder_filename = os.path.join(biking_berlin_image_base_path, 'entry_point_placeholder.png')
    #biking_berlin_entry_point = pygame.image.load(biking_berlin_placeholder_filename)
    #screen.blit(biking_berlin_entry_point, (0, 0))
    #pygame.display.flip()

    #TODO: Load music

    #TODO: Play little video before drawing the start menu - video can be ended by pressing ESC or double clicking with left mouse key
     
    # Draw start menu
    rect_array = draw_start_menu()
    return rect_array


def draw_start_menu():
    # Load configuration data from JSON file
    config_base_path = os.path.join("biking_berlin", "config")
    config_menu_path = os.path.join(config_base_path, "menu.json")
    with open(config_menu_path, "r") as f:
        config = json.load(f)
        
    # Window settings
    WIDTH = config["window"]["width"]
    HEIGHT = config["window"]["height"]
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(config["window"]["title"])

    BLACK = tuple(config["colors"]["background"])
    WHITE = tuple(config["colors"]["text"])
    GRAY = tuple(config["colors"]["button_start_menu"])

    # Define button properties
    BUTTON_WIDTH = config["button_start_menu"]["width"]
    BUTTON_HEIGHT = config["button_start_menu"]["height"]
    BUTTON_GAP = config["button_start_menu"]["gap"]
    font = pygame.font.Font(None, config["button_start_menu"]["font_size"])

    # Define button texts
    button_texts = config["texts"]

    # Calculate button positions
    button_positions = []
    total_height = BUTTON_HEIGHT * len(button_texts) + BUTTON_GAP * (len(button_texts) - 1)
    start_y = (HEIGHT - total_height) // 2
    for i in range(len(button_texts)):
        button_positions.append((WIDTH // 2 - BUTTON_WIDTH // 2, start_y + i * (BUTTON_HEIGHT + BUTTON_GAP)))

    # Clear the window
    window.fill(BLACK)

    # Draw buttons
    rect_array = []
    for i, text in enumerate(button_texts):
        rect = pygame.Rect(button_positions[i], (BUTTON_WIDTH, BUTTON_HEIGHT))
        pygame.draw.rect(window, GRAY, rect)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = rect.center
        window.blit(text_surface, text_rect)
        rect_dictionary = dict(text = text, rect = rect)
        rect_array.append(rect_dictionary)

    # Update the display
    pygame.display.update()
    return rect_array

#TODO: Add further state to ensure the pause key is only causing an action when the game is running and not when a menu is open
#TODO: Ask if game shall be quit when ESC is pressed, if left mouse key presses button or ESC key are pressed, quit game 
def user_interrupt(running, paused, events):
    for event in events:
        if event.type == QUIT:
            #sys.exit(0)
            print('Quit')
            running = False
        if event.type == KEYDOWN:
            if (event.key == K_q) or (event.key == K_ESCAPE):
                print('Quit')
                running = False
            elif (event.key == K_p) or (event.key == K_PAUSE):
                paused = not paused  # Toggle the paused flag
                if paused:
                    print('Pause')
                else:
                    print('Unpause')
        else:
            print(event)
    return running, paused

#TODO: Add actions for different buttons clicked
def  start_menu_handler(rect_array, running):
    """Handle button click (start menu)"""
    mouse_pos = pygame.mouse.get_pos()
    for button in rect_array:
        rect = button["rect"]
        text = button["text"]
        if rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            match text:
                case "Start Game":
                    print(f"Button '{text}' clicked!")
                case "Options":
                    print(f"Button '{text}' clicked!")
                case "Leaderboard":
                    print(f"Button '{text}' clicked!")
                case "Quit":
                    print(f"Button '{text}' clicked!")
                    running = False
                case _:
                    print(f"To be done!")
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

    running = True
    paused = False

    # Initialize the game
    rect_array = initialize_pygame()

    # Game loop
    while running:

        # Handle button click (start menu)
        running = start_menu_handler(rect_array, running)
        
        events = pygame.event.get()
        running, paused = user_interrupt(running, paused, events)

        #if paused:
        #    print("Game is paused - add image for unpausing and don't update the game")
        #else:
        #    print("This should be the regular case")

    pygame.quit()
    

'''
Calling the main game loop
'''
main_game_loop()
