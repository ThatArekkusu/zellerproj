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

    useryear = int(input("What year were you born on?:"))
    if useryear != len(4):
        print("Error, Incorrect format, make sure youe year is in the format YYYY")
        exit()
        # Error handling for year formatting

    usermonth = str(input("What month were you born on?: "))
    if usermonth not in months:
        print("Error, Incorrect format, make sure the first letter is captial and in the format MM\n")
        exit()
        # Error handling for month formatting

    userdays = str(input("Input the day you were born on. Ex. 02, Ensure to put in 2 digit format: "))
    if userdays not in days:
        print("Error, Incorrect format, make sure your day is in the format DD\n")
        exit()
        # Error handling for number formatting

    det = int(input("Would you like to add additional information? 1 for yes, 2 for no: "))
    if det == 1:
        additionalinfo()
    if det == 2:
        zelleralgo(useryear, usermonth, userdays, months, days)
    


def additionalinfo():
    birthplace = str(input("Where where you born?"))
    if birthplace == "":
        print("Error please enter a location")
        additionalinfo()
        # anticipates user not putting in an input and restarts the function if this happens
    else:
        zelleralgo()
            
def zelleralgo(usermonth, userdays, months, days, birthplace, useryear):
    daysindex = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    x = int((months.index(usermonth)) + 1)
    # references the index to parse the month to an integer
    if x == 1:
        x += 12
    elif x == 2:
        x += 12
    # accounts for january and feburary needing to be 13 & 14 in zeller algorithm

    y = userdays

    z = float(useryear / 100)

    

zeller()