import random


# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# #TODO-1: drew 2 card for player

# player_card_1 = random.choice(cards)
# player_card_2 = random.choice(cards)



# print(f"your cards are {player_card_1} and {player_card_2}")

# #TODO-2: drew 2 cards for computer and show the player the first card

# computer_card_1 = random.choice(cards)
# computer_card_2 = random.choice(cards)

# print(f"computer's first card is {computer_card_1}")





# #TODO-3: ask player if they want to get another card only if the total of his cars are less than 21 , TODO-5: if computer and player totals are less than 21 compair who is higher

# total_player_cards = player_card_2 + player_card_1

# total_computer_cards = computer_card_1 + computer_card_2
# get_a_3_card =True
# while total_player_cards < 21 and get_a_3_card:
#     get_a_3_card = True if input("would you like to get another card? (y,n) ") == 'y' else False
#     if get_a_3_card:
#         player_extra_card = random.choice(cards) 
#         print(f"your new card is {player_extra_card}")
#         total_player_cards += player_extra_card
#         if total_player_cards > 21:
#             print("you lost")
    
    
#     print(f"your total is {total_player_cards}")

# while total_computer_cards < 15 and total_player_cards < 21:
#     computer_extra_card = random.choice(cards)

#     total_computer_cards += computer_extra_card
#     if total_computer_cards > 21:
#         print(f"you won, computer got another card his total is {total_computer_cards} and the last card he got is {computer_extra_card}")
#     elif total_computer_cards < 21:
#         if total_player_cards > total_computer_cards:
#             print(f"you win {total_player_cards} and computer total is {total_computer_cards}")

    
        




#TODO-1: create a function to deal a card

def deal_card():
  card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(card)

#TODO-2: create a function to give the player 2 cards , and ask if he wants more cards

def player(computer_first_card):
    player_cards = []
    get_another_card = True
    for i in range(2):
       player_cards.append(deal_card())
    while sum(player_cards) < 21 and get_another_card:
       print(f"your cards are {player_cards} the total is {sum(player_cards)}")
       print(f"computer first cards is {computer_first_card}")
       get_another_card = True if input("anouther card(y,n)? ") == 'y' else False
       if get_another_card:
          extra_player_card = deal_card()
          player_cards.append(extra_player_card)
          print(f"your card is {extra_player_card}, total is {sum(player_cards)}")
    return player_cards

#TODO-3: create a function that gives the computer two cards and detarmins if more cards are needed 

def computer():
    computer_cards = []
    get_another_card = True
    for i in range(2):
       computer_cards.append(deal_card())
    while sum(computer_cards) < 17:
       new_card = deal_card()
       computer_cards.append(new_card)
    #    print(f"computer is getting another card {new_card}, computer total is {sum(computer_cards)}")

    return computer_cards

#TODO-4: create a function that for the opreator 

def operator():
   
    computer_cards = computer()
    player_cards = player(computer_cards[0])

    if sum(player_cards) == 21:
        print("you win by a BlackJack")
    elif sum(computer_cards) == 21:
       print("computer win by a BlackJack")
    elif sum(player_cards) > 21:
       print(f"you lost, total: {sum(player_cards)}")
    elif sum(computer_cards) > 21:
       print(f"you win computer total {sum(computer_cards)} and your total {sum(player_cards)}")
    elif sum(computer_cards) < sum(player_cards):
        print(f"you win computer total {sum(computer_cards)} and your total {sum(player_cards)}")
    elif sum(computer_cards) > sum(player_cards):
        print(f"you lost computer total {sum(computer_cards)} and your total {sum(player_cards)}")
    else:
       print(f"computer total {sum(computer_cards)} your total is {sum(player_cards)}")
operator()