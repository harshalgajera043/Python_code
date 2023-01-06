#Higher_Lower
import random
from replit import clear
from game_data import data

def random_city(Option_list, Option_dictionary):
    """This function will choose and return a random city from a given list of options and remove that city from main list."""
    display_1 = random.choice(Option_list)
    print(display_1)
    # count = Option_dictionary[display_1]
    # print(count)
    Option_list.remove(display_1)
    return display_1

def user_input():
    """This function willl take input from user and return the value of input as a result."""
    value = input("Make a guess on city value. 'Higher' or 'Lower'").title()
    if value == "Higher" or value == "Lower":
        return value 
    else:
        print("Please enter the valid input!!")
        return user_input()

Choice_list = []
for i in range(0,len(data)):
    Name = data[i]["name"]
    Choice_list.append(Name)
print(Choice_list)

#first displayed item
def random_choice(Choice_list, data_list):
    """This function will take the list of choice and list of data as input. use list of choice to  randomly """
    Display_choice = random.choice(Choice_list)
    occupation = data[Choice_list.index(Display_choice)]["description"]
    Display_score = data[Choice_list.index(Display_choice)]["follower_count"] #will take it to judge
    Area = data[Choice_list.index(Display_choice)]["country"]
    print(f"Compare {Display_choice}, who is {occupation} from {Area}.")
    data.remove(data[Choice_list.index(Display_choice)])
    return Display_score

print(data)

# save = True
# score = 0
# while save == True:
#     print("VS")
#     if len(Choice_list) != 0:
#         #using random_city function to make a random choice of city from modified list of city
#         Second_city = random_city(Choice_list, Choice_dictionary) #our function is printing the second city so no need to add print statement here.
#         guess_score = Choice_dictionary[Second_city]
#         # print(guess_score)
#         # print(Choice_list)
#         guess = user_input()
#         # print(guess)
#         if guess == "Higher" and Display_score <= guess_score:
#             score += 1
#             Display_city = Second_city
#             Display_score = guess_score
#             clear()
#             print(Display_city)
#             print(Display_score)
#         elif guess == "Lower" and Display_score >= guess_score:
#             score += 1
#             Display_city = Second_city
#             Display_score = guess_score
#             clear()
#             print(Display_city)
#             print(Display_score)
#         else:
#             save = False
#             clear()
#     else:
#         save = False
#         clear()
        
# #Review user score
# if score > 10:
#     print(f"Greaaaat!! {score} is excellent score.")
# elif score > 7:
#     print(f"Goooooood!! {score} is above avarage score.")
# elif score > 4:
#     print(f"Nooot Bad!! {score} is avarage score.")
# elif score>0:
#     print(f"ooooooooo!! {score} is too bad.")
# elif score == 0:
#     print("Diaster!! it's seems like you go and comeback with out playing.")
    
