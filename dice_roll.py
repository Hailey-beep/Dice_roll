import random
roll_dice = str(input("Press y to roll the dice, press n to exit"))
roll_dice = "y"

while roll_dice == "y":
    dice_num = random.randint(1,6)
    print(dice_num)
    roll_dice = str(input("Press y to roll the dice, press n to exit"))

if roll_dice == "n":
    print("goodbye")

