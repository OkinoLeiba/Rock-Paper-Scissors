#Practice Python: Rock, Paper, Scissors 


import string 
import random


rock = "rock"
paper = "paper"
scissors = "scissors"
global rps 
rps = ("rock", "paper", "scissors")
rps_dic = {1: "rock", 2: "paper", 3: "scissors"}


def func_rand():
    #randomize the values in tuple
    ran_rps = random.choice(rps)  
    return ran_rps
    pass


class class_rps: 

    #Conditional parameter for function rock 
    def func_rock():  
        if ran_rps == rock:
            print("Draw, try again.")
        elif ran_rps == paper:
            print("Paper covers rock, you win.")
        elif ran_rps == scissors:
            print("Rock breaks scissors, I win.")
        else:
            raise Exception("The Gods are Angry")
        pass


    #Conditional parameter for function paper 
    def func_paper():  
        if ran_rps == paper:
            print("Draw, try again.")
        elif ran_rps == scissors:
            print ("Scissors cuts paper, I win.")
        elif ran_rps == rock:
            print("Paper covers rock, you win.") #redun
        else:
            raise Exception("The Gods are Angry")
        pass

    #Conditional parameter for function paper
    def func_scissors():
        if ran_rps == scissors:
            print("Draw, try again.")
        elif ran_rps == rock:
            print("Rock breaks scissors, I win.") #redun
        elif ran_rps == paper:
            print("Scissors cuts paper. you win.") #redun
        else:
            raise Exception("The Gods are Angry")
        pass



    
f_rps = 'fin'
while f_rps != rps:
    #User Input
    u_rps = input("Rock, Paper, Scissors say shoot: ")
    l_rps = u_rps.lower()
    func_rand()
    if l_rps == rock:
        class_rps.func_rock()
    elif l_rps == paper:
        class_rps.func_paper()
    elif l_rps == scissors:
        class_rps.func_scissors()
    else:
        exit
    


