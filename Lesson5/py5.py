class Pet:
    """Klasa dla ulubieńców."""
    def speak(self):
        pass # odkładamy definicję na później
class Cat(Pet):
    """Klasa dla kotów."""
    def speak(self):
        print ( "miau!" )
class Dog(Pet):
    """Klasa dla psów."""
    def speak(self):
        print ( "hau!" )
# Klasa nie wywiedziona z Pet.
class Person:
    """Klasa dla osób."""
    def speak(self):
        print ( "witam!" )
    def drive(self):
        print ( "piii!" )
# Zwykła funkcja, a nie metoda.
def command(pet):
    pet.speak()
pets = [Cat(), Dog(), Person()] # konstruktory
# Przykład polimorfizmu Pythona.
# Funkcja oczekuje określonego interfejsu (metody speak),
# a nie określonego typu argumentu.
for pet in pets:
    command(pet)