class Pet:

    species = "Dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Max = Pet("Max", 10)
Blue = Pet("Blue", 12)

print("Max is a {}".format(Max.species))
print("Blue is a {}".format(Blue.species))

print("{} is {} years old".format(Max.name, Max.age))
print("{} is {} years old".format(Blue.name, Blue.age))
