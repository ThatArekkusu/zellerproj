# zeller programme

def zeller():
    months = [
        "January",
        "Feburary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    days = [f"{i:02}" for i in range(1, 32)] 
    #Iterates i in the format of a 2 digit number (i:02) in the range of 1, 32 (1 ... 31) making single digits 2 digits

    print("Welcome to the Zeller Programme,\n Input the date of your birth in the order prompted and it will compute the day of the week you were born on!")

    userYear = input("\nWhat year were you born on?: ")
    if len(userYear) != 4:
        print("\nError, Incorrect format, make sure your year is in the format YYYY\n")
    else:
        try:
            userYear = int(userYear)
        except ValueError:
            print("\nError, Incorrect format, make sure your year is in the format YYYY\n")
        # Error handling for year formatting

    userMonth = input("\nWhat month were you born on?: ")
    if userMonth not in months:
        print("\nError, Incorrect format, make sure the first letter is captial and in the format MM\n")
        return()
        # Error handling for month formatting

    userDays = input("\nInput the day you were born on. Ex. 02, Ensure to put in 2 digit format: ")
    if userDays not in days:
        print("\nError, Incorrect format, make sure your day is in the format DD\n")
    else:
        try:
            userDays = int(userDays)
        except ValueError:
            print("\nError, Incorrect format, make sure your day is in the format DD\n")
        # Error handling for number formatting

    det = int(input("\nWould you like to add additional information? 1 for yes, 2 for no: "))
    if det == 1:
        additionalinfo(det, userYear, userMonth, userDays, months)
    elif det == 2:
        zelleralgo(det, userYear, userMonth, userDays, months, birthplace="")
    


def additionalinfo(det, userYear, userMonth, userDays, months):
    birthplace = input("\nWhere where you born?: ")
    if birthplace == "":
        print("\nError please enter a location")
        return()
        # anticipates user not putting in an input and restarts the function if this happens
    else:
        zelleralgo(det, userYear, userMonth, userDays, months, birthplace)
            
def zelleralgo(det, userYear, userMonth, userDays, months, birthplace):
    daysindex = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    x = int((months.index(userMonth)) + 1)
    # references the index to parse the month to an integer
    if x == 1:
        x += 12
    elif x == 2:
        x += 12
    # accounts for january and feburary needing to be 13 & 14 in zeller algorithm

    X = userDays  # Day of the month
    Y = userYear % 100  # Year within the century
    Z = userYear // 100  # Century

    # Zeller's formula
    h = (X + ((13 * (x + 1)) // 5) + Y + (Y // 4) + (Z // 4) + (5 * Z)) % 7

    
    msg = (f"\nYou were born on a {daysindex[h]}")
    if det == 1:
        msg += (f" in {birthplace}")

    msg += "."

    print(msg) 

zeller()