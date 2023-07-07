class Customer:
    def __init__(self, fname, mname, lname, email, address, phone, gender, age, budget, interests):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.email = email
        self.address = address
        self.phone = phone
        self.gender = gender
        self.age = age
        self.budget = budget
        self.interests = interests

    def __str__(self):
        return f"Name: {self.fname} {self.mname} {self.lname}\n Email: {self.email}\n Age: {self.age}\n Gender: {self.gender}\n Address: {self.address}\n Phone: {self.phone}\n Budget: {self.budget}\n Interests: {self.interests}"

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_budget(self):
        return self.budget

    def set_budget(self, new_budget):
        self.budget = new_budget

    def spend_budget(self, amount):
        if amount > self.budget:
            return False  # Not enough budget
        else:
            self.budget -= amount
            return True  # Budget spent successfully

    def get_interests(self):
        return self.interests
