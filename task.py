import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer=[rock,paper,scissors]
player=int(input("Enter your choice \n(1).rock\n(2).paper\n(3)scissors\n: "))
if player==1 or player==2 or player==3:
    print("ok")
else:
    print("Idiot enter the the proper choice")
    exit()

comp=random.randint(0,2)
print(f"computer \n {computer[comp]}\n player {computer[player-1]}")
if computer[comp]==computer[player-1]:
    print("\ndraw")
elif computer[comp]==rock:
    if computer[player-1]==paper:
        print("player wins")
    else:
        print("computer wins")

elif computer[comp]==paper:
    if computer[player-1]==scissors:
        print("player wins")
    else:
        print("computer wins")

elif computer[comp]==scissors:
    if computer[player-1]==rock:
        print("player wins")
    else:
        print("computer wins")
else:
    print("good")

