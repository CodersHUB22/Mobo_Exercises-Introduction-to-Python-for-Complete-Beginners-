import datetime 
# we will use this for the date objects

class Celebrity:

    def __init__(self, fullname, stagename, birthdate, address, telephone, email):
        self.fullname = fullname
        self.stagename = stagename
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

Celebrity = Celebrity(
    "Real Name: Hope Elizabeth Soberano",
    "Alias: Liza Soberano",
    datetime.date(1997, 10, 11), # year, month, day
    "Complete Address: Santa Clara, California, United States",
    "Telephone Number: 09068657914",
    "Email Address: lizasoberano@gmail.com"
)

print(Celebrity.fullname)
print(Celebrity.stagename)
print(Celebrity.address)
print(Celebrity.telephone)
print(Celebrity.email)
print(Celebrity.age())
