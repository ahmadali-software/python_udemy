student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for key, value in student_scores.items():
    if value > 90:
        student_grades[key] = "Outstanding"
    elif value > 80:
        student_grades[key] = "Exceeds Expectations"
    elif value > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"


bids_dict = {}
more_biders = True

while more_biders:
    name = input("please enter your name: ")
    bid = int(input("enter the bid amount: "))

    bids_dict[name] = bid

    more_biders = True if input("any other biders(y, n): ") == 'y' else False
    
    print("\033[H\033[J", end="")

max_bid = max(bids_dict.values())
max_bider = max(bids_dict, key=bids_dict.get)

print(f"{max_bider} won by {max_bid}")



