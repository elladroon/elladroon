name  = input("Hi im a chatbot, what is your name? ")


def year():
    try:
        years = int(input(f"Oh hi{name}, nice to  meet you, can you tell me the year you where born? "))
        return years
    except:
        print("It seems like you didn't enter a valid year please enter a number")
        year()

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


print(f"Nice {name} you are {2024-years} old!")

hobbie = input("And do you have any hobbie? ")
print(f"Wow {name}, {hobbie} as a hobbie seems so fun!!")
