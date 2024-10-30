name  = input("Hi im a chatbot, what is your name? ")

# esta funcion pide el año denacimiento y corrige si no introduces un numero
def year():
    try:
        years = int(input(f"Oh hi{name}, nice to  meet you, can you tell me the year you where born? "))
        return years
    except:
        print("It seems like you didn't enter a valid year please enter a number")
        year()

# esta funcion pide el mes de nacimiento y corrige si no introduces un numero o si introduces un mes que no existe
def month():
    try:
        months = int(input("introduce the number of the month"))
        if months>12 or months<0:
            print("The number of the month should be between 1 and 12")
            month()
        return months
    except :
        print("It seems like you didn't enter a valid month number please enter a number between 1 and 12")
        month()


years = year()
months = month()


# esta funcion pide el dia de nacimiento y corrige si no introduces un numero o si introduces un dia que no existe en el mes
def day():
    try:
        days = int(input("introduce the number of the day"))
        if months in [4, 6, 9, 11] or months == 2:
            if days>30:
                print("This month only has 30 days")
                day()
            elif months ==2 and days>28:
                print("the month does not have that many days")
                day()
        if days>31 or days<0:
            print("The number of the day should be between 1 and 31")
            day()
        return days
    except :
        print("It seems like you didn't enter a valid day number please enter a number between 1 and 31")
        day()

days = day()

#en caso de que la persona no haya cumplido todavia este año
if months>10 and days>22:
    years -= 1

# responde de forma personalizada
print(f"Nice {name}, you are {2024-years} old!")

hobbie = input("And do you have any hobbie? ")
print(f"Wow {name}, {hobbie} as a hobbie seems so fun!!")