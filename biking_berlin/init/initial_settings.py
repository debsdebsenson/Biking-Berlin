"""
In this file initial settings are set, file pathes are created
"""

# Standard library imports
#from curses import window
#from turtle import window_height, window_width
#from typing_extensions import Self
from pygame import display, Surface, image 
#import os

# Biking-Berlin imports
#from biking_berlin import images
try:
    # for normal use
    from init.image_pathes import ImagePaths  # type: ignore
except Exception:
    # for testing purpose - pytest needs this import path
    from biking_berlin.init.image_pathes import ImagePaths  # type: ignore


class InitialSettings:

    '''
    Initial player settings
    '''
    @classmethod
    def get_intial_player_settings(cls):
        run = True
        return run

    #@classmethod
    #def get_player_image_size(cls):

    '''
    Initial screen/window settings
    '''
    @classmethod
    def set_screen_number(cls) -> int:
        # Set display number of the used display here
        display_number = 0
        return display_number

    @classmethod
    def initialize_screen(cls) -> bool:
        display.init()
        display_module_initialised = display.get_init()
        return display_module_initialised

    @classmethod
    def get_display_resolution(cls) -> tuple:

        display_module_initialised = InitialSettings.initialize_screen()
        display_number = InitialSettings.set_screen_number()

        # If the pygame display module was successfully initialised, go on
        if display_module_initialised:
            screen_info_test = display.Info()

            try:
                # TBD: rm "type: ignore" and check if get_desktop_sizes really does not exist             
                screen_info = display.get_desktop_sizes()  # type: ignore
                screen_resolution = screen_info[display_number]
            except:
                print("Screen Information taken from current screen")
                screen_resolution = (screen_info_test.current_w, screen_info_test.current_h)

            #print(display.list_modes())

            # TO DO: implement a full screen mode and a window mode 
            # list_available_screen_modes = display.list_modes()
        # Else print Error message
        else:
            print("Initialisation of the screen failed.")
            screen_resolution = [None, None]
        return screen_resolution

    @classmethod
    def set_display_parameters_and_return_screen_object(cls) -> Surface:
        """
        Set the display mode according to the display resolution. In case this
        fails, a 
        """
        screen = display.set_mode(InitialSettings.get_display_resolution())
        return screen # type: ignore

    # TBD: calculate  ground_position, size_player


    '''
    Background images:

    two background images are used to give the imagination of movement
    both images are moved left, when one finishes the other is put on
    the right side of the last image
    '''

    # TBD: fix this function
    """     @classmethod
    def get_background_dimensions_list(cls) -> list:

        background_image_path = (ImagePathes.get_background_image_path())[0]
        #print(background_image_path)
        background = image.load(background_image_path)
        background_dimensions = background.get_width(), background.get_height()
        background_dimensions_list = list(background_dimensions)

        return background_dimensions_list """

    # first background image (background_pos1 - x position of image) starts at x position 0
    # second background image starts at x position where first image ends
 
    # TBD: program function that sets the starting point of the image(s?) - only intitialisation, so here only 0,size?
    """ @classmethod
    def init_background_dimensions(cls) -> list:
    """
    """ 
    The init_background_dimensions function creates and returns a list 
        (init_background_dimensions_list) where:
        [starting point on x axis, background image length, background image height]
        By calling the InitialSettings.get_background_dimensions_list()
        function and merging it to the starting oint on the x axis.
    """
    """
        background_dimensions_list = InitialSettings.get_background_dimensions_list()
        init_background_dimensions_list = [0] + background_dimensions_list # type: ignore
        return init_background_dimensions_list """

InitialSettings.get_display_resolution()
