class Puppy:
    species = 'canine'
    def __init__(self,name,breed):
        self.name = name
        self.tricks = []
        self.breed = breed
        print(self.name)
        print(self.tricks)
        print(self.breed)
    def do_trick(self,new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)
        print(self.tricks)
    def bark(self):
        print(f"{self.name} says WOOF !!!")

class Names(Puppy):
    def roar(self):
        print(self.name)

otter = Names("Elton","german sheprd")

otter.roar()
otter.bark()
print(otter.species)
Elton = Puppy("Otter","mutt")
Elton.do_trick("sit")

