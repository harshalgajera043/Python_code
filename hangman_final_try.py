# #hangman
# import random
# life_of_choice = ["apple", "barries"]
# computer_choice = random.choice(life_of_choice)
# # print(computer_choice)
# choice_length = len(computer_choice)
# computer_choice_lst = []
# for latter in range(0,choice_length):
#     computer_choice_lst += computer_choice[latter]
# # print(computer_choice_lst)

# generate_blank = []
# for i in range(0,choice_length):
#     generate_blank += "_"
# # print(generate_blank)

# generate_blank_str = ""
# for n in generate_blank:
#     generate_blank_str += n
# print(generate_blank_str)

# #ask user for input
# user_input = input("Enter a latter.\n").lower()

# for i in range(0,choice_length):
#     if computer_choice_lst[i] == user_input:
#         generate_blank[i] = computer_choice_lst[i]
#         update_blank = ""
#         for latter in generate_blank:
#             generate_blank_str[i] == latter
#         print(generate_blank_str)
#     #     if update_blank != generate_blank_str:
#     #         print(update_blank)
        
#     # print(generate_blank_str)
        
    


# # for i in range(0,choice_length):
#     # if computer_choice_lst[i] != user_input:
        
# # print(computer_choice_lst)
# # print(generate_blank)















#NEW START
#Hangman
import random
list_of_word = ["apple", "barries"]
computer_choice = random.choice(list_of_word)
length = len(computer_choice) #count is used to count number of time a latter occurs in the word
#list of lattter in computer choice
computer_choice_lst = []
for latter in computer_choice:
    computer_choice_lst += latter
print(computer_choice_lst)

#generate equal number of require blanks (print string)
generate_blanks_str = ""
for letter in computer_choice:
    generate_blanks_str+= "_"
print(generate_blanks_str)
#list of blanks
blank_lst = []
for blank in generate_blanks_str:
    blank_lst += blank
print(blank_lst)

#game over condition for losser
loss = ["h","a","n","g","m","a","n"]
life_remaining_lst = ["_","_","_","_","_","_","_"]
# life_remaining = ""
# for life in life_remaining_lst:
#     life_remaining += "_"
# print(life_remaining)
trail = 0

#while loop to continue  input untill user get the word
while computer_choice_lst != blank_lst and life_remaining_lst != loss:
    guess_word = input("Enter a latter\n").lower()
    remember_value = blank_lst.copy() #every time before changing value of blank this variable will remember the earlier value this cariers
    
    #(User guess a latter  which is their in our word.)
    for i in range(0,length):
        if  guess_word == computer_choice[i]:
            blank_lst[i] = guess_word
    print(blank_lst)
    print(remember_value)
    
    if remember_value == blank_lst:
        trail += 1
        life_remaining_lst[trail-1] = loss[trail-1]
    print(life_remaining_lst)
    life_remaining = ""
    for life in life_remaining_lst:
        life_remaining += life
    print(life_remaining)









#     for i in range (0, length):
#         if guess_word == list_of_letters[i]:    #computer_choice != generate_blanks_str 
#             generate_blanks[i] = list_of_letters[i]
        
#     # print(generate_blanks)
#     generate_blanks_str = ""
#     for n in generate_blanks:
#         generate_blanks_str+= n
#     print(generate_blanks_str)

# #life gone
# total_life = ["H","A","N","G","M","A","N"]
# life_remaining = ["_","_","_","_","_","_","_"]

# while life_remaining != "HANGMAN":
#     guess_word = input("Enter a latter\n").lower()
#     for i in range(0,len(computer_choice)):
#         if guess_word[i] != guess_word:
#             life_remaining[i] = total_life
            
    
# if life_remaining = "HANGMAN":
#     print("GAMEOVER")
#     print("you loss")
# # elif guess_word != list_of_letters[i] and trail <= 7:    #hangmen != "Hangman"
# #             trail += 1
# #             life_remaining[trail-1] = user_wrong[trail-1]
# # user_wrong = ["H","A","N","G","M","A","N"]
# # life_remaining = ["_","_","_","_","_","_","_"]
# # trail = 0
# # print(life_remaining)