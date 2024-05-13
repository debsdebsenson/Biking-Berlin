import os
# import pygame


class ImagePaths():
    """
    Singleton class to create all the image pathes and pathes to the folders
    """
    folder_name_list_of_player = ['player']

    @classmethod
    def get_basic_path_to_images_folder(cls) -> str:
        """Concatenates the basic folder path to the image folder and returns
        it as string."""
        images_folder_path = os.path.join('biking_berlin', 'images')

        return images_folder_path

    @classmethod
    def concatenate_base_path_and_folder_name(cls, folder_name_list: list) -> str:
        """Concatenates the basic folder path with the folder names inserted as
        lists and returns it as a string."""

        number_of_folders_to_be_concatenated = len(folder_name_list)
        images_folder_path = ImagePaths.get_basic_path_to_images_folder()

        if number_of_folders_to_be_concatenated == 1:
            folder_path = os.path.join(images_folder_path, str(folder_name_list[0]))

        elif number_of_folders_to_be_concatenated > 1:

            folder_path = os.path.join(images_folder_path, str(folder_name_list[0]))
            for x in range(1, number_of_folders_to_be_concatenated):
                folder_path = os.path.join(folder_path, str(folder_name_list[x]))

        return folder_path

    @classmethod
    def create_pathes_of_images_list(cls, folder_name_list: list, image_base_name: str, number_of_images: int, image_type: str = 'png') -> list:
        """Concatenates number_of_images times the inserted path with the image
        base name and the image type to create and return a list of strings
        with the paths."""
        
        path = ImagePaths.concatenate_base_path_and_folder_name(folder_name_list)

        image_type_valid = False

        if isinstance(image_type, str):
            image_type_valid = True

        if (number_of_images == 1) & (image_type_valid == True):
            image_group_path_list = [os.path.join(path, str(image_base_name) + '.' + image_type)]
        elif (number_of_images > 1) & (image_type_valid == True):
            image_group_path_list = [os.path.join(path, str(image_base_name) + str(x) + '.' + image_type) for x in range(0, number_of_images)]
        else:
            print("Wrong input to create_pathes_of_images_list function. Input is treated as single image and png is used as default type. Number of images must be > 0.")
            image_group_path_list = [os.path.join(path, str(image_base_name) + '.png')]

        return image_group_path_list

    @classmethod
    def get_background_image_path(cls) -> list:
        """Concatenates the basic folder path with the background image folder
        path and returns it as a string."""
        background_folde_name_list = ['background']
        background_image_path = ImagePaths.create_pathes_of_images_list(background_folde_name_list, 'background', 1)
        return background_image_path
    
    @classmethod
    def get_special_sights_folder_path(cls) -> str:
        """Concatenates the basic folder path with the background image folder
        path and returns it as a string."""
        special_sights_name_list = ['background', 'special_sights']
        special_sights_folder_path = ImagePaths.concatenate_base_path_and_folder_name(special_sights_name_list)
 
        return special_sights_folder_path

    @classmethod
    def get_pothole_image_path(cls) -> list:
        """Concatenates the basic folder path with the pothole image folder
        path and returns it as a string."""
        pothole_folder_name_list = ['pothole']
        pothole_image_path = ImagePaths.create_pathes_of_images_list(pothole_folder_name_list, 'pothole', 1)
        # pothole_image_path = pygame.image.load(os.path.join('biking_berlin', images_folder)).convert()

        return pothole_image_path
    
    @classmethod
    def get_falling_player_images_folder_path(cls) -> list:
        """Concatenates the basic folder path with the fallen player image
        folder path and returns it as a string."""
        fallen_player_image_folder_path = ImagePaths.create_pathes_of_images_list(ImagePaths.folder_name_list_of_player, 'playerFALLEN', 1)
        # player_image_folder_path = pygame.image.load(os.path.join('biking_berlin', player_folder)).convert()

        return fallen_player_image_folder_path

    @classmethod
    def get_running_player_images_folder_path(cls) -> list:
        """Concatenates the basic folder path with the running player images
        folder pathes and returns them as a list of strings."""
        running_player_image_folder_path_list = ImagePaths.create_pathes_of_images_list(ImagePaths.folder_name_list_of_player, 'playerRUNNING', 8)

        return running_player_image_folder_path_list

    @classmethod
    def get_jumping_player_images_folder_path(cls) -> list:
        """Concatenates the basic folder path with the running player images
        folder pathes and returns them as a list of strings."""
        jumping_player_image_folder_path_list = ImagePaths.create_pathes_of_images_list(ImagePaths.folder_name_list_of_player, 'playerJUMPING', 8)

        return jumping_player_image_folder_path_list

    @classmethod
    def get_pidgeon_images_folder_path(cls) -> list:
        """Concatenates the basic folder path with the pidgeon images
        folder pathes and returns them as a list of strings."""
        pidgeon_image_folder_name_list = ['pidgeon']
        pidgeon_image_folder_path_list = ImagePaths.create_pathes_of_images_list(pidgeon_image_folder_name_list, 'PIDGEON', 4)

        return pidgeon_image_folder_path_list

    @classmethod
    def get_beatle_car_images_folder_path(cls) -> list:
        """Concatenates the basic folder path with the pidgeon images
        folder pathes and returns them as a list of strings."""
        pidgeon_image_folder_name_list = ['vehicles', 'beatle_car']
        pidgeon_image_folder_path_list = ImagePaths.create_pathes_of_images_list(pidgeon_image_folder_name_list, 'BEATLE', 8)

        return pidgeon_image_folder_path_list

"""
ToDo: Implement car image pathes (4x images per car - ) pathes. + testing
"""
