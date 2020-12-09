import random
from faker import Faker
from unidecode import unidecode

class Catchall:
    def __init__(self, catchall):

        if "@" not in catchall[0] or "." not in catchall:
            raise ValueError(f"{catchall} is not a valid catchall adress.")

        self.catchall = catchall

    def variations(self, gender="random"):

        faker = Faker()

        if gender == "random":
            firstname = unidecode(faker.first_name().lower())
        elif gender == "male":
            firstname = unidecode(faker.first_name_male().lower())
        elif gender == "female":
            firstname = unidecode(faker.first_name_female().lower())

        lastname = unidecode(faker.last_name().lower())

        variations = [
            firstname + "." + lastname[random.randrange(1, len(lastname))] + "." + lastname,
            lastname + "." + firstname[random.randrange(1, len(firstname))] + "." + firstname,
            firstname + lastname,
            firstname + lastname + str(random.randrange(10,999)),
            lastname + firstname,
            lastname + firstname + str(random.randrange(10,999)),
            firstname + "." + lastname,
            lastname + "." + firstname,
            firstname[0] + lastname,
            firstname + lastname[random.randrange(1, len(lastname))] + lastname
        ]

        return variations
    
    def generate(self):
        return random.choice(self.variations()) + self.catchall
    
    def generate_male(self):
        return random.choice(self.variations(gender="male")) + self.catchall
    
    def generate_female(self):
        return random.choice(self.variations(gender="female")) + self.catchall