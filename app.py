


import csv


def user_find_role():
    file = open("users.csv")
    reader=csv.DictReader(file)
    for row in file:
        if row['username'] == username and 