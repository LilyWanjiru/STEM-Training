#My attempt at OOP
class Human:
    def __init__(self, gender, eyes, ears, nose, mouth, hands, legs, nationality):
        self.gender = gender
        self.eyes = eyes
        self.ears = ears
        self.nose = nose
        self.mouth = mouth
        self.hands = hands
        self.legs = legs
        self.nationality = nationality

    def laugh(self):
        print('Ha! Ha! Ha!')
    def cry(self):
        print('Sad')
    def sleep(sleep):
        print('Zzzzz!')
    def sneeze(self):
        print('Achoo!')
    
Amanda = Human(gender= 'Female', eyes = 2, ears=2, nose=1, mouth=1,hands=2, legs=2, nationality='American')
Joel = Human(gender= 'Male', eyes=2,ears=4, nose=1, mouth=1, hands=2, legs=2, nationality='British')
Bob = Human(gender= 'Male', eyes=2, ears=2, nose=1, mouth=1, hands=1, legs=2, nationality='Australian')
Abby = Human('Female', 4, 2, 1, 1, 2 ,1,'Turkish')

print(Amanda.gender, Amanda.eyes, Amanda.ears, Amanda.nose, Amanda.mouth, Amanda.hands, Amanda.legs, Amanda.nationality)
Amanda.sleep()
print(Joel.gender, Joel.eyes, Joel.ears, Joel.nose, Joel.mouth, Joel.hands, Joel.legs, Joel.nationality)
Joel.laugh()
print(Bob.gender, Bob.eyes, Bob.ears, Bob.nose, Bob.mouth, Bob.hands, Bob.legs, Bob.nationality)
Bob.cry()
print(Abby.gender, Abby.eyes, Abby.ears, Abby.nose, Abby.mouth, Abby.hands, Abby.legs, Abby.nationality)
Abby.sneeze

Joel.nationality = 'British_African'
print(Joel.nationality)