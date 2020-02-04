

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


word = "hippopotamus"
toDisplay=""
completed=False

length_word = len(word)

for x in range(length_word):
    toDisplay+="_|"

i = 0

no_of_tries = 8

print ("Hint: animal")

while (i < no_of_tries and  not completed ):
    #while (correctAttempt):
        print (toDisplay)
        input_char=input("Guess a character > ")

        if input_char[0] in word:
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
            print ("You have ",attempts," attempts left")
            correctAttempt = True

if completed:
    print ("\n*** You have won the round !! ")
    print (toDisplay)
else:
    print ("You have exhausted all your attempts. Better luck next time ")
