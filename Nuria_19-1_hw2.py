
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
        print()

    def get_salary(self):
        if self.company_bank < 1:
            print("У компании не достаточно средств!")
        elif self.company_bank - self.salary > 1:
            print(f"""Company_bank: {self.company_bank}""")

    def person_info(self):
        print(f"""Info: {self.first_name} {self.last_name}
Salary: {self.salary}""")


tom = Person(0, "Opera", "Pit", "Tom", 2500)
tom.get_salary()
tom.person_info()

sem = Person(5000, "Vega", "Baron", "Sem", 2400)
sem.get_salary()
sem.person_info()
