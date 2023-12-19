import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate random id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student dataclass"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.lower()


def main():
    student = Student(name="Edward", surname="agle")
    print(student)
    student1 = Student(name="Edward", surname="agle", active=False)
    print(student1)
    # student2 = Student(name="Edward", surname="agle",  id = "toto")
    # print(student2)


if __name__ == "__main__":
    main()
