from abc import ABC, abstractmethod


class Character(ABC):
    """Class Character"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Function to kill Character"""
        self.is_alive = False


class Stark(Character):
    """Class Stark"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor of Stark"""
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"

    def die(self):
        """Method to kill Stark"""
        self.is_alive = False
