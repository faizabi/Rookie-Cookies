import random as rd

rock =  '''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a 

'''
scissors = '''
                     88                                                       
                     ""                                                       
                                                                              
,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  
I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    ""  
 `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,   
aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I  
`"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"ybbdP"'  `"YbbdP"'  88         `"YbbdP"' 

'''
paper = '''

8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
88                     88                                 
88                     88                                

'''
print("GAME STARTS!\n")
player_input = int(input("Enter 0 to throw a rock, Enter 1 to throw a paper and Enter 2 to throw a pair of Scissors : \n"))

if player_input==0:
    print(f"You Chose :\n {rock}")
elif player_input==1:
    print(f"You Chose :\n {paper}")
elif player_input==2:
    print(f"You Chose :\n {scissors}")
else:
    print("Invalid Choice. Pls enter from 0,1 or 2")

list_of_choices = [rock, paper, scissors]
mach_choice = rd.choice(list_of_choices)
print(f"The Computer Chose : \n {mach_choice}")

if player_input==0 and mach_choice==rock:
    print("It's a Tie")
elif player_input==0 and mach_choice==paper:
    print("Computer Wins!")
elif player_input==0 and mach_choice==scissors:
    print("You Win!")
elif player_input==1 and mach_choice==rock:
    print("You Win!")
elif player_input==1 and mach_choice==paper:
    print("It's a Tie")
elif player_input==1 and mach_choice==scissors:
    print("Computer Wins!")
elif player_input==2 and mach_choice==rock:
    print("Computer Wins!")
elif player_input==2 and mach_choice==paper:
    print("You Win!")
elif player_input==2 and mach_choice==scissors:
    print("It's a Tie")

          
