# Entity Class!
# a. The “Entity” class constructor should take in 3 inputs (apart from self), attack, defense, and hit points (there should be corresponding instance variables set to the values from attack, defense, and hit points)
# b. There should be an attack function that takes in another Entity, and deals damage to the opponent (takes away self.attack - opponent.defense from their opponent’s hitpoints)
#    attack
#    Inputs: opponent (this is another instance of the Entity Class)
#    Outputs: None
#        The function should take away (self.attack - opponent.defense) from the opponent’s health. 
# c. There should be a heal function that allows the Entity to heal hit points corresponding to their defense
#    heal
#    Inputs: None
#    Outputs: None
#        The function should add self.defense hitpoints to their own health (note that this CAN go over the original hitpoints)
# d. There should be an isDead function to check whether an entity has a positive number of hit points
#    isDead
#    Inputs: None
#    Outputs: boolean
#         The function should return True if the Entity has positive health and false otherwise. 
class Entity:
    def __init__(self, attack, defense, hitpoints, accuracy):
        self.attack=attack
        self.defense=defense
        self.hitpoints=hitpoints
        self.accuracy=accuracy

    # def takeHit(self, hits):
    #     self.hitpoints -= hits

    # def getDefense(self):
    #     return self.defense

    from random import choices
    def attackf(self, opponent):
        # opponent.takeHit(self.attack - opponent.getDefense())
        p = [0,1]
        w = [1-self.accuracy, self.accuracy]

        if random.choices(p, w) == [1]:
            opponent.hitpoints -= self.attack - opponent.defense

    def heal(self):
        self.hitpoints += self.defense

    def isDead(self):
        return self.hitpoints <= 0

# Battle: THIS FUNCTION DOES NOT BELONG TO THE ENTITY CLASS
# a. Write a function battle1 function
#    battle1
#    Inputs: entity1, entity2
#    Outputs: boolean
#         Have the entities fight it out ONLY using attacks (entity1 goes first)
#         Returns True if entity1 wins and false if entity2 wins
def battle1(entity1, entity2):
    while entity1.isDead() == False and entity2.isDead() == False:
        entity1.attackf(entity2)
        if entity2.isDead():
            return True
        entity2.attackf(entity1)
        if entity1.isDead():
            return False
    if entity2.isDead():
        return True
    if entity1.isDead():
        return False
# b. Write a function battle2
#    Battle2
#    Inputs: entity1, entity2
#    Outputs: boolean
#         Have the entities fight it out with each entity choosing with 50% probability between heal and attack
#         Returns True if entity1 wins and false if entity2 wins
import random
def battle2(entity1, entity2):
    while entity1.isDead() == False and entity2.isDead() == False:
        # 0 heal, 1 attack, start with entity1
        if random.choice([0, 1]):
            entity1.attackf(entity2)
            if entity2.isDead():
                return True
        else:
            entity1.heal()

        # now entity2
        if random.choice([0, 1]):
            entity2.attackf(entity1)
            if entity1.isDead():
                return False
        else:
            entity2.heal()
    if entity2.isDead():
        return True
    if entity1.isDead():
        return False

def main():
    player1 = Entity(5, 2, 100, 0.6)
    player2 = Entity(5, 2, 100, 0.8)
    # battle1
    if (battle1(player1, player2)):
        print("player1 wins battle1")
    else:
        print("player2 wins battle1")
    # battle2
    player1 = Entity(5, 2, 100, 0.6)
    player2 = Entity(5, 2, 100, 0.8)    
    if (battle2(player1, player2)):
        print("player1 wins battle2")
    else:
        print("player2 wins battle2")

if __name__ == "__main__":
    main()
