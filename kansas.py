from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"

def randomfunfact():
    # don't forget the commas
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the statem by many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")

    print(funfacts[int(index)])

# remember, two equals signs for comparing
# this file will run this function if it is the main file
# that can be very useful when creating modules
# this if also prevents module from including this function in what's available to import 
if __name__ == "__main__":
    randomfunfact()