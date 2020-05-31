class Animals:

    def __init__(self):
        
        self.eyes = 2
        self.legs = 4
        self.living = True

    def geteyes(self):
        
        return self.__eyes

    def seteyes(self, eyes):
        
        self.__eyes = eyes

    def getliving(self):
        
        return self._living

    def setliving(self, living):
        
        self._living = living

    def getlegs(self):
        
        return self.legs
    
    def setlegs(self, legs):
        
        self.legs = legs

class Deer(Animals):

    def eats(self):
        print("Deers eat leaces and twigs and grass.")

    def color(self):
        print("Deers are orange in colour.")

    def sound(self):
        print("Deers make bleat sound.")

    def typeOfAnimal(self):
        print("Dear is herbivorous animal.")

class Zebra(Animals):

    def eats(self):
        print("Zebras eat grass.")

    def color(self):
        print("Zebras are white with black strips.")

    def sound(self):
        print("Zebras either bark, brey or snort.")

    def typeOfAnimal(self):
        print("Zebra is herbivorous animal.")

class Cow(Animals):

    def eats(self):
        print("Cows eat grass, corn, grains.")

    def color(self):
        print("cows are generally white with black patches.")

    def sound(self):
        print("Cows moo.")

    def typeOfAnimal(self):
        print("Cow is herbivorous animal.")

class Elephant(Animals):

    def eats(self):
        print("Elephants eat grass, fruits, twigs.")

    def color(self):
        print("Elephants are dark grey in colour.")

    def sound(self):
        print("Elephants make sound called trumpet.")

    def typeOfAnimal(self):
        print("Elephant is herbivorous animal.")

class Horse(Animals):

    def eats(self):
        print("Horses eat grass and hay.")

    def color(self):
        print("Horses are of many different colours.")

    def sound(self):
        print("")

    def typeOfAnimal(self):
        print("Horse is herbivorous animal.")

class Cat(Animals):

    def eats(self):
        print("Cats eat rats.")

    def color(self):
        print("Cats are of many different colours but mainly they are grey.")

    def sound(self):
        print("Cat meows.")

    def typeOfAnimal(self):
        print("Cat is carnivorous animal")

class Lion(Animals):

    def eats(self):
        print("Lion eats meat of animals hunted.")

    def color(self):
        print("Color of Lion is Grayish Yellow.")

    def sound(self):
        print("A lion roars.")

    def typeOfAnimal(self):
        print("Lion is a carnivorous animal.")

class Tiger(Animals):

    def eats(self):
        print("Tiger eats the meat of hunted animals.")

    def color(self):
        print("Tiger is orange with black stripes.")

    def sound(self):
        print("a tiger roars.")

    def typeOfAnimal(self):
        print("Tiger is carnivorous animal.")

class Leopard(Animals):

    def eats(self):
        print("Leopard eats the meat of hunted animals.")

    def color(self):
        print("Leopards are cream-yellow, orange-black with black spots all over body.")

    def sound(self):
        print("Leopard makes hissing, growling and rasping sounds.")

    def typeOfAnimal(self):
        print("Leopard is carnivorous animal.")

class Jaguar(Animals):

    def eats(self):
        print("Jaguar eats the meat of hunted animals.")

    def color(self):
        print("Jaguars are cream-yellow, orange-black with black spots all over body.")

    def sound(self):
        print("Jaguar makes sound like sawing wood hence called saw.")

    def typeOfAnimal(self):
        print("Jaguar is carnivorous animal.")

Deer.eats(Deer)

Cow.sound(Cow)

Tiger.typeOfAnimal(Tiger)

Zebra.color(Zebra)

Elephant.living(Elephant)

Leopard.getlegs(Leopard)

Lion.geteyes(Lion)