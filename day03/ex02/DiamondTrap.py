from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class King"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor of King"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method to kill King"""
        self.is_alive = False

    def set_eyes(self, eyes):
        """Method to set eyes color"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Method to set hairs color"""
        self.hairs = hairs

    def get_eyes(self):
        """Method to get eyes color"""
        return self.eyes

    def get_hairs(self):
        """Method to get hairs color"""
        return self.hairs


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
