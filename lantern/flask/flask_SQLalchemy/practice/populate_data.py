import csv


def get_users():
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users
