#  Created by Artem Manchenkov
#  artyom@manchenkoff.me
#
#  Copyright © 2019
#
#  ООП - Наследование и перегрузка классов
#


# Пример базового класса
class Human:
    def walk(self):
        print("I'm walking...")

    def sleep(self):
        print("I'm sleeping...")


person = Human()
person.walk()


# Пример класса-наследника
class SuperHuman(Human):
    def fly(self):
        print("I'm flying...")


person = SuperHuman()
person.walk()
person.fly()


# Пример перегрузки родительского класса
class SuperHuman(Human):
    def fly(self):
        print("I'm flying...")

    def walk(self):
        super().walk()
        print("But as a super-hero!")


person = SuperHuman()
person.walk()
person.fly()


# Пример перегрузки стандартных операций (str - для print, repr - для print в списках)
class PrintableHuman:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Human instance: {self.name}"


person = PrintableHuman('John Doe')
print(person)
