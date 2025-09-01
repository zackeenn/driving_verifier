#data types are data restored in any kind of variable
#john needs to say his height, weight, name, age and if he drives

"""program1 is an exercise for data types"""

def program1 ():
    name = input("What is your name: ")
    age = int(input("How old are you: "))
    height = float(input("What is your height (cm): "))
    weight = float(input("What is your weight(kg): "))
    drive = input("Do have the permission to drive: ")

    if drive.lower() == "yes":
        print("Hope you drive well, we appreciate your sign up.")
    else:
        print("You need to drive to sign up.")
        
    
#call the funcion u want by calling it by its name
program1()
