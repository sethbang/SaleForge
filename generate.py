from classes import Customer
from data_lists import *
import random


def gen_customer():
    names = random.sample(female_names, 2)
    fname = names[0]
    mname = names[1]
    lname = random.choice(last_names)
    age = random.randint(18, 65)
    email = f"{fname[0].lower()}.{lname.lower()}{age}@gmail.com"
    address = f"{random.randint(1, 999)} Main St"
    phone = f"555-555-{random.randint(1000, 9999)}"
    gender = "female"
    budget = random.randint(100, 10000)
    interests = random.sample(item_categories, random.randint(1, 5))
    return Customer(fname, mname, lname, email, address, phone, gender, age, budget, interests)


print(gen_customer())
