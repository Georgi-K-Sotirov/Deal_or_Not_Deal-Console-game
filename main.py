import random
import sys


def box_draw(number):
    print()
    print()
    print(50 * "*")
    print(f"You have to select {number} boxes, until you get offer for the banker.")
    num = 1
    while num <= number:
        print("You haven't opened these amounts yet")
        print(", ".join(map(str, money_pool_in_game)))
        print(50 * "*")
        print(f"You can choose from the following boxes:")
        print(", ".join(map(str, box_pool)))

        box_choice = int(input(f"Please select box number {num}: "))
        if box_choice not in box_pool:
            print("Invalid box number!")
            print("Try again!")
            print()
            print()
            print(50 * "*")
            continue
        num += 1
        money_open = f"box_{box_choice}"
        money_open = globals()[money_open]
        global total_money_in_the_game
        total_money_in_the_game -= money_open
        money_pool_in_game.remove(money_open)
        print(f"In box number {box_choice} there was: {money_open} lv.")
        box_pool.remove(box_choice)
        print()
        print()
        print(50 * "*")


def offer_from_banker():
    print()
    print("Now is time to hear the offer from our banker.")
    print()

    offer = total_money_in_the_game / (len(box_pool)+1)

    print(50 * "*")
    print()
    print()
    print(f"The offer is: {offer:.2f} lv.")
    print()
    print()
    print(f"{player_name}. DEAL OR NOT DEAL!")
    while True:
        deal_or_not = input("Please enter y or n: ")
        if deal_or_not == "y" or deal_or_not == "n":
            if deal_or_not == "y":
                print()
                print()
                print(f"{player_name}. You made a deal worth of {offer:.2f} leva!")
                print(f"Lets open you box now.")
                print()
                print(50 * "*")
                print()
                print(f"In your box was the amount of {player_box} leva.")
                if offer > player_box:
                    print()
                    print(50 * "*")
                    print()
                    print(f"Congratulations!!!")
                    print(f"{player_name} You made a great deal.")
                else:
                    print()
                    print(50 * "*")
                    print()
                    print(f"Sorry!!!")
                    print(f"{player_name} Better luck next time!")
                sys.exit()
            elif deal_or_not == "n":
                print(f"Ok {player_name}, lets continue playing!")
                break
        else:
            print("Invalid input")
            continue


money_pool = [0.01, 0.10, 0.50, 1, 2, 5, 10, 50, 100, 250, 500, 750, 1000, 1500, 2500, 5000, 7500,
              10000, 12500, 15000, 20000, 25000, 50000, 100000]
money_pool_in_game = [0.01, 0.10, 0.50, 1, 2, 5, 10, 50, 100, 250, 500, 750, 1000, 1500, 2500, 5000, 7500,
                      10000, 12500, 15000, 20000, 25000, 50000, 100000]
total_money_in_the_game = sum(money_pool)
box_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

box_1 = random.choice(money_pool)
money_pool.remove(box_1)
box_2 = random.choice(money_pool)
money_pool.remove(box_2)
box_3 = random.choice(money_pool)
money_pool.remove(box_3)
box_4 = random.choice(money_pool)
money_pool.remove(box_4)
box_5 = random.choice(money_pool)
money_pool.remove(box_5)
box_6 = random.choice(money_pool)
money_pool.remove(box_6)
box_7 = random.choice(money_pool)
money_pool.remove(box_7)
box_8 = random.choice(money_pool)
money_pool.remove(box_8)
box_9 = random.choice(money_pool)
money_pool.remove(box_9)
box_10 = random.choice(money_pool)
money_pool.remove(box_10)
box_11 = random.choice(money_pool)
money_pool.remove(box_11)
box_12 = random.choice(money_pool)
money_pool.remove(box_12)
box_13 = random.choice(money_pool)
money_pool.remove(box_13)
box_14 = random.choice(money_pool)
money_pool.remove(box_14)
box_15 = random.choice(money_pool)
money_pool.remove(box_15)
box_16 = random.choice(money_pool)
money_pool.remove(box_16)
box_17 = random.choice(money_pool)
money_pool.remove(box_17)
box_18 = random.choice(money_pool)
money_pool.remove(box_18)
box_19 = random.choice(money_pool)
money_pool.remove(box_19)
box_20 = random.choice(money_pool)
money_pool.remove(box_20)
box_21 = random.choice(money_pool)
money_pool.remove(box_21)
box_22 = random.choice(money_pool)
money_pool.remove(box_22)
box_23 = random.choice(money_pool)
money_pool.remove(box_23)
box_24 = random.choice(money_pool)
money_pool.remove(box_24)

print(50 * "*")
print(14 * "*", "Welcome to the game!", 14 * "*")
print(16 * "*", "DEAL OR NOT DEAL!", 15 * "*")

player_name = input("What is your name: ")
print(f"Hello, {player_name}!")
print(f"Lets play!")
while True:
    accepted_input = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                      "18", "19", "20", "21", "22", "23", "24")
    player_box = input("Please select your box number from 1 to 24: ")
    if player_box not in accepted_input:
        print("Invalid input!")
        print("Try again!")
        continue
    else:
        break

print(f"Great!, You choose to play with box number {player_box}")
player_box = int(player_box)
box_pool.remove(player_box)
player_box = f"box_{player_box}"
player_box = globals()[player_box]





box_draw(6)

offer_from_banker()

box_draw(4)

offer_from_banker()

box_draw(3)

offer_from_banker()

box_draw(3)

offer_from_banker()

box_draw(3)

offer_from_banker()

box_draw(2)

offer_from_banker()

box_draw(1)

offer_from_banker()

print()
print()
print(50 * "*")
print()

print(len(box_pool))

# winning the chosen box
print()
print(50 * "*")
print()
print(f"{player_name}. You made it to the end!")
print()
print(f"Lets open you box now.")
print()
print(50 * "*")
print()
print(f"In your box was the amount of {player_box} leva.")
