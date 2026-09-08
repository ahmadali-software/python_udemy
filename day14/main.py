# Problem : higher lower game, selcting 2 items from data file and let the player guess which one is higher, if the user gessed right, option b becomes option a and we select another 
# a and the score counter increases by one, until the user guesses wrong 



# TODO-1:import the list of dictionaries from data.py, and create a function to format the output
from data import data as data_list

import random
from art import logo, vs

# this function only returns the output in format, i will keep the functionalty of chossing the item in a defferent function 
def format_output(item):
    """returns the output in format, takes data item as an argument"""
    return f"{item['name']} from {item['country']}, {item['description']}"

# TODO-2:create a function to choose option b from data 
def choose_option_b(data_length):
    return random.randint(0,data_length -1)



def compare_options(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


# TODO-3:create the main loop- this loop brakes if the guess is wrong, or if the the score is equal to the lenght of the data list (which means the options are done)

score = 0
data_length = len(data_list)
guess = True
option_a = data_list[choose_option_b(data_length)]
option_b = data_list[choose_option_b(data_length)]
while guess and data_length > 1:


    # displaying logo
    print(logo)

    # so we don't compare the same item
    while option_a == option_b:
        option_b = data_list[choose_option_b(data_length)]

# TODO-3.0: display options and make the user choose one, then compaire if the user guessed correctly

    
    
    print(f"option a: {format_output(option_a)} {vs} \noption b: {format_output(option_b)}")
    user_guess = input("please enter 'a' or 'b': ")
    print()
    correct_guess = compare_options(option_a, option_b)

# TODO-3.1:score counter with the game functionalty(if the guess is correct:  1:  option b become option a.  2: display the number of followrs of both options. 
#  3: adding 1 to score. 4:removing old option a from the list so it doesn't display again and update data_lenght. )

    if user_guess == correct_guess:

        #  adding 1 to score
        score +=1

        # clearing the screen after every comparison
        print("\033[H\033[J", end="")
        #  display the number of followrs of both options. 
        print(f"Correct your current score is: {score}\n")
        print(f"{option_a['name']} has {option_a['follower_count']}M followers")
        print(f"{option_b['name']} has {option_b['follower_count']}M followers\n")

        # removing old option a, and update data_lenght
        data_list.remove(option_a)
        data_length -= 1

        #   option b become option a
        option_a = option_b
        option_b = data_list[choose_option_b(data_length)]
       
        


# TODO-3.2:score counter with the game functionalty(if the guess is wrong display the score and the followers of both options )
    elif user_guess != correct_guess:
        print("losserrrrr")

        #  display the number of followrs of both options. 
        print(f"your final score is: {score}\n")
        print(f"{option_a['name']} has {option_a['follower_count']}M followers")
        print(f"{option_b['name']} has {option_b['follower_count']}M followers\n")
        guess = False

# after the loop is done, if data_lenght is 1 or player score == len(data_list) -1 that means the player won//// 
# bug: data_list lenght here is 1, so if score == len(data_list) does not work, so I had to swich it to data_length == 1
if data_length == 1:
    print("The only reason you know the followers count is your are a fucking looser, GET A LIFE")

# retreving formated date to output
# print(format_output(choose_option_b(data_list)))



# bug1: in one of the runs 2 options were new, bug2: comparing the same item, bug3: out of range. all solved Alhmdullah

