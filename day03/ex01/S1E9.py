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
        pass

    def __str__(self):
        return f"<bound method {self.__class__.__name__}.__str__ of Vector:\
('{self.family_name}', '{self.eyes}', '{self.hairs}')>"

    def __repr__(self):
        return f"<bound method {self.__class__.__name__}.__repr__ of Vector:\
('{self.family_name}', '{self.eyes}', '{self.hairs}')>"


class Stark(Character):
    """Class Stark"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor of Stark"""
        super().__init__(first_name, is_alive)
        self.family_name = "Stark"

    def die(self):
        """Method to kill Stark"""
        self.is_alive = False
