from S1E9 import Character


class Baratheon(Character):
    """Class Baratheon"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor of Baratheon"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Method to kill Baratheon"""
        self.is_alive = False


class Lannister(Character):
    """Class Lannister"""
    def __init__(self, first_name=None, is_alive=True):
        """Constructor of Lannister"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Method to kill Lannister"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Method to create Lannister"""
        return Lannister(first_name, is_alive)


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__())
    print(Robert.__repr__())
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__())
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__},\
 Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
