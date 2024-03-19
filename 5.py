import csv

def generate_hash(s : str):
    alp = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ')
    d = {l: i for i, l in enumerate(alp, 1)}
    p = 67
    m = 1e9 + 9
    p_pow = 1
    hash_value = 0
    for chr in s:
        hash_value = (hash_value + d[chr] * p_pow) % m
        p_pow = (p_pow * p)
    return int(hash_value)


student_with_hash = []
with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter = ',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        student_with_hash.append(row)
with open('students_with_hash.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writeheader()
    w.writerows(student_with_hash)