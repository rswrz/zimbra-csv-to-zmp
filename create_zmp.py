#/usr/bin/env python3
import csv
import random
import string

def rndpasswd(stringLength=12):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', fieldnames=['email', 'uid', 'type', 'displayname', 'status'])
    for row in reader:
        if row['status'] == 'active':
            if row['type'] == 'account':
                print('createAccount', row['email'], rndpasswd())

