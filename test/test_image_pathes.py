import pytest

from biking_berlin.init.image_pathes import ImagePathes # type: ignore

parametrize = pytest.mark.parametrize

class TestBasePathes:
    def test_get_basic_path_to_images_folder(self):
        assert ImagePathes.get_basic_path_to_images_folder() == 'biking_berlin/images'
        assert type(ImagePathes.get_basic_path_to_images_folder()) == str

    @parametrize(
        'string, expected', [
            (['something'], 'biking_berlin/images/something'),
            (['abc','def'], 'biking_berlin/images/abc/def'),
            (['1','2', 3.4], 'biking_berlin/images/1/2/3.4'),
            (['1','2', [3, 4]], 'biking_berlin/images/1/2/[3, 4]'),
            ([-2], 'biking_berlin/images/-2'),
            ([-2, 45.2, 'a'], 'biking_berlin/images/-2/45.2/a'),
            ([-2.1, 'a'], 'biking_berlin/images/-2.1/a'),
            ([[-2, 1], 'a'], 'biking_berlin/images/[-2, 1]/a'),
            ([-2.1, "a"], 'biking_berlin/images/-2.1/a'),
        ]
    )
    def test_concatenate_base_path_and_foldername(self, string, expected):
        assert ImagePathes.concatenate_base_path_and_foldername(string) == expected
        assert type(ImagePathes.concatenate_base_path_and_foldername(string)) == str

    @parametrize(
        'folder_name_list, image_base_name, number_of_images, expected', [
            (['a'], 'b', 1, ['biking_berlin/images/a/b.png']),
            (['a'], 'b', 2, ['biking_berlin/images/a/b0.png', 'biking_berlin/images/a/b1.png']),
            (['a'], 2.0, 2, ['biking_berlin/images/a/2.00.png', 'biking_berlin/images/a/2.01.png']),
            (['a'], 2.0, -2, ['biking_berlin/images/a/2.0.png']),
            (['a', 1], 2.0, -2, ['biking_berlin/images/a/1/2.0.png'])
        ]
    )
    def test_create_pathes_of_images_list(self, folder_name_list, image_base_name, number_of_images, expected):
        assert ImagePathes.create_pathes_of_images_list(folder_name_list, image_base_name, number_of_images) == expected
        #assert type(ImagePathes.create_pathes_of_images_list()) == list
        #assert len(ImagePathes.create_pathes_of_images_list()) == 1
    
    """     @parametrize(
        'folder_name_list, image_base_name, number_of_images, image_type, expected', [
            (['a'], 'b', 1, 'md', ['biking_berlin/images/a/b.md']),
            (['a'], 'b', 1, 3, ['biking_berlin/images/a/b.png'])#,
            #(['a', 'c'], 5.5, 1, 3, ['biking_berlin/images/a/c/5.5.png']),
            #(['a', 'c'], 'b', 2, 'md', ['biking_berlin/images/a/c/b0.md', 'biking_berlin/images/a/c/b1.md']),
            #(['a', 'c'], 'b', 2, 1, ['biking_berlin/images/a/c/b.png'])
        ]
    )
    def test_create_pathes_of_images_list_additional(self, folder_name_list, image_base_name, number_of_images, image_type, expected):
        assert ImagePathes.create_pathes_of_images_list(folder_name_list, image_base_name, number_of_images, image_type) == expected
        assert type(ImagePathes.create_pathes_of_images_list(folder_name_list, image_base_name, number_of_images, image_type)) == list
        # TBD: Add test that ensure the right number of pathes will be provided"""
        
    def test_get_special_sights_folder_path(self):
        assert ImagePathes.get_special_sights_folder_path() == 'biking_berlin/images/background/special_sights'

class TestImagePathes:
    def test_get_background_image_path(self):
        assert ImagePathes.get_background_image_path() == ['biking_berlin/images/background/background.png']
        assert len(ImagePathes.get_background_image_path()) == 1
        assert type(ImagePathes.get_background_image_path()) == list

    def test_get_falling_player_images_folder_path(self):
        assert ImagePathes.get_falling_player_images_folder_path() == ['biking_berlin/images/player/playerFALLEN.png']
        assert len(ImagePathes.get_falling_player_images_folder_path()) == 1
        assert type(ImagePathes.get_falling_player_images_folder_path()) == list

    def test_get_pothole_image_path(self):
        assert ImagePathes.get_pothole_image_path() == ['biking_berlin/images/pothole/pothole.png']
        assert len(ImagePathes.get_pothole_image_path()) == 1
        assert type(ImagePathes.get_pothole_image_path()) == list

    @parametrize(
        'expected', [
            (['biking_berlin/images/pidgeon/PIDGEON0.png',
            'biking_berlin/images/pidgeon/PIDGEON1.png',
            'biking_berlin/images/pidgeon/PIDGEON2.png',
            'biking_berlin/images/pidgeon/PIDGEON3.png'])
        ]
    )
    def test_get_pidgeon_images_folder_path(self, expected):
        assert ImagePathes.get_pidgeon_images_folder_path() == expected
        assert len(ImagePathes.get_pidgeon_images_folder_path()) == 4
        assert type(ImagePathes.get_pidgeon_images_folder_path()) == list

    @parametrize(
        'expected', [
            (['biking_berlin/images/player/playerRUNNING0.png',
            'biking_berlin/images/player/playerRUNNING1.png',
            'biking_berlin/images/player/playerRUNNING2.png',
            'biking_berlin/images/player/playerRUNNING3.png',
            'biking_berlin/images/player/playerRUNNING4.png',
            'biking_berlin/images/player/playerRUNNING5.png',
            'biking_berlin/images/player/playerRUNNING6.png',
            'biking_berlin/images/player/playerRUNNING7.png'])
        ]
    )
    def test_get_running_player_images_folder_path(self, expected):
        assert ImagePathes.get_running_player_images_folder_path() == expected
        assert len(ImagePathes.get_running_player_images_folder_path()) == 8
        assert type(ImagePathes.get_running_player_images_folder_path()) == list

    @parametrize(
        'expected', [
            (['biking_berlin/images/player/playerJUMPING0.png',
            'biking_berlin/images/player/playerJUMPING1.png',
            'biking_berlin/images/player/playerJUMPING2.png',
            'biking_berlin/images/player/playerJUMPING3.png',
            'biking_berlin/images/player/playerJUMPING4.png',
            'biking_berlin/images/player/playerJUMPING5.png',
            'biking_berlin/images/player/playerJUMPING6.png',
            'biking_berlin/images/player/playerJUMPING7.png'])
        ]
    )
    def test_get_jumping_player_images_folder_path(self, expected):
        assert ImagePathes.get_jumping_player_images_folder_path() == expected
        assert len(ImagePathes.get_jumping_player_images_folder_path()) == 8
        assert type(ImagePathes.get_jumping_player_images_folder_path()) == list

    @parametrize(
        'expected', [
            (['biking_berlin/images/vehicles/beatle_car/BEATLE0.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE1.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE2.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE3.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE4.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE5.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE6.png',
            'biking_berlin/images/vehicles/beatle_car/BEATLE7.png'])
        ]
    )
    def test_get_beatle_car_images_folder_path(self, expected):
        assert ImagePathes.get_beatle_car_images_folder_path() == expected
        assert len(ImagePathes.get_beatle_car_images_folder_path()) == 8
        assert type(ImagePathes.get_beatle_car_images_folder_path()) == list