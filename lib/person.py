#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name


from person import Person

alice = Person("Alice")
print(alice.name)  # Output: Alice

bob = Person("Bob")
print(bob.name)  # Output: Bob

