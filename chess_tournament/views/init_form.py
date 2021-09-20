"""Get tournament initialization details from User

"""


from typing import NamedTuple


def get_input():
    """Get user input and return the data as a dictionary"""
    # Rating choices, default is 'rapid'
    ratings = ('rapid', 'blitz', 'bullet')
    option = 0

    # Tournament name and location
    name = input("Enter tournament's name: ")
    location = input("Enter tournament's location: ")

    # Rating choice. Loop until user enter a valid option
    while True:
        rating = input("Rating type :\n    1 rapid\n    2 blitz\n    3 bullet\n    Rating ? (1-3, default=1) ")
        try:
            rating = int(rating)
            if rating > 0 and rating <= 3:
                option = int(option) - 1
                break
        except ValueError:
            continue

    # End date
    end = input("Enter length of the tournament : (days) ")

    return {'name': name, 'location': location, 'rating': ratings[option], 'end': int(end)}
