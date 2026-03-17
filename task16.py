min_age = None
age1 = int(input('son kiriting:'))
min_age = age1
for i in range(7 - 1):
    age = int(input('son kiriting:'))
    if age < min_age:
        min_age = age
print(min_age)