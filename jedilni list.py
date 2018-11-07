print "Welcome to your daily menu input application."

menu = {}

while True:
	meal = raw_input("Please enter name of the dish: "),
	price = raw_input("Please enter price of the dish:"),
	menu[meal] = price
	print menu

	new = raw_input("Would you like to add another dish? ( y / n )")
	if new == "n":
	    break

menu_file = open("menu.txt", "w+")

print "Today's menu: %s " % menu


with open("menu.txt", "w+") as menu_file:
    for dish in menu:
        menu_file.write("%s, %s EUR\n" % (dish, menu[dish]))

print "See you tommorow!"
