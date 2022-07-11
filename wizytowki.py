"""
Za nic mi to dalej nie chce zadziałać
import Faker
fake = Faker()
fake = Faker(['en_US'])
"""
class BaseContact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    def __str__(self):
        return f'{self.name} {self.number} {self.email}'
    def __gt__(self, other):
        return self.name > other.name
    def contact(self):
        print(f"I'm contacting {self.name} {self.number} {self.email}")
    def label_length(self):
        print(len(self.name))
class BusinessContact(BaseContact):
    def __init__(self, work_number, company, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_number = work_number
        self.company = company
        self.position = position
    def contact_work(self):
        print(f"I'm contacting {self.name} {self.work_number} {self.company}")
    def __str__(self):
        return f'{self.name} {self.work_number} {self.company} {self.position}'
"""
def create_contacts(contact_type, amount):
    for count in amount:
        contact.contact_type
"""
per1 = BaseContact(name="Jan Kowalski", number="123456789", email="sample@sample.co")
per1_1 = BusinessContact(work_number="987654321", company="Lidl", position="CEO", name=per1.name, email=per1.email, number=per1.number)
print(per1)
print(per1_1)