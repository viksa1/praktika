import csv
import string
import random


def create_login(s: string):
    names = s.split()
    return f'{names[0]}_{names[1][0]}{names[2][0]}'
def password_generation():
    chr = string.ascii_letters + string.digits
    password = ''.join(random.choice(chr) for _ in range(8))
    return password

students_with_password = []
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['login'] = create_login(row['Name'])
        row['password'] = password_generation()
        students_with_password.append(row)
with open('students_with_password.csv', 'w', newline = '', encoding='utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['id','Name','titleProject_id','class','score', 'login', 'password'])
    w.writeheader()
    w.writerows(students_with_password)