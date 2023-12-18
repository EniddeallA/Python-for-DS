import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    pass


def main():
    student = Student(name = "Edward", surname = "agle")
    print(student)
    

if __name__ == "__main__":
    main()