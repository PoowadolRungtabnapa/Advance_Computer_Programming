class Pet() :
    species = 'mammal'

    def __init__(self, name, pet) :
        self.name = name
        self.pet = pet
    
    def description1(self) :
        return "{} is {}.".format(self.name, self.pet)

    def description2(self, typepet) :
        return "I have {} {}.".format(self.pet, typepet)

I = Pet('I', 3)
print(I.description2('dogs'))

Tom = Pet('Tom', 6)
print(Tom.description1())

Fletcher = Pet('Fletcher', 7)
print(Fletcher.description1())

Larry = Pet('Larry', 9)
print(Larry.description1())

if Pet.species == 'mammal' :
    print("And they're all mammals, of course.")