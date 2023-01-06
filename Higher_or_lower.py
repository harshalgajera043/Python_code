#Higher_Lower
import random
from replit import clear
from game_data import data

def random_choice(list_of_data):
    """This function will choose a random dictionary from the list of dictionaries, print a compare message and return the follower_count of chosen person"""
    Choice_1 = random.choice(list_of_data)
    print(Choice_1)
    print(f"Compare {Choice_1['name']}, who is {Choice_1['description']} from {Choice_1['country']}.")
    list_of_data.remove(Choice_1)
    return Choice_1["follower_count"]

print(random_choice(data))

def user_input():
    """This function willl take input from user and return the value of input as a result."""
    value = input("Make a guess on city value. 'A' or 'B'").capital()
    if value == "A" or value == "B":
        return value 
    else:
        print("Please enter the valid input!!")
        return user_input()

# #first displayed item
# def random_choice(Choice_list, data_list):
#     """This function will take the list of choice and list of data as input. use list of choice to  randomly """
#     Display_choice = random.choice(Choice_list)
#     occupation = data[Choice_list.index(Display_choice)]["description"]
#     Display_score = data[Choice_list.index(Display_choice)]["follower_count"] #will take it to judge
#     Area = data[Choice_list.index(Display_choice)]["country"]
#     print(f"Compare {Display_choice}, who is {occupation} from {Area}.")
#     data.remove(data[Choice_list.index(Display_choice)])
#     return Display_score

# print(data)

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
    
