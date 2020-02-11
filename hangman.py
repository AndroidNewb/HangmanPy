import random
import os
from os import system, name

word=''
hint=''
words=[]
hangman_disp_array=["=============|","             |","            (.)","            /|\\","           / | \\","            / \\","           /   \\"]


# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    return

def find_indices_of_substr(input_str, search_str):
    indices = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return indices
        indices.append(i)
        index = i + 1
    return indices

def init_game():
    # List all files in a directory using scandir()
    basepath = 'data/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                file1 = open(entry, 'r')
                temp=file1.readlines()
                category=entry.name.split(".")[0]
                for s in temp:
                    words.append(s.rstrip()+":"+category)
                #words.extend(file1.readlines()) # This had all the words availble for game
    return


def get_random_word():
    random_index=random.randrange(0,len(words), 3)
    random_entry=words[random_index]
    #print(random_entry)
    global word
    global hint
    word=random_entry.split(":")[0]
    hint=random_entry.split(":")[1]
    #print("completed get_random_word",word,"  ",hint)
    return

def display_hangman(no_of_failed_attempts):
    for i in range(no_of_failed_attempts):
        print(hangman_disp_array[i])
    return


init_game()
get_random_word()


toDisplay=""
completed=False

length_word = len(word)

for x in range(length_word):
    toDisplay+="_|"

i = 0

no_of_tries = 7



while (i < no_of_tries and  not completed ):
    #while (correctAttempt):
        clear()
        if (i > 0):
            display_hangman(i)
        print ("\nHint: ",hint)
        print ("\n",toDisplay)
        input_char=input("Guess an alphabet > ")
        if input_char.isspace() or len(input_char)==0:
            print ("** invalid alphabet entered **")
            continue

        if input_char[0] in word and input_char[0] not in toDisplay:
            locs_of_char=find_indices_of_substr(word,input_char[0])
            toDisplay=list(toDisplay)
            for loc in locs_of_char:
                toDisplay[loc*2]=input_char[0]

            toDisplay="".join(toDisplay)
            if "_" not in toDisplay:
                completed=True
        elif input_char[0] not in word:
            #correctAttempt = False
            i=i+1
            attempts=no_of_tries - i
            if attempts > 0:
                #display_hangman(i)
                print ("** Incorrect guess ** You have ",attempts," attempts left")
            correctAttempt = True
        elif input_char[0] in toDisplay:
            print ("** You have already enetered the alphabet. Try another **")
if completed:
    print ("\n*** You have won the round !! ")
    print (toDisplay)
else:
    clear()
    display_hangman(7)
    print ("** GAME OVER **. Better luck next time ")
    print ("The word was ",word)
