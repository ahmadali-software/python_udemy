
def calculate_love_score(name1, name2):
    letters_in_true = 0
    letters_in_love = 0
    for letter in name1.lower():
        if letter in "true":
            letters_in_true +=1
        if letter in "love":
            letters_in_love +=1
            
    for letter in name2.lower():
        if letter in "true":
            letters_in_true +=1
        if letter in "love":
            letters_in_love +=1
            
    result = str(letters_in_true) + str(letters_in_love)
    print(f"Love Score = {result}")





letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypte(message, shift):
    encrypted = ""
    for letter in message:
        if letter not in letters:
            encrypted += letter

        else:
            pos = letters.index(letter)
            new_pos = pos + shift%26
            encrypted +=(letters[new_pos])

    print(encrypted)

def decrypte(message, shift):
    decrypted = ""
    for letter in message:
        if letter not in letters:
            decrypted += letter
        else:
            pos = letters.index(letter)
            new_pos = pos - shift%26
            decrypted +=(letters[new_pos])

    print(decrypted)


# encrypte("ahmad", 2)
# decrypte("fmrfi", 5)


user_input = input("enter 1 for enrypt or 2 for decrypte or x to exit: ")

while user_input != "x":
    if int(user_input) == 1:
        message = input("enter the meassage to encrypte: ")
        shift = input("enter the shift number: ")
        encrypte(message, int(shift))
    elif int(user_input) == 2:
        message = input("enter the meassage to decrypt: ")
        shift = input("enter the shift number: ")
        decrypte(message, int(shift))


    user_input = input("enter 1 for enrypt or 2 for decrypte or x to exit: ")