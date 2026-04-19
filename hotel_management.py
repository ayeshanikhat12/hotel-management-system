rooms = {}
bills = {}
current_room = None

def book_room():
    global current_room
    name = input("Enter name: ")
    room = input("Enter room no: ")
    
    if room in rooms:
        print("Already booked!")
    else:
        rooms[room] = name
        bills[room] = 0
        current_room = room
        print("Room booked & selected!")
        print("Welcome", name)

def order_food():
    if current_room is None:
        print("Book room first!")
        return
    
    # FOOD
    print("\nFood Menu")
    print("1.Pizza-200  2.Burger-100  3.Sandwich-100")
    food = input("Enter food choices (e.g. 1 2): ").split()
    
    for f in food:
        if f == "1":
            bills[current_room] += 200
        elif f == "2":
            bills[current_room] += 100
        elif f == "3":
            bills[current_room] += 100

    # DRINKS
    print("\nDrinks Menu")
    print("1.Coke-50  2.ColdCoffee-100  3.HotCoffee-80")
    drink = input("Enter drink choices (e.g. 1 3): ").split()
    
    for d in drink:
        if d == "1":
            bills[current_room] += 50
        elif d == "2":
            bills[current_room] += 100
        elif d == "3":
            bills[current_room] += 80

    
    print("\nTotal Bill:", bills[current_room])
    print("Thank you,", rooms[current_room], "! Visit again 😊")

# MAIN MENU
while True:
    print("\n1.Book Room")
    print("2.Order Food/Drinks")
    print("3.Exit")
    
    ch = int(input("Choice: "))
    
    if ch == 1:
        book_room()
    elif ch == 2:
        order_food()
    elif ch == 3:
        print("Goodbye 😊")
        break
    else:
        print("Invalid choice")
