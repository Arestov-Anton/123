from Lesson_1.character import Character
from berserk import berserk


p1 = berserk(name = 'berserk', hp = 100, damage = 8, armor = 0 )
p2 = Character(name = 'character', hp= 100, damage=10,armor = 0)
while p1.hp > 0 and p2.hp > 0:
    print(p1)
    print(p2)
    p1.attack(p2)
    p2.attack(p1)
    print()
'''
import random
if random.randint(1, 100) <= 30:

else:
'''