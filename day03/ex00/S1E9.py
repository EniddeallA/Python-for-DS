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


class Stark(Character):
    """Class Stark"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor of Stark"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Method to kill Stark"""
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
