from abc import ABC, abstractmethod 

class Character(ABC):
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for Method"""
        pass

class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(self)
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False