# OOP
#OBJECT-ORIENTED PROGRAMMING'''

class Dog:
    def __init__(self, no_of_eyes, colour, no_of_legs, ears):#__init__=initialize
        self.no_of_eyes = no_of_eyes
        self.colour = colour
        self.no_of_legs = no_of_legs
        self.ears = ears

    def bark(self):# is an action ,does not use init, belongs to the class itself
        print('Woof! Woof!')
    def walk(self):
        print('Limps')
    def eat(self):
        print('Meat')
    def play(self):
        print('Playful')

German_shepherd = Dog(no_of_eyes=2, colour='Grey', no_of_legs =4, ears ='pointed')
Dodger = Dog(colour='white', no_of_eyes=1, no_of_legs= 4, ears ='rounded')
Dobberman = Dog(2, 'brown', 4, 'pointed')
Golden_retriever =Dog(2, 'gold', 4, 'floppy')

print(German_shepherd.colour, German_shepherd.no_of_eyes, German_shepherd.no_of_legs, German_shepherd.ears)
German_shepherd.bark()
print(Dodger.no_of_eyes, Dodger.colour, Dodger.no_of_legs, Dodger.ears)
Dodger.eat()
print(Dobberman.no_of_eyes, Dobberman.colour, Dobberman.no_of_legs, Dobberman.ears)
Dobberman.walk()
print(Golden_retriever.no_of_eyes, Golden_retriever.colour, Golden_retriever.no_of_legs, Golden_retriever.ears)
Golden_retriever.play()

Dobberman.colour = 'dark-brown'
print(Dobberman.colour)
Golden_retriever.colour = 'yellow-brown'
print(Golden_retriever.colour)