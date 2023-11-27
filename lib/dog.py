#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Labrador", "German Shepherd", "Golden Retriever", "Bulldog", "Poodle"]

    def __init__(self, name, breed):
        self._name = None  # Use a private attribute to store the name
        self._breed = None  # Use a private attribute to store the breed
        self.name = name  # Use the property setter for validation
        self.breed = breed  # Use the property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")


