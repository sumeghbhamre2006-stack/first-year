#Create an intelligent agent which helps user,decide what to eat on their preferences.
menu = {
    "Breakfast": {
        "Indian": ["Idli", "Dosa", "Misal", "Chole Bhature"],
        "Chinese": ["Congee", "Noodles", "Steamed Bun", "Egg filled Pancakes"],
        "Italian": ["Cornetti", "Maritozzi", "Cappacino"]
    },
    "Lunch": {
        "Indian": ["Veg kofta", "Chicken korma", "Mutton khema", "Boti ki biryani"],
        "Chinese": ["Spring rolls", "Chowmein", "Charsiu"],
        "Italian": ["Pizza", "Pasta", "Pork chop milanese"]
    },
    "Dinner": {
        "Indian": ["Paneer Tikka", "Butter Chicken", "Chicken Tandoori"],
        "Chinese": ["Beef and Broccoli", "Crispy Beef", "Sesame Chicken"],
        "Italian": ["Salad", "Veal Piccata", "Riso al Salto"]
    }
}


x = input("Choose your Meal:\nBreakfast, Lunch, Dinner\nAns: ")
y = input("Enter your preferred cuisine:\nIndian, Chinese, Italian\nAns: ")


if x == "Breakfast":
    if y in menu["Breakfast"]:
        print("\nHere are some " + y + " breakfast options for you:")
        for dish in menu["Breakfast"][y]:
            print("- " + dish)
    else:
        print("Sorry, we don't have that cuisine for breakfast.")

elif x == "Lunch":
    if y in menu["Lunch"]:
        print("\nHere are some " + y + " lunch options for you:")
        for dish in menu["Lunch"][y]:
            print("- " + dish)
    else:
        print("Sorry, we don't have that cuisine for lunch.")

elif x == "Dinner":
    if y in menu["Dinner"]:
        print("\nHere are some " + y + " dinner options for you:")
        for dish in menu["Dinner"][y]:
            print("- " + dish)
    else:
        print("Sorry, we don't have that cuisine for dinner.")

else:
    print("Invalid meal type. Please enter 'Breakfast', 'Lunch', or 'Dinner'.")
