import random

test_seed = int(input("Create a seed mumber: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(",")

num_items = len(names)
random_choice = random.randint(0, num_items -1 )
person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy meal today!" )




