'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def find_all_indexes(input_str, search_str):
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


word = "chocolate"
toDisplay=""
correctAttempt=True

length_word = len(word)

for x in range(length_word):
    toDisplay+="*"

i = 0

no_of_tries = 3 

print ("Hint: Sweet")

while (i < no_of_tries and ("*"  in toDisplay) ):
    while (correctAttempt):
        print (toDisplay)
        input_char=input("Guess a character > ")
        
        if input_char[0] in word:
            locs_of_char=find_all_indexes(word,input_char[0])
            toDisplay=list(toDisplay)
            for loc in locs_of_char:
                toDisplay[loc]=input_char[0]
            toDisplay="".join(toDisplay)
        elif input_char[0] not in word:
            correctAttempt = False
            i=i+1
            attempts=no_of_tries - i
            print ("You have ",attempts," attempts left")
            correctAttempt = True
            break
        


    