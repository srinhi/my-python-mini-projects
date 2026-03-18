list = []

def add(task):
    list.append(task)


def remove(n):
    list.pop(n)


def view():
    if(len(list) == 0):
        print("Your list is empty!")
        return

    counter = len(list) - 1

    for i in range(len(list)):
        if(counter == 0):
            print(str(i + 1) + ". " + list[i])
        else:
            print(str(i + 1) + ". " + list[i] + "\n")
        
        counter = counter - 1

def main():
    while True:
        option = input("Choose a valid menu option: \n 1. Add \n 2. Remove \n 3. View \n 4. Quit \n: ")
    
        while(not option.isdigit() or (int(option) > 4 or int(option) < 1)):
            option = input("Choose a valid menu option: \n 1. Add \n 2. Remove \n 3. View \n 4. Quit \n: ")

        if(int(option) == 4):
            break

        if(int(option) == 1):
            addition = input("What do you want to add to the list?: ")
            add(addition)
    
        if(int(option) == 2):
            view()
            subtraction = input("What do you want to remove from the list? (Enter a number from 1): ")

            while not subtraction.isdigit() or int(subtraction) <= 0 or int(len(list)) < int(subtraction):
                subtraction = input("Enter a valid number: ")
        
            remove(int(subtraction) - 1)

        if(int(option) == 3):
            view()

    print("Thank you for visiting my list app!")

main()