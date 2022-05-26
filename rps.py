#Practice Python: Rock, Paper, Scissors 


import string, random, sys


rock = "rock"
paper = "paper"
scissors = "scissors"
global rps 
rps = ("rock", "paper", "scissors")
#rps_dic = {1: "rock", 2: "paper", 3: "scissors"}
end_program = "Sho'Nuff is the Master"




class class_rps: 

    #unnecessary but defining static data members/variables in class good stucture
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    rps = ("rock", "paper", "scissors")
    #rps_dic = {1: "rock", 2: "paper", 3: "scissors"}
    end_program = "Sho\'Nuff is the Master"


     #unnecessary but defining constructor in class good stucture
    def __init__(self, rock, paper, scissors, rps):
        return super().__init__(rock, paper, scissors, rps)

   
    @staticmethod    
    def func_rand():
        #randomize the values in tuple
        rand_rps = random.choice(class_rps.rps) 
        return rand_rps
        pass

    #Conditional parameter for function rock 
    def func_rock(rand_rps):
        print(rand_rps.title())
        if rand_rps == class_rps.rock:
            print("Draw, try again.\n")
        elif rand_rps == paper:
            print("Paper covers rock, I win.\n")
        elif rand_rps == scissors:
            print("Rock breaks scissors, you win.\n")
        else:
            raise Exception("The Gods are Angry.\n")
        pass


    #Conditional parameter for function paper 
    def func_paper(rand_rps): 
        print(rand_rps.title())
        if rand_rps == class_rps.paper:
            print("Draw, try again.\n")
        elif rand_rps == scissors:
            print ("Scissors cuts paper, I win.\n")
        elif rand_rps == rock:
            print("Paper covers rock, you win.\n") #redun
        else:
            raise Exception("The Gods are Angry.\n")
        pass

    #Conditional parameter for function paper
    def func_scissors(rand_rps):
        print(rand_rps.title())
        if rand_rps == class_rps.scissors:
            print("Draw, try again.\n")
        elif rand_rps == rock:
            print("Rock breaks scissors, I win.\n") #redun
        elif rand_rps == paper:
            print("Scissors cuts paper, you win.\n") #redun
        else:
            raise Exception("The Gods are Angry.\n")
        pass

    def func_done():
        sys.exit
        pass
    

while True:
    #User Input
    u_rps = input("Rock, Paper, Scissors say shoot: ")
    l_rps = u_rps.lower()
    rand_rps = class_rps.func_rand()
    if l_rps == class_rps.rock:
        class_rps.func_rock(rand_rps)
    elif l_rps == class_rps.paper:
        class_rps.func_paper(rand_rps)
    elif l_rps == class_rps.scissors:
        class_rps.func_scissors(rand_rps)
    elif u_rps != class_rps.rps:
        print("Please type rock, paper, or scissors")
        print("To quit type \"Sho'Nuff is the Master\"\n")
    elif u_rps == 1: #class_rps.end_program:
        class_rps.func_done
    else:   
        raise Exception("The Gods are Angry.\n")
    


