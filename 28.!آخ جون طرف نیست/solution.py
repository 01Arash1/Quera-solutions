day_person_1 = int(input())
person1 = input()
person_1 = set(person1.split(" "))
day_person_2 = int(input())
person2 = input()
person_2 = set(person2.split(" "))
day_person_3 = int(input())
person3 = input()
person_3 = set(person3.split(" "))

not_my_day = len(person_1.union(person_2.union(person_3)))
my_day = 7 - not_my_day

print(my_day)