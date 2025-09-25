# Build a basic intelligent in python that acts as decision maker based on user input

tourist_destinations = {
    "Summer": {
        "March": ["Maldives", "Singapore", "Cambodia", "Japan (Cherry blossoms)", "Bhutan"],
        "April": ["Thailand", "Italy", "Bali", "Munnar", "Manali"],
        "May": ["Canada", "Spain", "Greece", "Morocco", "Leh"]
    },
    "Rainy": {
        "June": ["Mauritius", "Denmark", "Peru", "Coorg", "Auli"],
        "July": ["Santorini", "Rome", "Venice", "Croatia", "Portugal"],
        "August": ["Varanasi", "Udaipur", "Kodaikanal", "Cherrapunji", "Ladakh"]
    },
    "Spring": {
        "September": ["Zurich", "Sicily", "Tanzania", "Oahu", "Paris"],
        "October": ["New Zealand", "Vietnam", "Egypt", "Mexico", "Jordan"],
        "November": ["Hong Kong", "UAE", "Sri Lanka", "Indonesia", "Argentina"]
    },
    "Winter": {
        "December": ["Goa", "Jaisalmer", "Andaman & Nicobar"],
        "January": ["Costa Rica", "Iceland", "Norway"],
        "February": ["Gulmarg", "Puri", "Jodhpur"]
    }
}


x = input("Choose your Preferred Season:\nSummer, Rainy, Spring, Winter\nAns: ")


if x in tourist_destinations:
  
    valid_months = list(tourist_destinations[x].keys())
    
   
    y = input(f"Enter your preferred Month for {x} season. Valid months are: {', '.join(valid_months)}\nAns: ")
    
 
    if y in valid_months:
        print(f"\nHere are some tourist destinations for you in {x} season during {y}:")
        for destination in tourist_destinations[x][y]:
            print("- " + destination)
    else:
        print(f"Sorry, {y} is not a valid month for {x} season.")
else:
    print("Invalid season. Please choose from 'Summer', 'Rainy', 'Spring', or 'Winter'.")


