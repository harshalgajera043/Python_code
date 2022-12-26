#Hangman
import random
list_of_word = ["apple", "barries"]
computer_choice = random.choice(list_of_word)
length = len(computer_choice) #count is used to count number of time a latter occurs in the word

#generate equal number of require blanks (list)
generate_blanks = []
for i in range (0, length):
    generate_blanks += "_"

#generate equal number of require blanks (print string)
generate_blanks_str = ""
for n in generate_blanks:
    generate_blanks_str+= n
print(generate_blanks_str)

#list of word to compare it with user inputs
list_of_letters = []
for i in range(0, length):
    list_of_letters.append(computer_choice[i])
print(list_of_letters)

#while loop to continue  input untill user get the word
while computer_choice != generate_blanks_str and :
    guess_word = input("Enter a latter\n").lower()

    #(User guess a latter  which is their in our word.)
    for i in range (0, length):
        if guess_word == list_of_letters[i]:    #computer_choice != generate_blanks_str 
            generate_blanks[i] = list_of_letters[i]
        
    # print(generate_blanks)
    generate_blanks_str = ""
    for n in generate_blanks:
        generate_blanks_str+= n
    print(generate_blanks_str)

#life gone
total_life = ["H","A","N","G","M","A","N"]
life_remaining = ["_","_","_","_","_","_","_"]

while life_remaining != "HANGMAN":
    guess_word = input("Enter a latter\n").lower()
    for i in range(0,len(computer_choice)):
        if guess_word[i] != guess_word:
            life_remaining[i] = total_life
            
    
if life_remaining = "HANGMAN":
    print("GAMEOVER")
    print("you loss")
# elif guess_word != list_of_letters[i] and trail <= 7:    #hangmen != "Hangman"
#             trail += 1
#             life_remaining[trail-1] = user_wrong[trail-1]
# user_wrong = ["H","A","N","G","M","A","N"]
# life_remaining = ["_","_","_","_","_","_","_"]
# trail = 0
# print(life_remaining)