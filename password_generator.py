import string
import random

def main():
    while True:
        list = []
        length = input("How long do you want your password to be?: ")
        while(not length.isdigit() or int(length) > 32 or int(length) < 6):
            length = input("How long do you want your password to be?: ")

        while(len(list) == 0):
            choices = input("Do you want to include uppercase, numbers, or special characters?: ")

            if "uppercase" in choices:
                list.append("upper")
        

            if "numbers" in choices:
                list.append("numbers")
        

            if "special characters" in choices:
                list.append("special")

            if(len(list) > 0):
                break
                
            print("Please choose at least one! \n")
    

        password = ""

        for i in range(int(length)):
            random_value = random.randint(0, len(list))

            if random_value == len(list):
                password += random.choice(string.ascii_lowercase)
            elif list[random_value] == "upper":
                password += random.choice(string.ascii_uppercase)
            elif list[random_value] == "numbers":
                password += random.choice(string.digits)
            elif list[random_value] == "special":
                password += random.choice(string.punctuation)
    
        print(password)
        
        again = input("Do you want to play again?: (yes/no) ")
        
        while not again == "no" and not again == "yes":
            again = input("Do you want to play again?: (yes/no) ")

        if(again == "no"):
            print("Thank you for using the random password generator application!")
            break

main()