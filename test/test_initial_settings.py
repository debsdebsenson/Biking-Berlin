import pytest
import pygame
import sys
import os

from biking_berlin.init.initial_settings import InitialSettings # type: ignore

class TestInitialSettings:
    def test_get_intial_player_settings(self):
        assert InitialSettings.get_intial_player_settings() == True
        assert type(InitialSettings.get_intial_player_settings()) == bool

    def test_initialize_screen(self):
        assert type(InitialSettings.initialize_screen()) == bool
        assert InitialSettings.initialize_screen() == True

    def test_get_display_resolution(self):
        assert type(InitialSettings.get_display_resolution()) == tuple
        assert InitialSettings.get_display_resolution() == (1920, 1080)

    """     def test_set_display_parameters_and_return_screen_object(self):
            assert type(InitialSettings.set_display_parameters_and_return_screen_object()) == pygame.Surface
    """
    # for performing this test the directory needs to be changed to ensure the images can be found 
    """ @pytest.fixture(autouse=True)
    def test_get_background_dimensions_list(self, monkeypatch):
        new_dirname = os.path.join(os.path.split(sys.path[0])[0], 'Biking-Berlin')
        monkeypatch.chdir(new_dirname)
        assert type(InitialSettings.get_background_dimensions_list()) == list
        assert InitialSettings.get_background_dimensions_list() == [1788, 447]
    """
    """     @pytest.fixture(autouse=True)
    def test_init_background_dimensions(self, monkeypatch):
        new_dirname = os.path.join(os.path.split(sys.path[0])[0], 'Biking-Berlin')
        monkeypatch.chdir(new_dirname)
        assert type(InitialSettings.init_background_dimensions()) == list
        assert InitialSettings.init_background_dimensions() == [0, 1788, 447] """
