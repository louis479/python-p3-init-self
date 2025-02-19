#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

from dog import Dog

fido = Dog("Fido")
print(fido.name)  # Output: Fido
print(fido.breed)  # Output: Mutt

snoopy = Dog("Snoopy", "Beagle")
print(snoopy.name)  # Output: Snoopy
print(snoopy.breed)  # Output: Beagle