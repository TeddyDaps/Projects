import csv #Importing the CSV module for the purpose of managing CSV files in a program.

def login(username,password): # The function processes the provided username and password
    file=open("users.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['username'] == username and row['password'] == password:
            return row['role']
    return None

def is_valid(username,password): # Executes an authentication process utilizing the provided username and password.
    with open("users.csv") as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
        return False
