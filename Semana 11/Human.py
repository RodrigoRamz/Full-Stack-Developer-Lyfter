
from dataclasses import dataclass

@dataclass
class Head:
    eyes: int = 2
    ears: int = 2
    nose: int = 1
    mouth: int = 1

@dataclass
class Hand:
    fingers: int = 5

@dataclass
class Arm:
    side: str # Left or Right
    hand: Hand

@dataclass
class Feet:
    toes: int = 5

@dataclass
class Leg:
    side: str # Left or Right
    feet: Feet

@dataclass
class Torso:
    head: Head
    left_arm: Arm
    right_arm: Arm
    left_leg: Leg
    right_leg: Leg

class Human:
    def __init__(self, name: str, torso: Torso):
        self.name = name
        self.torso = torso

    
    def wave(self, side: str = "right") -> None:
        if side not in ("left", "right"):
            raise ValueError("Side must be 'left' or 'right'")
        arm = self.torso.right_arm if side == "right" else self.torso.left_arm
        print (f'{self.name} waves with the {side} arm (fingers: {arm.hand.fingers}).')

    def count_toe(self) -> int:
        return self.torso.left_leg.feet.toes + self.torso.right_leg.feet.toes
    

    def __repr__(self) -> str:
        return f"Human(name={self.name!r})"
    
#Instances

head = Head()
left_hand = Hand()
right_hand = Hand()

left_arm = Arm(side="left", hand=left_hand)
right_arm = Arm(side="right", hand=right_hand)

left_feet = Feet()
right_feet = Feet()

left_leg = Leg(side="left", feet=left_feet)
right_leg = Leg(side="right", feet=right_feet)

torso = Torso(head=head,
    left_arm=left_arm,
    right_arm=right_arm,
    left_leg=left_leg,
    right_leg=right_leg
    )

person = Human(name="Rodrigo", torso=torso)

person.wave("right")
print(person.count_toe())