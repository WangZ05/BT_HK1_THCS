meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 =['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
def menu_is_boring(meals):
    for i in meals:
        if meals.index(i)+1 == len(meals):
            return False
        if i == meals[meals.index(i)+1]:
            return True

print(menu_is_boring(meals_1))    
print(menu_is_boring(meals_2))