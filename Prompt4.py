class FavAnimal:
    def print(self):
        print("Here's my favorite animal.")
        print(f"It's arms are {self.arm_length}ft long.")
        print(f"It's legs are {self.leg_length}ft long.")
        print(f"It has {self.eye_number} eyes.")
        print(f"It has a tail. {self.tail}")
        print(f"It has fur. {self.fur}")
    def __init__(self, ArmLength, LegLength, EyeNumber, Tail, Fur):
        self.arm_length = ArmLength
        self.leg_length = LegLength
        self.eye_number = EyeNumber
        self.tail = Tail
        self.fur = Fur

def main():
    ArmLength=1.7
    LegLength =1.7
    EyeNumber=2
    Tail=True
    Fur=False
    Pangolins = FavAnimal(ArmLength,LegLength,EyeNumber,Tail,Fur)
    Pangolins.print()

if __name__=="__main__":
    main()
