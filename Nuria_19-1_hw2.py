
class Company:
    def __init__(self, company_bank, company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):
    def __init__(self, company_bank, company_name, first_name, last_name, salary):
        super().__init__(company_bank, company_name)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self.company_bank <= self.salary:
            return "У компании не достаточно средств!"
        else:
            self.company_bank -= self.salary
            return self.salary

    def person_info(self):
        print(f""" 
Name: {self.first_name} 
Last_name: {self.last_name}
PersonSalary: {self.get_salary()}""")


tom = Person(10000, "Opera", "Baron", "Tom", 2500)
tom.person_info()
tom.person_info()
tom.person_info()
tom.person_info()
tom.person_info()




